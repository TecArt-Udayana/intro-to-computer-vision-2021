import numpy as np
import cv2

img = cv2.imread("visualize/assets/road.jpg")
cv2.circle(img, (5, 5), 3, (0, 255, 0), 1)
cv2.imshow("Gambar BGR", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gambar Grayscale", img_gray)

output = img.copy()

edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)
cv2.imshow("Edges ", edges)

dilated_frame = cv2.dilate(edges, np.ones((5, 5), dtype=np.uint8))
cv2.imshow("Dilated frame", dilated_frame)

minLineLength = 10
maxLineGap = 50
lines = cv2.HoughLinesP(dilated_frame, 1.2, np.pi/180,
                        100, minLineLength, maxLineGap)

for x1, y1, x2, y2 in lines[:, 0]:
    cv2.line(output, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow("Found lines", output)
cv2.waitKey(0)
