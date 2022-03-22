import cv2
import os


#for all stopsigns
for i in range(26):
	for j in range(30):

		if i > 9:
			if j > 9:
				name = "C:\\Users\\stijn\\Downloads\\archive\\Train\\14\\pCOLOR\\00014_000" + str(i) + "_000" + str(j) + ".png"
			else:
				name = "C:\\Users\\stijn\\Downloads\\archive\\Train\\14\\pCOLOR\\00014_000" + str(i) + "_0000" + str(j) + ".png"
		else:
			if j > 9:
				name = "C:\\Users\\stijn\\Downloads\\archive\\Train\\14\\pCOLOR\\00014_0000" + str(i) + "_000" + str(j) + ".png"
			else:
				name = "C:\\Users\\stijn\\Downloads\\archive\\Train\\14\\pCOLOR\\00014_0000" + str(i) + "_0000" + str(j) + ".png"
		
		print(name)
		print(os.getcwd())

		im_gray = cv2.imread(name, cv2.IMREAD_GRAYSCALE)

		output = "C:\\Users\\stijn\\Downloads\\archive\\Train\\14\\pCOLOR\\greyscaled\\0000-" + str(i) + str(j) + ".png"
		print("saved to: " + output)
		cv2.imwrite(output, im_gray)


