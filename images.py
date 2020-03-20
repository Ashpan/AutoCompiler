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
    for file in os.listdir(path='./processing/completed/'):
        os.remove("./processing/completed/"+file)

    straighten.deskew("./processing/staged/" + file_name, "./processing/temporary/deskewed_sheet.jpg")
    straighten.remove_border("./processing/temporary/deskewed_sheet.jpg","./processing/temporary/removed_" + file_name)
    straighten.deskew("./processing/temporary/removed_" + file_name, "./processing/temporary/deskewed_sheet.jpg")
    #os.remove("./processing/staged/" + file_name)
    sheet = cv2.imread("./processing/temporary/deskewed_sheet.jpg")
    sheet = cv2.resize(sheet, (2496,2962))
    cv2.imwrite("./processing/temporary/preprocessed_sheet.jpg", sheet)
    sheet = cv2.imread("./processing/temporary/preprocessed_sheet.jpg")

    os.rename("./processing/staged/" + file_name,"./processing/previous_sheets/" + file_name)

    #This is the height and width of the box in which a single number is placed
    h = 65
    w = 38

    #This is the x,y location of the top left corner of the box in which a single number is placed
    x, y = 805, 532
    #Gap refers to the line width seperating 2 boxes.
    gap = 55
    cv2.imwrite("./processing/completed/team_num1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/team_num2.jpg", sheet[y:y+h, x+gap:x+gap+w])
    cv2.imwrite("./processing/completed/team_num3.jpg", sheet[y:y+h, x+2*gap:x+2*gap+w])
    cv2.imwrite("./processing/completed/team_num4.jpg", sheet[y:y+h, x+3*gap:x+3*gap+w])

    x, y = 1668, 530
    gap = 80
    cv2.imwrite("./processing/completed/match1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/match2.jpg", sheet[y:y+h, x+gap:x+gap+w])
    cv2.imwrite("./processing/completed/match3.jpg", sheet[y:y+h, x+2*gap:x+2*gap+w])

    x, y = 540, 1030
    gap = 55
    cv2.imwrite("./processing/completed/auto_rocket_cargo_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_rocket_cargo_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 930, 1030
    cv2.imwrite("./processing/completed/auto_rocket_cargo_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_rocket_cargo_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 538, 1320
    gap = 55
    cv2.imwrite("./processing/completed/auto_rocket_hatch_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_rocket_hatch_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 930, 1315
    cv2.imwrite("./processing/completed/auto_rocket_hatch_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_rocket_hatch_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])
# ------
    x, y = 1545, 1030
    cv2.imwrite("./processing/completed/auto_cargoship_cargo_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_cargoship_cargo_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 1935, 1030
    cv2.imwrite("./processing/completed/auto_cargoship_cargo_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_cargoship_cargo_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 1543, 1320
    cv2.imwrite("./processing/completed/auto_cargoship_hatch_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_cargoship_hatch_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 1935, 1320
    cv2.imwrite("./processing/completed/auto_cargoship_hatch_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/auto_cargoship_hatch_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])
    # -----------------
    x, y = 540, 1960
    cv2.imwrite("./processing/completed/teleop_rocket_cargo_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_rocket_cargo_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 930, 1960
    cv2.imwrite("./processing/completed/teleop_rocket_cargo_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_rocket_cargo_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 540, 2250
    cv2.imwrite("./processing/completed/teleop_rocket_hatch_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_rocket_hatch_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 935, 2250
    cv2.imwrite("./processing/completed/teleop_rocket_hatch_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_rocket_hatch_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])
# ------
    x, y = 1545, 1960
    cv2.imwrite("./processing/completed/teleop_cargoship_cargo_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_cargoship_cargo_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 1935, 1960
    cv2.imwrite("./processing/completed/teleop_cargoship_cargo_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_cargoship_cargo_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 1540, 2250
    cv2.imwrite("./processing/completed/teleop_cargoship_hatch_scored1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_cargoship_hatch_scored2.jpg", sheet[y:y+h, x+gap:x+gap+w])

    x, y = 1935, 2250
    cv2.imwrite("./processing/completed/teleop_cargoship_hatch_missed1.jpg", sheet[y:y+h, x:x+w])
    cv2.imwrite("./processing/completed/teleop_cargoship_hatch_missed2.jpg", sheet[y:y+h, x+gap:x+gap+w])
# ------
    x1, y1 = 395, 2521
    x2, y2 = 580, 2610
    cv2.imwrite("./processing/completed/climb_1.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 600, 2520
    x2, y2 = 818, 2600
    cv2.imwrite("./processing/completed/climb_2.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 830, 2520
    x2, y2 = 1020, 2610
    cv2.imwrite("./processing/completed/climb_3.jpg", sheet[y1:y2, x1:x2])
# ------
    x1, y1 = 1400, 2540
    x2, y2 = 1530, 2640
    cv2.imwrite("./processing/completed/defense_bad.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1540, 2540
    x2, y2 = 1690, 2640
    cv2.imwrite("./processing/completed/defense_meh.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1710, 2540
    x2, y2 = 1870, 2640
    cv2.imwrite("./processing/completed/defense_good.jpg", sheet[y1:y2, x1:x2])
# ------
    x1, y1 = 1400, 2745
    x2, y2 = 1530, 2845
    cv2.imwrite("./processing/completed/defense_line.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1545, 2750
    x2, y2 = 1690, 2850
    cv2.imwrite("./processing/completed/defense_cargo.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1710, 2750
    x2, y2 = 1865, 2845
    cv2.imwrite("./processing/completed/defense_pingpong.jpg", sheet[y1:y2, x1:x2])
# ------
    x1, y1 = 390, 2710
    x2, y2 = 1020, 2885
    cv2.imwrite("./processing/completed/comments.jpg", sheet[y1:y2, x1:x2])
