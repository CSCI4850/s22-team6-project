import numpy as np
import cv2
import time


videoPath = "imageExamples\\drive.mp4"
#videoPath = "imageExamples\\drive2.mp4"

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
def getLines(image): #note: threshold of 30 seems to work well on lines
    lines = cv2.HoughLinesP(image, 0.3, np.pi/180, 30, np.array([]), minLineLength=35, maxLineGap=20)
    return lines


def displayLines(image, lines):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4) #converting to 1d array
            cv2.line(image, (x1, y1), (x2, y2), (255, 50, 255), 5)
    return image



def averageLines(lines):

    #get the average of left lines and right lines and print that
    print()


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
    original = frame
    original = cv2.resize(original, (900, 700))
    gray = original
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    canny = canyEdgeDetector(gray)
    #canny = cv2.GaussianBlur(canny, (3,3), 0)
    roi = getROI(canny)

    #get the lines in roi
    lines = getLines(roi)

    #averge lines
    averageLines(lines)

    #displaying lines on original
    original = displayLines(original,lines)


    color = (0, 255, 0)
    original = cv2.line(original,(522,437),(635,550),color,5)


 
    # Calculate FPS
    font = cv2.FONT_HERSHEY_SIMPLEX
    new_frame_time = time.time()
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = str(fps)
    cv2.putText(original, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
 
    # displaying the frame with fps
    cv2.imshow('frame', original)

    #DEBUG OUTPUTS
    #cv2.imshow('frame', canny)
    #cv2.imshow('frame', roi)
    #cv2.imshow('frame', th3)
 
    # press 'Q' if you want to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


 
# When everything done, release the capture
cap.release()
# Destroy the all windows now
cv2.destroyAllWindows()








