import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as dt
from joblib import dump,load
from sklearn import datasets, svm, metrics
from sklearn.datasets import fetch_openml
from PIL import Image, ImageEnhance, ImageFilter
import PIL.ImageOps
from matplotlib import image
from matplotlib import pyplot
from scipy import ndimage
import os

def is_empty(image_array,threshold):
    average = np.mean(image_array)
    if average > threshold:
        return False
    else:
        return True

def preprossess(file_name):
    #Model trained for images with resolution 784 x 784
    file_name = convert_png(file_name)
    basewidth = 28
    height = 28
    grey_image = Image.open(file_name).convert('L')
    grey_image = grey_image.filter(ImageFilter.GaussianBlur(2))
    #grey_image = ImageEnhance.Color(grey_image).enhance(1)
    grey_image = ImageEnhance.Brightness(grey_image).enhance(1)
    grey_image = ImageEnhance.Contrast(grey_image).enhance(1)
    #grey_image = ImageEnhance.Brightness(grey_image).enhance(1)
    grey_image = ImageEnhance.Sharpness(grey_image).enhance(3)

    #Change resolution to fit the model size
    grey_image = grey_image.resize((basewidth, height))
    invert_image = PIL.ImageOps.invert(grey_image)
    invert_image = invert_image.resize((basewidth, height))
    invert_image.save(os.path.basename(file_name)[:-4] + "_processed" + ".png")
    return(invert_image)

def number_recognition(file_name):

    img = preprossess(file_name)
    data = np.asarray(img)
    data = np.reshape(data, (1, 784))
    empty = is_empty(data,5)

    if not empty:
        X_data = data / 255.0
        #print(X_data)

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
    number = number_recognition("/Users/bilalqadar/Documents/GitHub/FuckCompiling/1.png")
    print(number)
