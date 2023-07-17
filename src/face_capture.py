import cv2
import time
from datetime import datetime
import os

IMG_PATH = 'D:/Research/Computer Vision/FaceRecog/miai/dataset/FaceData/raw'
count = 50
usr_name = input("Input ur name: ")
USR_PATH = os.path.join(IMG_PATH, usr_name)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened() and count:
    isSuccess, frame = cap.read()
    if isSuccess :
        path = os.path.join(USR_PATH, f"{str(datetime.now())[:-7].replace(':', '-').replace(' ', '-')}{count}.jpg")
        cv2.imwrite(path, frame)
        count -= 1
        time.sleep(1)
    cv2.imshow('Face Capturing', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()