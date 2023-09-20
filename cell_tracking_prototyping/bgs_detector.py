import cv2
import numpy as np


class Detector:

    def __init__(self, background: np.array, threshold: int, min_area: int):
        self.background = background
        self.threshold = threshold
        self.min_area = min_area

    def detect(self, frame):
        difference = cv2.absdiff(self.background, frame)
        ret, difference = cv2.threshold(difference, self.threshold, 255,
                                        cv2.THRESH_BINARY)
        if ret:
            return difference
        else:
            return None

    def filtered_detect(self, frame):
        # find contours and set contour to black if smaller than some area
        mask = self.detect(frame)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)
        self.filter_contours(mask, contours)

        # gaussian blur and second threshold
    #    mask = cv2.GaussianBlur(mask, (11, 11), 255)
     #   ret, mask = cv2.threshold(mask, 50, 255, cv2.THRESH_BINARY)

        return mask

    def filter_contours(self, frame, contours):
        noise = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < self.min_area:
                noise.append(cnt)

        cv2.drawContours(frame, noise, -1, color=(0, 0, 0), thickness=cv2.FILLED)
