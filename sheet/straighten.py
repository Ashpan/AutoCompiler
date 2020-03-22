###WRITTEN BY: ASHPAN RASKAR & BILAL QADAR###
# import the necessary packages
import numpy as np
from math import *
import argparse
import cv2
from PIL import Image

def reorient(image_name, dest_name):
	img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
	first_point = int(img.shape[0]*0.3)
	second_point = int(img.shape[0]*0.6)
	past_white = not(img[first_point][0] > 150)
	past_black = False
	for i in range(len(img[first_point])):
		if(img[first_point][i] < 100):
			past_white = True
		elif(img[first_point][i] > 190):
			past_black = True
		if(past_white and past_black):
			first_angle = i
			break
	past_white = not(img[second_point][0] > 150)
	past_black = False
	for i in range(len(img[second_point])):
		if(img[second_point][i] < 100):
			past_white = True
			past_black = False
		elif(img[second_point][i] > 190):
			past_black = True
		if(past_white and past_black):
			second_angle = i
			break
	print(first_angle, second_angle)
	opposite = abs(first_angle - second_angle)
	adjacent = abs(first_point - second_point)
	theta = degrees(atan(opposite/adjacent))
	print(theta)
	imag = Image.open(image_name)
	if(first_angle<second_angle):
		imag = imag.rotate(-theta, resample=0, expand=0, center=None, translate=None, fillcolor=None)
	else:
		imag = imag.rotate(theta, resample=0, expand=0, center=None, translate=None, fillcolor=None)
	imag.save(dest_name)

def remove_border(image_name, dest_name):
	img = cv2.imread(image_name)
	h,w = img.shape[:2]
	mask = np.zeros((h,w), np.uint8)

	# Transform to gray colorspace and invert Otsu threshold the image
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	# ***OPTIONAL FOR THIS IMAGE

	### Perform opening (erosion followed by dilation)
	kernel = np.ones((2,2),np.uint8)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

	# ***

	# Search for contours, select the biggest and draw it on the mask
	contours, hierarchy = cv2.findContours(opening, # if you use opening then change "thresh" to "opening"
	                                      cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	cnt = max(contours, key=cv2.contourArea)
	cv2.drawContours(mask, [cnt], 0, 255, -1)

	# Perform a bitwise operation
	res = cv2.bitwise_and(img, img, mask=mask)

	########### The result is a ROI with some noise
	########### Clearing the noise

	# Create a new mask
	mask = np.zeros((h,w), np.uint8)

	# Transform the resulting image to gray colorspace and Otsu threshold the image
	gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	# Search for contours and select the biggest one again
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	cnt = max(contours, key=cv2.contourArea)

	# Draw it on the new mask and perform a bitwise operation again
	cv2.drawContours(mask, [cnt], 0, 255, -1)
	res = cv2.bitwise_and(img, img, mask=mask)

	# If you will use pytesseract it is wise to make an aditional white border
	# so that the letters arent on the borders
	x,y,w,h = cv2.boundingRect(cnt)
	cv2.rectangle(res,(x,y),(x+w,y+h),(255,255,255),1)

	# Crop the result
	final_image = res[y:y+h+1, x:x+w+1]
	cv2.imwrite(dest_name, final_image)


def deskew(input_file, output_file):
	# construct the argument parse and parse the arguments

	# load the image from disk
	image = cv2.imread(input_file)

	# convert the image to grayscale and flip the foreground
	# and background to ensure foreground is now "white" and
	# the background is "black"
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.bitwise_not(gray)

	# threshold the image, setting all foreground pixels to
	# 255 and all background pixels to 0
	thresh = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# grab the (x, y) coordinates of all pixel values that
	# are greater than zero, then use these coordinates to
	# compute a rotated bounding box that contains all
	# coordinates
	coords = np.column_stack(np.where(thresh > 0))
	angle = cv2.minAreaRect(coords)[-1]

	# the `cv2.minAreaRect` function returns values in the
	# range [-90, 0); as the rectangle rotates clockwise the
	# returned angle trends to 0 -- in this special case we
	# need to add 90 degrees to the angle
	if angle < -45:
		angle = -(90 + angle)

	# otherwise, just take the inverse of the angle to make
	# it positive
	else:
		angle = -angle

	# rotate the image to deskew it
	(h, w) = image.shape[:2]
	center = (w // 2, h // 2)
	M = cv2.getRotationMatrix2D(center, angle, 1.0)
	rotated = cv2.warpAffine(image, M, (w, h),
		flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

	# show the output image
	# print("[INFO] angle: {:.3f}".format(angle))
	# cv2.imwrite(output_file, rotated)

	# image2 = cv2.imread(output_file)
	gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
	black_pixels = np.array(np.where(gray <= 190))

	first_black_pixel = black_pixels[:,0]

	last_black_pixel = black_pixels[:,-1]

	new_img = gray[first_black_pixel[0]:last_black_pixel[0], 0:len(gray[1])]

	cv2.imwrite(output_file, new_img)
