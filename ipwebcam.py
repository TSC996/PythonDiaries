import urllib.request
import cv2
import numpy as np

# replace with your own ip address
url = "http://192.168.43.1:8080/shot.jpg"

while True:

    imgResponse = urllib.request.urlopen(url)

# Numpy to convert into a array
    imgNp = np.array(bytearray(imgResponse.read()), dtype=np.uint8)

# decode the array via opencv to see a vunderstandable content
    img = cv2.imdecode(imgNp, -1)


# Put's image on the screen
    cv2.imshow("IPWebcam", img)

# Use 'q' to close the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
