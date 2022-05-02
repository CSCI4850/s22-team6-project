#Driver file that:
# 1) imports a generated model by CNN_model.ipynb
# 2) connect to the simulation
# 3) retrieves input data from sim
# 4) decodes input data and feeds it to the model
# 5) use the model to predict an action for the car
# 6) send that action to the car

# THIS PROGRAM RUNS THE SIMULATION - SHOULD BE FINAL PRODUCT

#Driver file that:
# 1) imports a generated model by CNN_model.ipynb
# 2) connect to the simulation
# 3) retrieves input data from sim
# 4) decodes input data and feeds it to the model
# 5) use the model to predict an action for the car
# 6) send that action to the car

# THIS PROGRAM RUNS THE SIMULATION - SHOULD BE FINAL PRODUCT

#import libraries
from tensorflow import keras
from keras.models import load_model #for importing the model
import numpy as np                  #for calculations and converting between formats
from io import BytesIO              #for input and output
#import socketio                     #for connecting to simualation
import eventlet
import socketio
import eventlet.wsgi
import argparse
from datetime import datetime
from PIL import Image
import os                           #for os actions
import base64                       #for decoding images that come from the simulation
from flask import Flask             #net framework that we use to connect
import cv2
import time

#min and max speed and speed limit:
MIN_SPEED = 1
MAX_SPEED = 28.5
speed_limit = MAX_SPEED


#set up connection to simulation
sio = socketio.Server()
app = Flask(__name__)
model = None
prev_image_array = None


new_frame_time = 0
prev_frame_time = time.time()

@sio.on("telemetry")
def telemetry(sid, data):
    global speed_limit
    global new_frame_time
    global prev_frame_time

    if data:
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        steering_angle = (float(data["steering_angle"]))
        steering_angle = steering_angle
        throttle = float(data["throttle"])
        speed = float(data["speed"])
        image = Image.open(BytesIO(base64.b64decode(data["image"])))
        try:
            image = np.asarray(image)
            image = preProcess(image)
            image = np.array([image])
            steering_angle = float(model.predict(image, batch_size=1))
            if speed > speed_limit:
                speed_limit = MIN_SPEED  # slow down
            else:
                speed_limit = MAX_SPEED
            if speed == 0:
                throttle = 1.0
            else:
                throttle = 1.0 - steering_angle**2 - (speed/speed_limit)**2
            print('{} {} {} {}'.format(steering_angle, throttle, speed, fps))
            send_control(steering_angle, throttle)
        except Exception as e:
            print(e)
@sio.on("connect")
def connect(sid, environ):
    print("connect ", sid)
    send_control(0,0)
                       
def send_control(steering_angle, throttle):
    sio.emit("steer", data = {'steering_angle':steering_angle.__str__(),'throttle':throttle.__str__()})
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote Driving')
    parser.add_argument('model',type = str,help='Path to h5 file. Model should be on the same path.')
    parser.add_argument('image_folder', type=str,nargs='?', default='', help='Path to image folder. This is where the images from the run will be saved.')
    args = parser.parse_args()
    model = load_model(args.model)
    if args.image_folder != '':
        print("Creating image folder at {}".format(args.image_folder))
        if not os.path.exists(args.image_folder):
            os.makedirs(args.image_folder)
        else:
            shutil.rmtree(args.image_folder)
            os.maskedirs(args.image_folder)
            ptiny("RECORDING THIS RUN..")
    else:
        print("NOT RECORDING THIS RUN...")
#retrieves the frame/image from the simulation and decodes it
def getImage():
    print("placeholder")

    
#process the image to the format that the model has been trained on
def preProcess(image): 
    
    #note by stijn:
    #used the same preprocessing steps as I did for training the model
    #should help the model perform better in the actual simulation
    image = image[60:130,:,:]                                     #crops image
    image = np.float32(image)                                     #convert to float
    image = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)                 #convert rbg to yuv for better line detection
    image = cv2.GaussianBlur(image,(3,3),0)                       #add light gassianblur
    image = cv2.resize(image,(200,60))                            #resize the image so that it can be processed faster
    image = image/255
    return image
    
   
#imports a *.h5 model from the same directory
def importModel(MODEL_NAME):
    
    #import model using keras
    model = "model-import-here"
    
    
    return model #returns the .h5 model       
app = socketio.Middleware(sio, app)
eventlet.wsgi.server(eventlet.listen(('', 4567)), app)