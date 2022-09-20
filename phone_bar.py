import cv2
import time
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture('http://192.168.0.104:8080/video')


cap.set(3, 640) #wight
cap.set(4, 480) #height

used_codes = []

while True:
    sucess, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Код подтвержден')
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print('Извините, данный код уже был использован')
            time.sleep(5)
        else:
            pass

    cv2.imshow('Test', frame)
    cv2.waitKey(1)


