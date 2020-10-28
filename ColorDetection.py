import numpy as np
import cv2

capture = cv2.VideoCapture(0)
lower = np.array([100, 100, 100], dtype="uint8")
upper = np.array([255, 255, 255], dtype="uint8")

while(True):
    ret, frame = capture.read()
    image = frame
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    #color mask
    mask = cv2.inRange(hsv, lower, upper)

    maskedImage = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Light", maskedImage)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()