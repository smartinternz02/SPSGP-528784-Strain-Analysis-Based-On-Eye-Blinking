# SPSGP-528784-Strain-Analysis-Based-On-Eye-Blinking
Strain Analysis Based On Eye Blinking

Skills Required: Python, Open CV


Project Description:

Blinking is a reflex, which means your body does it automatically. Babies and children only blink about two times per minute. By the time you reach adolescence that increases to 14 to 17 times per minute. 
Detecting eye blinks is important for instance in systems that monitor a human operator vigilance, e.g. driver drowsiness, in systems that warn a computer user staring at the screen without blinking for a 
long time to prevent the dry eye and the computer vision syndromes, in human-computer interfaces that ease communication for disabled people. There should be an application that monitors to let the user 
know that he might get strained.

A neural network model is built which alerts the user if eyes are getting strained. This model uses the integrated webcam to capture the face (eyes) of the person. It captures the eye movement and counts 
the number of times a person blinks. If blink count deviates from the average value (if the number of blinks is less or more), then an alert is initiated by playing an audio message along with a  popup 
message is displayed on the screen appropriately.


import threading, time, cv2, dlib, argparse, scipy, gtts, playsound, tkinter  to run the code.

Demo Link : https://drive.google.com/file/d/17xOqZOREnUAwNoDtCLvcIJNY-fSWJHUQ/view?usp=sharing


       Note : 

       1)While Running the project place "shape_predictor_68_face_landmarks.dat" file in the same directory where the python file is placed.
       
       2) Run the file in the anaconda prompt by passing face land marks file as argument as below:
         "python eye_strain_analyzer.py --shape-predictor shape_predictor_68_face_landmarks.dat".
       
       3)Download suitable "dlib" library version which is suitable for your system python version.
       
       4) We taken an average eye blinks per minute as 20.Based on which the Strain is analyzed.
