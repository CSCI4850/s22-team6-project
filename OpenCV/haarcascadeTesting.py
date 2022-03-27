import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# Read in the cascade classifiers for stopsign and eyes
stopsign_cascade = cv2.CascadeClassifier("classifiers\\stopsign-1368p-4000n\\cascade.xml")

 
 
 
# create a function to detect stopsign
def adjusted_detect_stopsign(img):
     
    stopsign_img = img.copy()
     
    stopsign_rect = stopsign_cascade.detectMultiScale(stopsign_img,
                                              scaleFactor = 1.2,
                                              minNeighbors = 1)
     
    for (x, y, w, h) in stopsign_rect:
        cv2.rectangle(stopsign_img, (x, y),
                      (x + w, y + h), (255, 0, 255), 2)
         
    return stopsign_img
 

for i in range(6):
	# Reading in the image and creating copies
	inString = "imageExamples\\stopsign" + str(i+1) + ".png"
	outString = "output\\stopsign" + str(i+1) + ".jpg"
	print(inString)
	print(outString)
	img = cv2.imread(inString)

	 
	# Detecting the stopsign
	stopsign = adjusted_detect_stopsign(img)
	plt.imshow(stopsign)
	# Saving the image
	cv2.imwrite(outString, stopsign)