# create by: yashar zavary rezaie
import cv2

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    frame=cv2.flip(frame, 1)
    cv2.imshow("eye control", frame)
    cv2.waitKey(1)


