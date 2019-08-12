import cv2
import numpy as np
from PIL import Image

img = cv2.imread('box.jpg')
img = cv2.resize(img, (70, 70))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,50,150, apertureSize=3)
# lines = cv2.HoughLines(edges,8,np.pi/180,300)
parameters = {'interval':1, 'accuracy':1, 'threshold':50, 'min_len':50,
        'max_gap':10}
polar = np.pi/180
lines = cv2.HoughLinesP(edges,parameters['interval'],parameters['accuracy']*polar, parameters['threshold'],
    parameters['min_len'], parameters['max_gap'])
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# cv2.lines(img,(x1,y1),(x2,y2),(0,0,255),2)
	
cv2.imshow('houghlines3.jpg',img)
cv2.waitKey(0)