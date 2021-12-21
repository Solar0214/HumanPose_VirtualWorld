#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import threading
import cv2, pafy
import mediapipe as mp
import json
import numpy as np
import socket # TCP, UDP 송신용 
import sys
mp_drawing = mp.solutions.drawing_utils

mp_pose = mp.solutions.pose

SOCKET_IP = '127.0.0.1'
SOCKET_PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP 소켓
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP 소켓

url = 'https://www.youtube.com/watch?v=EnCVaLIOIV4'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
# best = video.getbest(preftype='webm')     # 'mp4','3gp'
best = video.getbest()
print('best.resolution', best.resolution)

cap = cv2.VideoCapture(best.url)

## Setup mediapipe instance
with mp_pose.Pose(static_image_mode=True, enable_segmentation=True, min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        print("==" * 10)

        try:
            landmarks = results.pose_landmarks.landmark
            # print(landmarks)

            final_data = [{"X": lmk.x, "Y": lmk.y, "Z": lmk.z} for lmk in results.pose_landmarks.landmark]

            #print(final_data)
            print("###" * 2)
            

            try:
                item = {"items": final_data}
                item = json.dumps(item)
                print("O-O"*10)
                print(item)
                
            except:
                print("item에서 에러 발생")

            Message = str(json.loads(item.replace("\n", "")))#.replace("\n", "")
            sock.sendto(Message.encode(), (SOCKET_IP, SOCKET_PORT))

        except:
            pass  # countinue로 하면 cap창이 안뜸

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2)
                                  )

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

