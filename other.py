import cv2
import numpy as np
from PIL import Image, ImageEnhance

def test():
	img3 = Image.open('houghlines5.jpg').convert('L')
	img3 = ImageEnhance.Color(img3).enhance(5)
	img3 = ImageEnhance.Contrast(img3).enhance(5)
	img3 = ImageEnhance.Brightness(img3).enhance(5)
	img3 = ImageEnhance.Sharpness(img3).enhance(5)
	img3.save('enhanced.jpg')


img = cv2.imread('box.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
cv2.imwrite('houghlines5.jpg',laplacian)
test()
img2 = cv2.imread('enhanced.jpg')

edges = cv2.Canny(img2,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
print(lines)
for line in lines:
	for x1,y1,x2,y2 in line:
		cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)


cv2.imwrite('houghlines10.jpg',img)


