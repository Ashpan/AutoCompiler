###WRITTEN BY: BILAL QADAR & ASHPAN RASKAR###
import pytesseract
import cv2

def labels(file_name):
    """LMFAO this was way easier then I thought"""
    gray = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    text = str(((pytesseract.image_to_string(gray))))
    return text
