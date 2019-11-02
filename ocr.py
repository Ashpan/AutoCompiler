import pytesseract
import cv2
from number_rec import *

def labels(file_name):
    """LMFAO this was way easier then I thought"""
    gray = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    text = str(((pytesseract.image_to_string(gray))))
    return text

if __name__ == "__main__":
    label = labels("C:\\Users\\Ashpan\\Drive\\Current\\Programming\\1325Robotics\\Scouting\\Fuck Compiling\\bough\\cropped\\2.png")
    print(label.split(" ")[0])
