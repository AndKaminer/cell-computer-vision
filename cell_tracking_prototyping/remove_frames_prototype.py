import cv2
import numpy as np


VIDEO_NAME = "better_contrast_new.mp4"

object_detector = cv2.createBackgroundSubtractorMOG2(varThreshold=5)
cap = cv2.VideoCapture(VIDEO_NAME)
VIDEO_WIDTH = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
VIDEO_HEIGHT = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
RESIZE_DIM = (VIDEO_HEIGHT, VIDEO_HEIGHT)
DIFFERENCE_THRESHOLD = 50000000
CENTER_COORDS = (VIDEO_WIDTH // 2, VIDEO_HEIGHT // 2)


def crop(frame: np.array, center: tuple[int, int], width: int, height: int):
    left_bound = center[0] - width // 2
    right_bound = center[0] + width // 2
    upper_bound = center[1] + height // 2
    lower_bound = center[1] - height // 2

    return frame[lower_bound:upper_bound, left_bound:right_bound]


def frame_difference(frame1: np.array, frame2: np.array):
    img1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    img2 = cv2.cvtColor(frame2, cv2.COLOR_RGB2GRAY)

    result = (abs(img2 - img1)).sum()
    return result


ret, frame = cap.read()
frame = crop(frame, CENTER_COORDS, VIDEO_HEIGHT + 600, VIDEO_HEIGHT)

while True:
    last_frame = frame
    ret, frame = cap.read()

    if not ret:
        break

    frame = crop(frame, CENTER_COORDS, VIDEO_HEIGHT + 600, VIDEO_HEIGHT)

    fd = frame_difference(last_frame, frame)
    if fd < DIFFERENCE_THRESHOLD:
        continue

    mask = object_detector.apply(frame)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    big_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            big_contours.append(cnt)
            cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)

    cv2.imshow("FRAME", mask)
    key = cv2.waitKey(0)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
