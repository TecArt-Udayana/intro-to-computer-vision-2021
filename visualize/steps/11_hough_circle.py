import numpy as np
import cv2

img = cv2.imread("visualize/assets/planets.jpg")
cv2.circle(img, (5, 5), 3, (0, 255, 0), 1)
cv2.imshow("Gambar BGR", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gambar Grayscale", img_gray)

output = img.copy()
circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 1.05, 30)
print(len(circles[0, :]))
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5),
                      (x + 5, y + 5), (0, 128, 255), -1)


cv2.imshow("Found contours", output)
cv2.waitKey(0)
