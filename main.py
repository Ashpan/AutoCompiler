from boxes import *
import os
from deskew import deskew
from ocr import labels
import time
def runBox():
    for file in os.listdir(path='./processing/'):
        os.remove("./processing/"+file)
    for file in os.listdir(path='./done/'):
        os.remove("./done/"+file)
    deskew("./new_scans/sheet.jpg", "./sheet/fixed_sheet.jpg")

    auto_box = box_extraction("./sheet/fixed_sheet.jpg","./cropped/", 2144, 968, 2, True) #AUTO
    delFile(1)
    fileLst = os.listdir(path='./cropped/')
    label1 = (labels("./cropped/"+fileLst[0]).split()[0])
    os.rename("./cropped/"+fileLst[0], "./processing/"+label1+".png")
    auto_sub_box = box_extraction("./processing/"+label1+".png","./cropped/", 920, 810, 1.13, True) #AUTO ROCKET AND CARGO
    os.unlink(path='./processing/Autonomous.png')
    fileLst = os.listdir(path='./cropped/')
    i = 0;
    for file in os.listdir(path='./cropped/'):
        ocrStr = labels("./cropped/"+file)
        if("Cargoship" in ocrStr):
            label2 = label1+"_Cargoship"
        elif("Rocket" in ocrStr):
            label2 = label1+"_Rocket"

        try:
            os.remove("./processing/"+label2+".png")
        except:
            print("didnt delete anything")
        os.rename("./cropped/"+fileLst[i], "./processing/"+label2+".png")
        i+=1;

    for file in os.listdir(path='./processing/'):
        label2 = file.split(".")[0]
        auto_sub_box = box_extraction("./processing/"+file,"./cropped/", 285, 275, 1.04, False) #AUTO ROCKET AND CARGO
        nameLst = []
        fileLst = []
        for sub_file in os.listdir(path='./cropped/'):
            # print(file)
            title = labels("./cropped/"+sub_file).split("\n")[0]
            if(not title in nameLst and not title is ''):
                nameLst.append(title)
                fileLst.append(sub_file)

        for sub_file in os.listdir(path='./cropped/'):
            if(not sub_file in fileLst):
                os.remove("./cropped/"+sub_file)
        
        for sub_file in os.listdir(path='./cropped/'):
            # print(sub_file)
            label3 = labels("./cropped/"+sub_file).split("\n")[0]
            label3 = label2+"_"+label3
            os.rename("./cropped/"+sub_file, "./processing/"+label3+".png")
            print(label3+".png")
        os.remove("./processing/"+label2+".png")
    for sub_file in os.listdir(path='./processing/'):
        box_extraction("./processing/"+sub_file, "./done/", 113, 113, 1, True)
        os.rename("./done/1.png", "./done/"+sub_file)

    # ----------------------------------------------------------------------------------------------
    empty_dir('processing')
    teleop_box = box_extraction("./sheet/fixed_sheet.jpg","./cropped/", 2160, 1558, 1.33, True) #Teleop
    fileLst = os.listdir(path='./cropped/')
    label1 = (labels("./cropped/"+fileLst[0]).split()[0])
    print(label1)
    os.rename("./cropped/"+fileLst[0], "./processing/"+label1+".png")
    teleop_sub_box = box_extraction("./processing/"+label1+".png","./cropped/", 906, 792, 906/792, True) #AUTO ROCKET AND CARGO
    os.unlink(path='./processing/Teleoperated.png')
    fileLst = os.listdir(path='./cropped/')
    i = 0;
    for file in os.listdir(path='./cropped/'):
        ocrStr = labels("./cropped/"+file)
        if("Cargoship" in ocrStr):
            label2 = label1+"_Cargoship"
        elif("Rocket" in ocrStr):
            label2 = label1+"_Rocket"

        try:
            os.remove("./processing/"+label2+".png")
        except:
            print("didnt delete anything")
        os.rename("./cropped/"+fileLst[i], "./processing/"+label2+".png")
        i+=1;

    for file in os.listdir(path='./processing/'):
        label2 = file.split(".")[0]
        teleop_sub_box = box_extraction("./processing/"+file,"./cropped/", 285, 275, 1.04, False) #AUTO ROCKET AND CARGO
        nameLst = []
        fileLst = []
        for sub_file in os.listdir(path='./cropped/'):
            # print(file)
            title = labels("./cropped/"+sub_file).split("\n")[0]
            if(not title in nameLst and not title is ''):
                nameLst.append(title)
                fileLst.append(sub_file)

        for sub_file in os.listdir(path='./cropped/'):
            if(not sub_file in fileLst):
                os.remove("./cropped/"+sub_file)
        
        for sub_file in os.listdir(path='./cropped/'):
            # print(sub_file)
            label3 = labels("./cropped/"+sub_file).split("\n")[0]
            label3 = label2+"_"+label3
            os.rename("./cropped/"+sub_file, "./processing/"+label3+".png")
            print(label3+".png")
        os.remove("./processing/"+label2+".png")
    for sub_file in os.listdir(path='./processing/'):
        box_extraction("./processing/"+sub_file, "./done/", 113, 113, 1, True)
        os.rename("./done/1.png", "./done/"+sub_file)


def empty_dir(directory):
    for file in os.listdir(path='./'+directory+'/'):
        os.remove('./'+directory+'/'+file)
    print("EMPTIED", directory)


runBox()