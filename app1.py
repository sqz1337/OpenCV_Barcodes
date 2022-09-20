import streamlit as st
import os
from pyzbar.pyzbar import decode
import cv2
import numpy as np
from PIL import Image

def load_image(img):
    im = Image.open(img)
    return im

def main():
    menu = ['Считать штрих-код','LIVE-DECODER']

    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Считать штрих-код':
        st.subheader('Считать штрих-код')
        image_file = st.file_uploader('Загрузите изображение', type=['jpg','png','jpeg'])
        if image_file is not None:
            image = Image.open(image_file)
            image = np.array(image)
            image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            st.image(image)
            result = []
            for code in decode(image):
                result.append(code.type)
                result.append(code.data.decode('utf-8'))
            st.write(result)

    else:
        st.subheader('LIVE-DECODER')

if __name__ =='__main__':
    main()