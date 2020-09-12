import numpy as np
import cv2

img = cv2.imread('E:/Python Automations/Imageprocessing/elon_musk_tesla_3036.jpg')

### Getting a gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9 , 9)

### Cartoonizing the image

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

### Final Output
cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("CartoonImage", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()