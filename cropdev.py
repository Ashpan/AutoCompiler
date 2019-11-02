import cv2
# Will be saving coords as (x1, y1), (x2, y2)
cropCoord = [
[(0, 280),(145, 625)],
[(75, 280),(220, 625)],
[(160, 280),(305, 625)],
[(295, 280),(440, 625)],
[(388, 280),(533, 625)],
[(471, 280),(616, 625)]
]

img = cv2.imread("testimg.JPG")
for i in range(len(cropCoord)):
	crop_img = img[cropCoord[i][0][1]:cropCoord[i][1][1], cropCoord[i][0][0]:cropCoord[i][1][0]]
	cv2.imshow("cropped", crop_img)
	cv2.waitKey(0)