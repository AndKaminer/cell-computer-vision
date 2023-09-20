import cv2
import numpy as np
import matplotlib.pyplot as plt

from tracker import Tracker

import argparse


def crop(frame, x1, x2, y1, y2):
    return frame[y1:y2, x1:x2]


def frame_difference(frame1: np.array, frame2: np.array):
    img1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    img2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)

    result = (abs(img2 - img1)).sum()
    return result


parser = argparse.ArgumentParser(description="Test tracking")
parser.add_argument('--file', dest="file")
parser.add_argument('--diff', dest="diff")
parser.add_argument('--tThresh', dest='tThresh')

args = parser.parse_args()

VIDEO_NAME, DIFFERENCE_THRESHOLD, TRACKER_THRESHOLD = (args.file,
                                                       int(args.diff),
                                                       int(args.tThresh))

object_detector = cv2.createBackgroundSubtractorMOG2(
        varThreshold=TRACKER_THRESHOLD)
object_tracker = Tracker()

cap = cv2.VideoCapture(VIDEO_NAME)
ret, frame = cap.read()

cv2.namedWindow("Select Region", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Select Region", 1920, 1080)

r = cv2.selectROI("Select Region", frame, False)
x1, y1, width, height = r
x2, y2 = x1 + width, y1 + height

frame = crop(frame, x1, x2, y1, y2)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1920, 1080)

while True:
    last_frame = frame
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.GaussianBlur(frame, (7, 7), 0)
    frame = crop(frame, x1, x2, y1, y2)
    if frame_difference(last_frame, frame) < DIFFERENCE_THRESHOLD:
        continue

    mask = object_detector.apply(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    big_contours = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10:
            M = cv2.moments(cnt)
            cX = M["m10"] / M["m00"]
            if cX > x1 and cX < x2:
                big_contours.append(cnt)
                cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)

    object_tracker.update(big_contours)

    cv2.imshow("Image", object_tracker.show_contour_ids(frame))

    key = cv2.waitKey(20)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

cell = object_tracker.cell_dict[object_tracker.curr_id - 2]

fig, axes = plt.subplots(2, 2)

fig.suptitle("Statistics from the Experiment")

axes[0][1].scatter(cell.timesteps, cell.circularity_points)
axes[0][1].set_xlabel("Time (s)")
axes[0][1].set_ylabel("Circularity")
axes[0][1].set_title("Circularity Over Time")

axes[1][1].scatter(cell.timesteps, cell.area_points)
axes[1][1].set_xlabel("Time (s)")
axes[1][1].set_ylabel("Area (px)")
axes[1][1].set_title("Area Over Time")

cvp = [-el[1] for el in cell.velocity_points]

axes[1][0].scatter(cell.timesteps, cvp)
axes[1][0].set_xlabel("Time (s)")
axes[1][0].set_ylabel("Velocity (px/s)")
axes[1][0].set_title("Velocity Over Time")

axes[0][0].scatter(cell.timesteps, [el[0] for el in cell.location_points])
axes[0][0].set_xlabel("Time (s)")
axes[0][0].set_ylabel("Horizontal Position (px)")
axes[0][0].set_title("Horisontal Position Over Time")

plt.show()
