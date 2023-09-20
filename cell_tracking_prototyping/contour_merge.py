
import cv2
import numpy as np

from tracker import Tracker

import argparse
import math


def crop(frame, x1, x2, y1, y2):
    return frame[y1:y2, x1:x2]


def frame_difference(frame1: np.array, frame2: np.array):
    img1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    img2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)

    result = (abs(img2 - img1)).sum()
    return result

'''
def merge_contours(cnt1, cnt2):
    # contour format: array of points of format: [[x, y]]
    # step 1: delete all points inside other contour
    # step 2: merge points
    # step 3: sort in clockwise order
    # step 4: return contour

    merged_points = []
    cnt1.astype(np.float32)
    for point in cnt1:
        if cv2.pointPolygonTest(cnt2, [float(el) for el in point[0]],
                                False) == -1:
            merged_points.append(point)
    for point in cnt2:
        if cv2.pointPolygonTest(cnt1, [float(el) for el in point[0]],
                                False) == -1:
            merged_points.append(point)

    return sort_points(merged_points)


def sort_points(points):
    if not points:
        return []

    x = [p[0][0] for p in points]
    y = [p[0][1] for p in points]

    x0 = np.mean(x)
    y0 = np.mean(y)

    r = np.sqrt((x-x0)**2 + (y-y0)**2)

    angles = np.where((y-y0) > 0, np.arccos((x-x0)/r),
                      2*np.pi-np.arccos((x-x0)/r))

    mask = np.argsort(angles)

    x_sorted = x[mask]
    y_sorted = y[mask]

    zipped = list(zip(x_sorted, y_sorted))

    return [[xy] for xy in zipped]


def contour_in_circle(center_base, rad_base, cnt):
    # if distance between centers < rad + rad
    center, rad = cv2.minEnclosingCircle(cnt)
    distance = math.sqrt((center_base[0] - center[0])**2 +
                         (center_base[1] - center[1])**2)

    return distance < rad + rad_base


def process_large_contours(cnt, contours):
    # step 1: find bounding circle of large contour
    # step 2: find every contour with points inside bounding box
    # step 3: merge all contours together
    if len(contours) == 1:
        return contours, (0, 0), 0

    center, rad = cv2.minEnclosingCircle(cnt)
    contours_of_interest = []
    for c in contours:
        if contour_in_circle(center, rad, c):
            contours_of_interest.append(c)

    for c in contours_of_interest:
        cnt = merge_contours(cnt, c)

    return cnt, list(map(int, center)), int(rad)

'''


def merge_contours(big_contours):
    if len(big_contours) == 1:
        return big_contours

    i = 0
    while i < len(big_contours):
        pass


def find_if_close(cnt1, cnt2):
    row1, row2 = cnt1.shape[0], cnt2.shape[0]
    for i in range(row1):
        for j in range(row2):
            dist = np.linalg.norm(cnt1[i] - cnt2[j])
            if abs(dist) < 50:
                return True
            elif i == row1 - 1 and j == row2 - 1:
                return False


parser = argparse.ArgumentParser(description="Test tracking")
parser.add_argument('--file', dest="file")
parser.add_argument('--diff', dest="diff")
parser.add_argument('--tThresh', dest='tThresh')

args = parser.parse_args()

VIDEO_NAME, DIFFERENCE_THRESHOLD, TRACKER_THRESHOLD = (args.file,
                                                       int(args.diff),
                                                       int(args.tThresh))

object_detector = cv2.createBackgroundSubtractorMOG2(
        history=100,
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

    frame = crop(frame, x1, x2, y1, y2)
    if frame_difference(frame, last_frame) < DIFFERENCE_THRESHOLD:
        continue

    mask = object_detector.apply(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)

    big_contours = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10:
            # it is guaranteed that cnt is nonnull and contours has at least
            # one contour in it
            big_contours.append(cnt)

    real_contours = merge_contours(big_contours)

    for cnt in real_contours:
        cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)

    cv2.imshow("Image", object_tracker.show_contour_ids(frame))

    key = cv2.waitKey(60)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
