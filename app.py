from flask import Flask, render_template, request
import os
import pyzbar.pyzbar
from pyzbar.pyzbar import decode
import cv2
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
            return render_template('index.html')
@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = 'C:\\Users\\Amaterasu\Desktop\\barcodes_opencv' + imagefile.filename
    imagefile.save(image_path)

    image = Image.open(image_path)
    image = np.array(image)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    result = []
    for code in decode(image):
        # result.append(code.type)
        result.append(code.data.decode('utf-8'))

    return render_template('index.html', filenames=image, prediction = result)
if __name__ =='__main__':
    app.run(port=3000, debug=True)