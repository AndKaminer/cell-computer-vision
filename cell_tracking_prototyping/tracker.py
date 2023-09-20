import cv2
import numpy as np

from cell import Cell


class Tracker:

    def __init__(self):
        self.num_cells: int = 0
        self.cell_dict: dict[int, Cell] = {}
        self.curr_id: int = -1

    def register_cell(self, contour: np.array):
        cell = Cell(contour)
        self.cell_dict[self.curr_id] = cell
        self.num_cells += 1
        self.curr_id += 1

    def deregister_cell(self, cell_id: int):
        if cell_id in self.cell_dict:
            del self.cell_dict[cell_id]
            self.num_cells -= 1
        else:
            raise IndexError("Cell id not found in cell dictionary")

    def update_cell(self, cell_id: int, contour: np.array):
        if cell_id not in self.cell_dict:
            raise IndexError("Cell id not found in cell dictionary")
        else:
            self.cell_dict[cell_id].update(contour)

    def update(self, contours: list):
        if len(contours) == 0:
            return

        contours_centers = []
        for cnt in contours:
            M = cv2.moments(cnt)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            contours_centers.append((cnt, (cX, cY)))

            # sort by x coordinate
            contours_centers.sort(key=lambda el: el[1][0])

            # deregister first cell if its coordinates move backwards (ie it
            # reaches the edge of the screen and the coordinates move to
            # the next cell)

            if len(self.cell_dict) != 0:
                first_cell = self.cell_dict[self.curr_id - self.num_cells]
                first_new_cell = contours_centers[0]
                if first_cell.centerpoint[0] < first_new_cell[1][0]:
                    self.deregister_cell(self.curr_id - self.num_cells)

            for index, c in enumerate(contours_centers):
                current_cell_id = self.curr_id - self.num_cells + index

                if current_cell_id in self.cell_dict:
                    self.update_cell(current_cell_id, c[0])
                else:
                    self.register_cell(c[0])

    def show_contour_ids(self, frame):
        curr_frame = frame
        for cell_id in self.cell_dict:
            curr_frame = cv2.putText(img=curr_frame,
                                     text=str(cell_id),
                                     org=self.cell_dict[cell_id].text_loc(),
                                     fontFace=cv2.FONT_HERSHEY_PLAIN,
                                     fontScale=1,
                                     color=(0, 255, 0),
                                     thickness=1)

        return curr_frame
