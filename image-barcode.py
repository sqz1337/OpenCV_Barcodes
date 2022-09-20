from pyzbar.pyzbar import decode
import cv2
import numpy as np
image = cv2.imread('images/pax1.jpg')
result = []
for code in decode(image):
    result.append(code.type)
    result.append(code.data.decode('utf-8'))
text_file = open("data.txt", "w")
text_file.write(str(result))
text_file.close()
print(result)



