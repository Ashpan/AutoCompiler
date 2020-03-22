### WRITTEN BY: BILAL QADAR & ASHPAN RASKAR ###
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
from sheet import boxes_coordinates

def empty_dir(directory):
    for file in os.listdir(path='./'+directory+'/'):
        os.remove('./'+directory+'/'+file)
    print("EMPTIED", directory)

def runBox(file_name):
    """runBox is when the data is cropped into a useable form. Sheets are descewed
    and enhanced in this step. As well all image and file management occurs. This
    function needs to be modified for any new sheets. Each single number or chec
    box needs to be cropped and moved to the temporary folders. Strongly recommend
    using https://www.image-map.net/ to help find coordinates."""

    for file in os.listdir(path='./processing/temporary'):
        os.remove("./processing/temporary/"+file)
    for file in os.listdir(path='./processing/previous_sheets'):
        os.remove("./processing/previous_sheets/"+file)
    for file in os.listdir(path='./processing/completed/'):
        os.remove("./processing/completed/"+file)
    straighten.reorient("./processing/staged/" + file_name, "./processing/temporary/reoriented.jpg")
    straighten.deskew("./processing/temporary/reoriented.jpg", "./processing/temporary/deskewed_sheet.jpg")
    straighten.remove_border("./processing/temporary/deskewed_sheet.jpg","./processing/temporary/removed_" + file_name)
    straighten.deskew("./processing/temporary/removed_" + file_name, "./processing/temporary/deskewed_sheet.jpg")
    # os.remove("./processing/staged/" + file_name)
    sheet = cv2.imread("./processing/temporary/deskewed_sheet.jpg")
    sheet = cv2.resize(sheet, (2289,2962))
    cv2.imwrite("./processing/temporary/preprocessed_sheet.jpg", sheet)
    sheet = cv2.imread("./processing/temporary/preprocessed_sheet.jpg")
    # os.rename("./processing/staged/" + file_name,"./processing/previous_sheets/" + file_name)

    small_boxes = boxes_coordinates.small_boxes
    h = 95
    w = 99
    for key in small_boxes:
        x,y = small_boxes[key][0], small_boxes[key][1]
        new_sheet = sheet[y:y+h, x:x+w]
        print("Writing: ", key, "\t", [x,y] ,[x+w, y+h])
        cv2.imwrite("./processing/temporary/" + key + "_boxes.jpg", new_sheet)
        straighten.remove_border("./processing/temporary/" + key + "_boxes.jpg","./processing/completed/" + key + ".jpg")
        os.remove("./processing/temporary/" + key + "_boxes.jpg")
    return(small_boxes.keys())

