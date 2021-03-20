import cv2
import numpy as np


def hough_transform_circle(img, param_2=200, param_1=10, min_radius=20, max_radius=35, threshold_1=120,
                           threshold_2=240):
    print('p1,p2,min,max', param_2, param_1, min_radius, max_radius)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("hough_result/hough_gray.jpg", gray)
    # Blur the image to reduce noise
    img_blur = cv2.medianBlur(gray, 5)
    cv2.imwrite("hough_result/hasilblur",img_blur)
    # Canny edge detection
    img_canny = cv2.Canny(img_blur, threshold_1, threshold_2)
    cv2.imwrite("hough_result/hough_canny.jpg", img_canny)
    # Apply hough transform on the image
    circles = cv2.HoughCircles(img_canny, cv2.HOUGH_GRADIENT, 1, img.shape[0] / 20, param1=param_2, param2=param_1,
                               minRadius=min_radius,
                               maxRadius=max_radius)
    if circles is not None:
        cv2.imwrite("hough_result/hough_result.jpg", circles)

    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Show result
    result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    img_canny = cv2.cvtColor(img_canny, cv2.COLOR_GRAY2RGB)
    return gray, img_canny, result


def hough_transform_line(img, max_slider=0, min_line_length=3, max_line_gap=20, threshold_1=50,
                         threshold_2=200):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("hough_result/hasilbgr.jpg", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("hough_result/hasilgray.jpg", gray)
    # Find the edges in the image using canny detector
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.Canny(gray, threshold_1, threshold_2)
    cv2.imwrite("hough_result/hasilblur.jpg", gray)
    cv2.imwrite("hough_result/hasilcanny.jpg", edges)

    # Probabilistic Hough
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, max_slider, minLineLength=min_line_length, maxLineGap=max_line_gap)
    # Draw lines on the image
    idx = 1
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)
            print("Line {} x1 = {}, y1 = {}, x2 = {}, y2 = {}, ".format(idx, x1, y1, x2, y2))
            idx += 1
    # Show result
    result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return gray, edges, result, lines


def erosi_citra(img):
    # Threshold the image
    ret, img = cv2.threshold(img, 127, 255, 0)

    # Step 1: Create an empty skeleton
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)

    # Get a Cross Shaped Kernel
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    # Repeat steps 2-4
    while True:
        # Step 2: Open the image
        open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
        # Step 3: Substract open from the original image
        temp = cv2.subtract(img, open)
        # Step 4: Erode the original image and refine the skeleton
        eroded = cv2.erode(img, element)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()
        # Step 5: If there are no white pixels left ie.. the image has been completely eroded, quit the loop
        if cv2.countNonZero(img) == 0:
            break
    return skel
