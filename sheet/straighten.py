###WRITTEN BY: ASHPAN RASKAR & BILAL QADAR###
# import the necessary packages
import numpy as np
import argparse
import cv2

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
