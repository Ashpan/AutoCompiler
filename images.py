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

small_boxes =   {
  "team1": (245, 125),
  "team2": (342, 125),
  "team3": (439, 125),
  "team2": (536, 125),
  "match1": (918, 125),
  "match2": (1015, 125),

  "moved_off_line": (1737, 261),
  "auto": (2167, 260),
  "auto_cell_picked": (1258, 427),
  "auto_cell_missed": (1258, 580),
  "auto_low_scored": (1735, 425),
  "auto_cell_missed": (2168, 426),
  "auto_outer_scored": (1738, 579),
  "auto_outer_missed": (2168, 578),
  "auto_cell_picked": (1901, 728),

  "cycle1_cellintake_2": (1023, 1007),
  "cycle1_cellintake_3_2": (1144, 1007),
  "cycle1_cellintake_4_3": (1263, 1007),
  "cycle1_lower_scored": (1381, 1007),
  "cycle1_lower_missed": (1480, 1007),
  "cycle1_outer_scored": (1604, 1007),
  "cycle1_outer_missed": (1708, 1007),
  "cycle1_inner_scored": (1850, 1005),
  "cycle1_def": (2160, 1003),

  "cycle2_cellintake_2": (1023, 1111),
  "cycle2_cellintake_3_2": (1144, 1111),
  "cycle2_cellintake_4_3": (1263, 1111),
  "cycle2_lower_scored": (1381, 1111),
  "cycle2_lower_missed": (1480, 1111),
  "cycle2_outer_scored": (1604, 1109),
  "cycle2_outer_missed": (1708, 1111),
  "cycle2_inner_scored": (1850, 1109),
  "cycle2_def": (2160, 1107),

  "cycle3_cellintake_2": (1023, 1215),
  "cycle3_cellintake_3_2": (1144, 1215),
  "cycle3_cellintake_4_3": (1263, 1215),
  "cycle3_lower_scored": (1381, 1215),
  "cycle3_lower_missed": (1480, 1215),
  "cycle3_outer_scored": (1604, 1215),
  "cycle3_outer_missed": (1708, 1215),
  "cycle3_inner_scored": (1850, 1213),
  "cycle3_def": (2160, 1211),

  "cycle4_cellintake_2": (1023, 1318),
  "cycle4_cellintake_3_2": (1144, 1318),
  "cycle4_cellintake_4_3": (1263, 1318),
  "cycle4_lower_scored": (1381, 1318),
  "cycle4_lower_missed": (1480, 1318),
  "cycle4_outer_scored": (1604, 1317),
  "cycle4_outer_missed": (1708, 1318),
  "cycle4_inner_scored": (1850, 1316),
  "cycle4_def": (2160, 1314),

  "cycle5_cellintake_2": (1023, 1417),
  "cycle5_cellintake_3_2": (1144, 1417),
  "cycle5_cellintake_4_3": (1263, 1417),
  "cycle5_lower_scored": (1381, 1417),
  "cycle5_lower_missed": (1480, 1417),
  "cycle5_outer_scored": (1604, 1417),
  "cycle5_outer_missed": (1708, 1417),
  "cycle5_inner_scored": (1850, 1415),
  "cycle5_def": (2160, 1413),

  "cycle6_cellintake_2": (1023, 1529),
  "cycle6_cellintake_3_2": (1144, 1529),
  "cycle6_cellintake_4_3": (1263, 1529),
  "cycle6_lower_scored": (1381, 1529),
  "cycle6_lower_missed": (1480, 1529),
  "cycle6_outer_scored": (1604, 1529),
  "cycle6_outer_missed": (1708, 1529),
  "cycle6_inner_scored": (1850, 1527),
  "cycle6_def": (2160, 1525),

  "cycle7_cellintake_2": (1023, 1643),
  "cycle7_cellintake_3_2": (1144, 1643),
  "cycle7_cellintake_4_3": (1263, 1643),
  "cycle7_lower_scored": (1381, 1643),
  "cycle7_lower_missed": (1480, 1643),
  "cycle7_outer_scored": (1604, 1643),
  "cycle7_outer_missed": (1708, 1643),
  "cycle7_inner_scored": (1850, 1641),
  "cycle7_def": (2160, 1639),

  "cycle8_cellintake_2": (1023, 1755),
  "cycle8_cellintake_3_2": (1144, 1755),
  "cycle8_cellintake_4_3": (1263, 1755),
  "cycle8_lower_scored": (1381, 1755),
  "cycle8_lower_missed": (1480, 1755),
  "cycle8_outer_scored": (1604, 1755),
  "cycle8_outer_missed": (1708, 1755),
  "cycle8_inner_scored": (1850, 1753),
  "cycle8_def": (2160, 1751),

  "cycle9_cellintake_2": (1023, 1866),
  "cycle9_cellintake_3_2": (1144, 1866),
  "cycle9_cellintake_4_3": (1263, 1866),
  "cycle9_lower_scored": (1381, 1866),
  "cycle9_lower_missed": (1480, 1866),
  "cycle9_outer_scored": (1604, 1866),
  "cycle9_outer_missed": (1708, 1866),
  "cycle9_inner_scored": (1850, 1864),
  "cycle9_def": (2160, 1862),

  "cycle10_cellintake_2": (1023, 1978),
  "cycle10_cellintake_3_2": (1144, 1978),
  "cycle10_cellintake_4_3": (1263, 1978),
  "cycle10_lower_scored": (1381, 1978),
  "cycle10_lower_missed": (1480, 1978),
  "cycle10_outer_scored": (1604, 1978),
  "cycle10_outer_missed": (1708, 1978),
  "cycle10_inner_scored": (1850, 1976),
  "cycle10_def": (2160, 1974),

  "final_attempt_color": (2159, 2078),
  "control_first": (917, 2211),
  "control_second": (1141, 2209),
  "control_second_m": (1263, 2209),
  "control_third": (1478, 2209),
  "control_third_m": (1605, 2208),
  "target_colour": (2159, 2197),



  "fits_under": (11, 1548),
  "low_port": (481, 1545),
  "defense_strat_shot": (11, 1757),
  "defense_strat_zone": (11, 1870),
  "defense_strat_other": (11, 1982),

  "defense_level_good": (483, 1754),
  "defense_level_med": (483, 1867),
  "defense_level_bad": (483, 1978),

  "fouls_regular": (303, 2210),
  "defense_level_bad": (730, 2210),

  "climb_self_climb": (12, 2416),
  "climb_failed_climb": (14, 2525),
  "climb_did_not_attempt": (12, 2634),
  "climb_assisted_by": (15, 2749),
  "climb_lifted": (15, 2864),
  "climb_park": (480, 2413),
  "climb_failed_park": (480, 2522),
  "climb_robots_climbed": (479, 2633),
  "climb_scaled_levelled": (480, 2749)
}

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
    os.rename("./processing/staged/" + file_name,"./processing/previous_sheets/" + file_name)

    h = 95
    w = 99
    for key in small_boxes:
        x,y = small_boxes[key][0], small_boxes[key][1]
        new_sheet = sheet[y:y+h, x:x+w]
        print(key, [x,y,x+w, y+h])
        cv2.imwrite("./processing/temporary/" + key + "_boxes.jpg", new_sheet)
        straighten.remove_border("./processing/temporary/" + key + "_boxes.jpg","./processing/completed/" + key + ".jpg")
        os.remove("./processing/temporary/" + key + "_boxes.jpg")


