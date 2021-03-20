import numpy as np
import cv2

img = cv2.imread("visualize/assets/planets.jpg")
cv2.circle(img, (5, 5), 3, (0, 255, 0), 1)
cv2.imshow("Gambar BGR", img)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Gambar HSV", img_hsv)

lower_hsv = np.array([0, 0, 0])
upper_hsv = np.array([179, 255, 245])
only_planet = cv2.inRange(img_hsv, lower_hsv, upper_hsv)
cv2.imshow("Only Planets", only_planet)

eroded_frame = cv2.erode(only_planet, np.ones((5, 5), dtype=np.uint8))
cv2.imshow("Eroded", eroded_frame)
dilated_frame = cv2.dilate(eroded_frame, np.ones((5, 5), dtype=np.uint8))
cv2.imshow("Dilated", dilated_frame)

contours_canvas = img.copy()
contours, hierarchy = cv2.findContours(
    dilated_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))
contours_canvas = cv2.drawContours(
    contours_canvas, contours, -1, (0, 255, 0), 3)

cv2.imshow("Found contours", contours_canvas)
cv2.waitKey(0)
