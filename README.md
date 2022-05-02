# s22-team6-project Leabra

---------------------------

## Team Members:

James Coyle https://csci4850-5850-s22.slack.com/team/U02UAFZP0LW

Kwabena Owusu Fosuhene https://csci4850-5850-s22.slack.com/team/U02U2HMESSK

Le'Shawn Sears https://csci4850-5850-s22.slack.com/team/U02UAG284UE

Patrick Burnett https://csci4850-5850-s22.slack.com/team/U02UH7A60JF

Stijn Slump https://csci4850-5850-s22.slack.com/team/U02UAG05BAS


---------------------------

## Project Description:

Create a self-driving car that works in a simulation that runs on the unity engine

---------------------------

## Current Challenges

* make python program connect to simulation for car control

* start building the network

* train model

* test model

---------------------------

## Completed Challenges

* create more data by augmenting the original data

* clean data

* get simulation to run

* collect useful data

* analyze data

* write linedetection filter

---------------------------

## Demo

Our project uses a convolutional neural net to control a car in a simulated environment. Before any code can be run though, you will have to install the simulator we used from the following link: https://github.com/udacity/self-driving-car-sim. This simulator is useful because it has 2 modes, a training mode and an autonomous mode. The training mode allows you to manually drive the car as it collects data in the form on images and steering inputs. The autonomous mode allows you to upload a pretrained model to control the simulation by itself. Download version 2 for whatever system type you have. Extract the contents of the compressed file. The next step is to install anaconda to easily create an environment to run the simulation. Install anaconda from this link here: https://www.anaconda.com/. Download all of the files from the Demo folder on our github and put them in the same folder as the executable for the simulator. Open the anaconda prompt and navigate to the folder with all of the files and the simulator executable. From there, run the terminal command:

conda wnv create -f enviroment-gpu.yml

This command might take a while to execute as it creates an anaconda environment will all the necessary python libraries needed to connect to the simulator. Activate the environment with the command:

conda activate test2

Now we are ready to connect to the simulation. While keeping the terminal open, launch the simulator and start autonomous mode. Then type the command:

pyhton driver.py Test_Model.h5

into the terminal. It might take a minute for driver.py to connect to the simulation but the car should eventually start driving itself. The driver.py file works by creating a socket to send and receive data to and from the simulator. It takes data from the simulation as input, feeds that data through the pre-trained model in Test_Model.h5, and outputs a steering angle decided by the model and sets the speed of the car.

---------------------------
