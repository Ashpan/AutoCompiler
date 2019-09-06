import matplotlib.pyplot as plt
import numpy as np
from joblib import dump,load
from sklearn.datasets import fetch_openml
from matplotlib import image
from scipy import ndimage
import cv2
import os
import math

def field_empty(image_array,threshold):
    average = np.mean(image_array)
    if average > threshold:
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

def preprocess(file_name):
    gray = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
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

def number_recognition(file_name):

    data = preprocess(file_name)
    data = np.reshape(data, (1, 784))
    empty = field_empty(data,5)

    if not empty:
        X_data = data / 255.0

        classifier = load('model.joblib')
        prediction = classifier.predict(X_data)
        return(prediction)

    else:
        return [None]

def test_data(directory):
    images = os.listdir(directory)
    size = len(images)
    individual_acc = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    correct = 0
    incorrect = 0
    for i in range(len(images)):
        guess = number_recognition(os.path.join(directory,images[i]))

        if guess[0] == images[i][0]:
            correct += 1
            individual_acc[int(images[i][0])] += 1
        else:
            incorrect += 1
        print("Guess for " + images[i] + ": " + str(guess[0]))

    accuracy = (correct/size)*100
    for key in individual_acc.keys():
        ind_acc = (individual_acc[key]/(size/10))*100
        print(str(key) + " Accuracy: " + str(ind_acc))

    print("Overall Accuracy: " + str(accuracy))
    print("Test Set Size: " + str(size))

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

if __name__ == "__main__":
    number = test_data("/Users/bilalqadar/Documents/GitHub/FuckCompiling/test_data/pencil_set")
    print(number)
    #pre("/Users/bilalqadar/Documents/GitHub/FuckCompiling/test_data/pencil_set/0_1.png")
