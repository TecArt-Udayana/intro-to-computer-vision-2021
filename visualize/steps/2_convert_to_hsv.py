import cv2

# Load gambar raw
img = cv2.imread("visualize/assets/alpha-big.png")
# Tampilkan gambar raw
cv2.imshow("Gambar BGR", img)

# Ubah menjadi hsv
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Tampilkan gambar hsv
cv2.imshow("Gambar HSV", img_hsv)

# Kasih delay
cv2.waitKey(0)