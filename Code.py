
import cv2
import random

def take_Snapshot():
    video_capture_object=cv2.VideoCapture(0)
    number = random.randint(0,100)
    result = True
    while(result):
        ret, frame = video_capture_object.read()
        img_name = "Image"+number+".png"
        cv2.imwrite(img_name, frame)
        result = False
take_Snapshot()
