import cv2

img = cv2.imread("visualize/assets/alpha-big.png")
cv2.imshow("Gambar BGR", img)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("Gambar HSV", img_hsv)

cv2.waitKey(0)