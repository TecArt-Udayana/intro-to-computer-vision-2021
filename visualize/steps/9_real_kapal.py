import numpy as np
import cv2

img = cv2.imread("visualize/assets/kapal-2.jpeg")
cv2.circle(img, (5, 5), 3, (0, 255, 0), 1)
cv2.imshow("Gambar BGR", img)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Gambar HSV", img_hsv)

lower_red = np.array([0, 178, 150])
upper_red = np.array([10, 255, 255])
only_orange = cv2.inRange(img_hsv, lower_red, upper_red)
cv2.imshow("Only Orange", only_orange)

lower_blue = np.array([79, 70, 74])
upper_blue = np.array([94, 255, 255])
only_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
cv2.imshow("Only Orange", only_orange)

only_hsv = cv2.bitwise_or(only_orange, only_blue)

eroded_frame = cv2.erode(only_hsv, np.ones((3, 3), dtype=np.uint8))
cv2.imshow("Eroded", eroded_frame)
dilated_frame = cv2.dilate(eroded_frame, np.ones((13, 13), dtype=np.uint8))
cv2.imshow("Dilated", dilated_frame)

contours_canvas = img.copy()
contours, hierarchy = cv2.findContours(
    dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))
contours_canvas = cv2.drawContours(contours_canvas, contours, -1, (0,0,255), 3)

# for i, it in enumerate(contours):
#     M = cv2.moments(it)
#     bbox = cv2.boundingRect(it)
#     x, y, w, h = bbox
#     # cv2.rectangle(contours_canvas, (x, y), (x+w, y+h), (255, 255, 0), 3)
#     # cv2.circle(contours_canvas, ((x+w//2), (y+h//2)), 5, (0, 255, 255), -3)

cv2.imshow("Found contours", contours_canvas)
cv2.waitKey(0)
