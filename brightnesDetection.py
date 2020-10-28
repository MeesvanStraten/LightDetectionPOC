import argparse

import cv2

capture = cv2.VideoCapture(0)
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

while(True):
    ret, frame = capture.read()

    image = frame
    orig = image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (41,41), 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    image = orig.copy()
    cv2.circle(gray, maxLoc, 41, (255, 0, 0), 2)

    cv2.imshow("Bright:)", gray)




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()