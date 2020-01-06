from boxes import *
import os
from deskew import deskew
from ocr import labels
import time
from PIL import Image  


def empty_dir(directory):
    for file in os.listdir(path='./'+directory+'/'):
        os.remove('./'+directory+'/'+file)
    print("EMPTIED", directory)


def runBox():
    for file in os.listdir(path='./processing/'):
        os.remove("./processing/"+file)
    for file in os.listdir(path='./done/'):
        os.remove("./done/"+file)
    deskew("./new_scans/sheet.jpg", "./sheet/deskewed_sheet.jpg")
    sheet = cv2.imread("./sheet/deskewed_sheet.jpg")
    sheet = cv2.resize(sheet, (2496,2962))  
    cv2.imwrite("./sheet/fixed_sheet.jpg", sheet)
    sheet = cv2.imread("./sheet/fixed_sheet.jpg")
    h = 128
    w = 124
    x, y = 460, 712
    cv2.imwrite("./done/auto_rocket_cargo_scored.jpg", sheet[y:y+h, x:x+w])

    x, y = 912, 712
    cv2.imwrite("./done/auto_rocket_cargo_missed.jpg", sheet[y:y+h, x:x+w])

    x, y = 460, 1059
    cv2.imwrite("./done/auto_rocket_hatch_scored.jpg", sheet[y:y+h, x:x+w])
    
    x, y = 912, 1059
    cv2.imwrite("./done/auto_rocket_hatch_missed.jpg", sheet[y:y+h, x:x+w])
# ------
    x, y = 1608, 722
    cv2.imwrite("./done/auto_cargoship_cargo_scored.jpg", sheet[y:y+h, x:x+w])

    x, y = 2055, 722
    cv2.imwrite("./done/auto_cargoship_cargo_missed.jpg", sheet[y:y+h, x:x+w])

    x, y = 1608, 1059
    cv2.imwrite("./done/auto_cargoship_hatch_scored.jpg", sheet[y:y+h, x:x+w])
    
    x, y = 2055, 1059
    cv2.imwrite("./done/auto_cargoship_hatch_missed.jpg", sheet[y:y+h, x:x+w])

    # -----------------
    x, y = 460, 1807
    cv2.imwrite("./done/teleop_rocket_cargo_scored.jpg", sheet[y:y+h, x:x+w])

    x, y = 912, 1807
    cv2.imwrite("./done/teleop_rocket_cargo_missed.jpg", sheet[y:y+h, x:x+w])

    x, y = 460, 2154
    cv2.imwrite("./done/teleop_rocket_hatch_scored.jpg", sheet[y:y+h, x:x+w])
    
    x, y = 912, 2154
    cv2.imwrite("./done/teleop_rocket_hatch_missed.jpg", sheet[y:y+h, x:x+w])
# ------
    x, y = 1608, 1817
    cv2.imwrite("./done/teleop_cargoship_cargo_scored.jpg", sheet[y:y+h, x:x+w])

    x, y = 2055, 1817
    cv2.imwrite("./done/teleop_cargoship_cargo_missed.jpg", sheet[y:y+h, x:x+w])

    x, y = 1608, 2154
    cv2.imwrite("./done/teleop_cargoship_hatch_scored.jpg", sheet[y:y+h, x:x+w])
    
    x, y = 2055, 2154
    cv2.imwrite("./done/teleop_cargoship_hatch_missed.jpg", sheet[y:y+h, x:x+w])

    x1, y1 = 298, 2477
    x2, y2 = 521, 2592
    cv2.imwrite("./done/climb_1.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 521, 2477
    x2, y2 = 795, 2592
    cv2.imwrite("./done/climb_2.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 795, 2477
    x2, y2 = 1030, 2592
    cv2.imwrite("./done/climb_3.jpg", sheet[y1:y2, x1:x2])

    x1, y1 = 1446, 2502
    x2, y2 = 1607, 2638
    cv2.imwrite("./done/defense_bad.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1607, 2502
    x2, y2 = 1794, 2638
    cv2.imwrite("./done/defense_meh.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1794, 2502
    x2, y2 = 1994, 2638
    cv2.imwrite("./done/defense_good.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1994, 2502
    x2, y2 = 2234, 2638
    cv2.imwrite("./done/defense_clamps.jpg", sheet[y1:y2, x1:x2])

    x1, y1 = 1446, 2745
    x2, y2 = 1607, 2881
    cv2.imwrite("./done/defense_line.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1607, 2745
    x2, y2 = 1794, 2881
    cv2.imwrite("./done/defense_cargo.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1794, 2745
    x2, y2 = 1994, 2881
    cv2.imwrite("./done/defense_pingpong.jpg", sheet[y1:y2, x1:x2])
    x1, y1 = 1994, 2745
    x2, y2 = 2234, 2881
    cv2.imwrite("./done/defense_clamps.jpg", sheet[y1:y2, x1:x2])

    x1, y1 = 296, 2711
    x2, y2 = 1029, 2920
    cv2.imwrite("./done/comments.jpg", sheet[y1:y2, x1:x2])

    x1, y1 = 716, 131
    x2, y2 = 998, 209
    cv2.imwrite("./done/team_number.jpg", sheet[y1:y2, x1:x2])

    x1, y1 = 1712, 119
    x2, y2 = 2006, 204
    cv2.imwrite("./done/match_number.jpg", sheet[y1:y2, x1:x2])





runBox()