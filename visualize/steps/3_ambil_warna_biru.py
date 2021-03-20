import cv2

img = cv2.imread("visualize/assets/alpha-big.png")
cv2.imshow("Gambar BGR", img)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Gambar HSV", img_hsv)

import numpy as np
lower_hsv = np.array([0,150,0])
upper_hsv = np.array([179,255,210])

only_blue = cv2.inRange(img_hsv, lower_hsv, upper_hsv)
cv2.imshow("Only Blue", only_blue)

cv2.waitKey(0)