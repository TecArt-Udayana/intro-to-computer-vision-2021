#Import library
import cv2

# Baca gambar file
img = cv2.imread("visualize/assets/alpha-big.png") # visualize/assets/alpha-big.png
cv2.imshow("Judul window", img)
cv2.waitKey(0)