import threading
import time
import cv2
import dlib
import argparse
from scipy.spatial import distance
from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os


def generate_and_play_sound():
        
        speech=gTTS("Please Takes some rest")
        speech.save("../output11.mp3")
        playsound("../output11.mp3")


def popupmsg():
    
    popup = tk.Tk()
    popup.wm_title("Urgent")
    style = ttk.Style(popup)
    style.theme_use('classic')
    style.configure('Test.TLabel', background='aqua')
    label = ttk.Label(popup, text="Take some rest", style='Test.TLabel', width=50)
    label.pack(side='top', fill="x", pady=10)
    generate_and_play_sound()
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()
    
    
     

def calculate_EAR(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear_aspect_ratio = (A+B)/(2.0*C)
    return ear_aspect_ratio
    

def process_frame():
    global blink
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--shape-predictor", required=True,
                help="path to facial landmark predictor")
    ap.add_argument("-v", "--video", type=str, default="",
                help="path to input video file")
    args = vars(ap.parse_args())
    cap = cv2.VideoCapture(0)
    hog_face_detector = dlib.get_frontal_face_detector()
    dlib_facelandmark = dlib.shape_predictor(args["shape_predictor"])

    while True:
        
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = hog_face_detector(gray)
        for face in faces:
            face_landmarks = dlib_facelandmark(gray, face)
            x11=face.left()
            y11=face.top()
            x22=face.right()
            y22=face.bottom()
        leftEye = []
        rightEye = []

        for n in range(36,42):

            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x,y))
            next_point = n+1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        for n in range(42,48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x,y))
            next_point = n+1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame,(x,y),(x2,y2),(0,255,0),1)

        left_ear = calculate_EAR(leftEye)
        right_ear = calculate_EAR(rightEye)

        EAR = (left_ear+right_ear)/2
        EAR = round(EAR,2)
        
        if EAR<0.15:
            cv2.putText(frame,"Blink",(20,100),
                cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),4)
            cv2.putText(frame,"-----",(20,400),
                cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
            
            blink=blink+1
        # print(EAR)
        print(blink)
        cv2.rectangle(frame,(x11,y11),(x22,y22),(136,8,8),2)
        cv2.imshow("Are you Sleepy", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()




global c
c=1


def run_every_60_seconds():
    global blink
    global c
    if c==0:
        if blink < 20 :

            print("------Strained------")
            blink = 0
            popupmsg()

        
    c=0
    
    
    blink = 0

    
    threading.Timer(60, run_every_60_seconds).start()


blink = 0


run_every_60_seconds()


process_frame()


# python final.py --shape-predictor shape_predictor_68_face_landmarks.dat