import cv2


def crop(frame, x1, x2, y1, y2):
    return frame[y1:y2, x1:x2]


FILE_NAME = "video.cine"

cap = cv2.VideoCapture(FILE_NAME)

ret, img = cap.read()

cv2.namedWindow("Select Region", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Select Region", 1920, 1080)

r = cv2.selectROI("Select Region", img, False)
x1, y1, width, height = r
x2, y2 = x1 + width, y1 + height

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1920, 1080)

img = crop(img, x1, x2, y1, y2)

cv2.imshow("Image", img)

key = cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
