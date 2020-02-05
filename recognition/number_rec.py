###WRITTEN BY: BILAL QADAR & ASHPAN RASKAR###

import matplotlib.pyplot as plt
import numpy as np
from joblib import dump,load
from sklearn.datasets import fetch_openml
from matplotlib import image
from scipy import ndimage
import cv2
import os
import math


def field_empty(image,threshold):
    """Takes an image path and returns whether it is empty
    or not. The threshold parameter is the amount of noise an image can have
    and this function still concludes it is empty"""

    image_array = cv2.resize(image,(200,200))
    white = 0
    black = 0
    for row in image_array:
        #print(row)
        for pixel in row:
            #print(pixel[2])
            if pixel < 250:
                black += 1
            else:
                white += 1

    if black > threshold:
        return False
    else:
        return True

def getBestShift(img):
    cy,cx = ndimage.measurements.center_of_mass(img)

    rows,cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)

    return shiftx,shifty

def shift(img,sx,sy):
    rows,cols = img.shape
    M = np.float32([[1,0,sx],[0,1,sy]])
    shifted = cv2.warpAffine(img,M,(cols,rows))
    return shifted

def preprocess(image_array):
    gray = image_array
    (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY
        | cv2.THRESH_OTSU)

    gray = cv2.GaussianBlur(gray,(5,5),0)
    gray = cv2.resize(255-gray,(28,28))

    while np.sum(gray[0]) == 0:
        gray = gray[1:]

    while np.sum(gray[:,0]) == 0:
        gray = np.delete(gray,0,1)

    while np.sum(gray[-1]) == 0:
        gray = gray[:-1]

    while np.sum(gray[:,-1]) == 0:
        gray = np.delete(gray,-1,1)

    rows,cols = gray.shape

    if rows > cols:
        factor = 20.0/rows
        rows = 20
        cols = int(round(cols*factor))
		# first cols than rows
        gray = cv2.resize(gray, (cols,rows))
    else:
        factor = 20.0/cols
        cols = 20
        rows = int(round(rows*factor))
        # first cols than rows
        gray = cv2.resize(gray, (cols, rows))

    colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
    rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
    gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

    shiftx,shifty = getBestShift(gray)
    shifted = shift(gray,shiftx,shifty)
    return shifted

def number_recognition(image_array):
    empty = field_empty(image_array,3000)
    data = preprocess(image_array)
    data = np.reshape(data, (1, 784))
    if not empty:
        X_data = data / 255.0

        classifier = load('./recognition/model.joblib')
        prediction = classifier.predict(X_data)
        return(prediction[0])

    else:
        return '0'

def convert_png(file_path):
    file_name, file_extenstion = os.path.splitext(file_path)

    if file_extenstion == ".png" or file_extenstion == ".jpg":
        if file_extenstion == ".jpg":
            img = Image.open(file_path)
            img.save(file_name + ".png")
            os.remove(file_path)
        return file_name + ".png"
    else:
        raise TypeError("Image must be a .jpg or .png file")
