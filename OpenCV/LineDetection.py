import numpy as np
import cv2
import time


videoPath = "C:\\Users\\stijn\\Documents\\GitHub\\s22-team6-project\\OpenCV\\imageExamples\\drive.mp4"
#videoPath = "C:\\Users\\stijn\\Documents\\GitHub\\s22-team6-project\\OpenCV\\imageExamples\\drive2.mp4"

#used to detect edges in an image/frame
def canyEdgeDetector(image):
    edged = cv2.Canny(image, 250, 350)
    return edged


#create a area of interest we care about 
def getROI(image):
    height = image.shape[0]
    width = image.shape[1]
    # Defining Triangular ROI: The values will change as per your camera mounts
    triangle = np.array([[(0, height-150), (width, height-150), (int(width/(1.5)), int(height/1.6)), (int(width/(4)), int(height/1.6))]])
    # creating black image same as that of input image
    black_image = np.zeros_like(image)
    # Put the Triangular shape on top of our Black image to create a mask
    mask = cv2.fillPoly(black_image, triangle, 255)
    # applying mask on original image
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

#finds the lines in the image
def getLines(image):
	lines = cv2.HoughLinesP(image, 0.3, np.pi/180, 30, np.array([]), minLineLength=50, maxLineGap=20)
	return lines


def displayLines(image, lines):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4) #converting to 1d array
            cv2.line(image, (x1, y1), (x2, y2), (255, 50, 255), 5)
    return image

# creating the videocapture object
# and reading from the input file
# Change it to 0 if reading from webcam
cap = cv2.VideoCapture(videoPath)

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

# Reading the video file until finished
while(cap.isOpened()):
 
    # Capture frame-by-frame
 
    ret, frame = cap.read()
 
    # if video finished or no Video Input
    if not ret:
        break
 
    # Our operations on the frame come here
    gray = frame

    # resizing the frame size according to our need
    gray = cv2.resize(gray, (900, 700))
    canny = canyEdgeDetector(gray)
    roi = getROI(canny)



    #get the lines in roi
    lines = getLines(roi)


    gray = displayLines(gray,lines)


 
    # font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX
    # time when we finish processing for this frame
    new_frame_time = time.time()
 
    # Calculating the fps
 
    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    # converting the fps into integer
    fps = int(fps)
 
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
 
    # putting the FPS count on the frame
    cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
 
    # displaying the frame with fps
    cv2.imshow('frame', gray)

    #DEBUG OUTPUTS
    #cv2.imshow('frame', canny)
    #cv2.imshow('frame', roi)
 
    # press 'Q' if you want to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


 
# When everything done, release the capture
cap.release()
# Destroy the all windows now
cv2.destroyAllWindows()








