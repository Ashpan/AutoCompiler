import cv2
import numpy as np

img = cv2.imread('box.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,100,apertureSize = 3)
parameters = {'interval':1, 'accuracy':1, 'threshold':5, 'min_len':50, 'max_gap':100}
polar = np.pi/180
lines = cv2.HoughLinesP(edges,parameters['interval'],parameters['accuracy']*polar, parameters['threshold'], parameters['min_len'], parameters['max_gap'])
for line in lines:
	print(line)
	for x1,y1,x2,y2 in line:
	    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('houghlines5.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
