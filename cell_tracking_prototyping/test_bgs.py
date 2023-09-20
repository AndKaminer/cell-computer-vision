import cv2
import numpy as np
import matplotlib.pyplot as plt

from tracker import Tracker
from bgs_detector import Detector

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
object_tracker = Tracker()

cap = cv2.VideoCapture(VIDEO_NAME)
ret, frame = cap.read()

cv2.namedWindow("Select Region", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Select Region", 1920, 1080)

r = cv2.selectROI("Select Region", frame, False)
x1, y1, width, height = r
x2, y2 = x1 + width, y1 + height

frame = crop(frame, x1, x2, y1, y2)

object_detector = Detector(frame, 10, 10)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1920, 1080)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = crop(frame, x1, x2, y1, y2)

    diff = object_detector.filtered_detect(frame)
    cv2.imshow("Image", frame)
    cv2.imshow("Mask", diff)

    key = cv2.waitKey(20)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
