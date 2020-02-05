###WRITTEN BY: BILAL QADAR & ASHPAN RASKAR###
import sys
import os
import time
import cv2
from PIL import Image
sys.path.insert(0, '/sheet/')
sys.path.insert(0, '/recognition/')
from sheet import boxes
from sheet import straighten
from recognition import ocr
from recognition import number_rec
import numpy as np


def empty_dir(directory):
    for file in os.listdir(path='./'+directory+'/'):
        os.remove('./'+directory+'/'+file)
    print("EMPTIED", directory)

def get_rect(file_name,box_parameters):
    """File name is the name of the .jpg file of the entire survey which must be
    located in the temporary/staged/ folder. Width and height are number of
    pixels which make up the box which contains each question. Undersize these
    values. Oversizing these images will result in none crops made. The destination
    of the cropped files will be in the /processing/completed folder."""

    for file in os.listdir(path='./processing/temporary'):
        os.remove("./processing/temporary/"+file)
    for file in os.listdir(path='./processing/completed/'):
        os.remove("./processing/completed/"+file)

    straighten.deskew("./processing/staged/" + file_name, "./processing/temporary/deskewed_sheet.jpg")
    os.remove("./processing/staged/" + file_name)
    sheet = cv2.imread("./processing/temporary/deskewed_sheet.jpg")
    sheet = cv2.resize(sheet, (2450,2962))
    cv2.imwrite("./processing/temporary/preprocessed_sheet.jpg", sheet)

    os.rename("./processing/staged/" + file_name,"./processing/previous_sheets/" + file_name)
    w1,h1 = box_parameters
    rects = findCnt("./processing/temporary/preprocessed_sheet.jpg",w1,h1)

    for i in range(len(rects)):
        cv2.imwrite("./processing/completed/cropped_sheet" + str(i) + ".jpg", rects[i])
        relabel("./processing/completed/cropped_sheet" + str(i) + ".jpg")

def get_data(directory,box_parameters):
    """Want to add another kind of data type? This is where you do it!"""
    start_point,w,h,lw = box_parameters
    x,y = start_point
    num_data = {}
    check_data = {}

    for file in os.listdir(directory):
        num_boxes = file[1]
        data_type = file[2]
        name = file[5:len(file)-4]
        img = cv2.imread(os.path.join(directory,file),cv2.COLOR_BGR2GRAY)

        for i in range(len(num_boxes)):
            crop = img[y:y+h,x-((i+1)*w)-(i*lw): x-(i*w)-(i*lw)]
            temp = []

            if data_type == "N":
                img = cv2.imread(os.path.join(directory,file),cv2.IMREAD_GRAYSCALE)
                crop = img[y:y+h,x-((i+1)*w)-(i*lw): x-(i*w)-(i*lw)]

                value = number_rec.number_recognition(crop)
                temp.append(value)

            elif data_type == "T":
                value = number_rec.field_empty(crop,3000)
                if value == True:
                    check_data[name] = str(False)
                else:
                    check_data[name] = str(True)

            final_val = ""
            #The contents of temp are in reverse order so we need to flip it
            for i in range(len(temp)):
                final_val += temp[len(temp)- 1- i]

            num_data[name] = final_val
    return (num_data,check_data)

def relabel(image):
    dir = os.path.dirname(image)
    label = ocr.labels(image)
    q_index = label.find("?")
    label = label[0:q_index]
    label = label.lstrip()
    label = label.rstrip()
    label = label.replace(" ", "_")
    os.rename(image,os.path.join(dir,label + ".jpg"))

def findCnt(image_name,width,height,fill=100):
    img = cv2.imread(image_name,0)
    h, w = img.shape[:2]
    kernel = np.ones((15,15),np.uint8)

    e = cv2.erode(img,kernel,iterations = 2)
    d = cv2.dilate(e,kernel,iterations = 1)
    ret, th = cv2.threshold(d, 150, 255, cv2.THRESH_BINARY_INV)

    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(th, mask, (fill,fill), 255); # position = (200,200)
    out = cv2.bitwise_not(th)
    out= cv2.dilate(out,kernel,iterations = 3)

    cnt, h = cv2.findContours(out,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    rects = []
    for i in range(len(cnt)):
        area = cv2.contourArea(cnt[i])

        if (area > 1.5*(width*height) and area < 5*width*height):
            mask = np.zeros_like(img)
            cv2.drawContours(mask, cnt, i, 255, -1)
            x,y,w,h = cv2.boundingRect(cnt[i])
            rects.append(img[y:h+y,x:w+x])

    return rects
