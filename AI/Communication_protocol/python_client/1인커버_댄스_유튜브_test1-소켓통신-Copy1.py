#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import numpy as np
import socket # TCP, UDP 송신용 
import sys
mp_drawing = mp.solutions.drawing_utils

mp_pose = mp.solutions.pose

SOCKET_IP = '127.0.0.1'
SOCKET_PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP 소켓
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP 소켓


# In[2]:


"""
2021년 11월쯤에 유튜브에서 싫어요를 제외시켜서
자꾸 실행할때 싫어요에 관련된 오류가 발생함
pafy 에 가서        
self._dislikes = self._ydl_info['dislike_count']
이 문장을 삭제하면 잘됨
리스트 형태로 보내니까 - 유니티에서 로그가 매번 갱신함 
즉- 업데이트가 잘됨
문제는 보내는게 string 형식이라 문제임
"""
import cv2, pafy
url = 'https://www.youtube.com/watch?v=EnCVaLIOIV4'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
#best = video.getbest(preftype='webm')     # 'mp4','3gp'
best = video.getbest()
print('best.resolution', best.resolution)


cap=cv2.VideoCapture(best.url)

## Setup mediapipe instance
with mp_pose.Pose(static_image_mode=True,enable_segmentation=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
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
        

        print("=="*10)
        
        
        # Extract landmarks- 하드코딩 - 그래야 보기 편함,배열 형식인데, - 리스트로 변경 - C#에서 받기 쉬움
        # 하드 코딩 한 이유 - 송신자가 어떤것을 보내는지 보기용, 수신자는 어떤것을 받는지 확인용
        #landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x 형식임, 
        try:
            landmarks = results.pose_landmarks.landmark
            #print(landmarks)
            
            list_poselandmark_x = [
                landmarks[mp_pose.PoseLandmark.NOSE.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x
                ,landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x
                ,landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x
                ,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x
                ,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x
            ]

            list_poselandmark_y = [
                landmarks[mp_pose.PoseLandmark.NOSE.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y
                ,landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y
                ,landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y
                ,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y
                ,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y
            ]


            list_poselandmark_z = [
                landmarks[mp_pose.PoseLandmark.NOSE.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].z
                ,landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].z
                ,landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].z
                ,landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].z
                ,landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].z
            ]
            
            
                             
            print(list_poselandmark_x)
            print("xx"*20)
            print(list_poselandmark_y)
            print("yy"*20)
            print(list_poselandmark_z)
            print("zz"*20)
            
            
            
            
            #UDP 소켓 통신 - 하드코딩으로 변경
            #그런데 float 형식으로 udp를 못 보내고 str 형태로 udp 를 보낼수있다
            x_data = str(list_poselandmark_x)
            y_data = str(list_poselandmark_y)
            z_data = str(list_poselandmark_z)
            sock.sendto(x_data.encode(), (SOCKET_IP, SOCKET_PORT))
            sock.sendto(y_data.encode(), (SOCKET_IP, SOCKET_PORT))
            sock.sendto(z_data.encode(), (SOCKET_IP, SOCKET_PORT))
            
            
            ###

        except:
            pass
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
              
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# In[ ]:


"""
2021년 11월쯤에 유튜브에서 싫어요를 제외시켜서
자꾸 실행할때 싫어요에 관련된 오류가 발생함
pafy 에 가서        
self._dislikes = self._ydl_info['dislike_count']
이 문장을 삭제하면 잘됨
특이한건 딕셔너리 형태로 보내면 unity에서 로그한곳에서 연속적으로 받는다 
- 즉 업데이트가 안될수도 있음
문제는 보내는게 string 형식이라 문제임

"""
import cv2, pafy
url = 'https://www.youtube.com/watch?v=EnCVaLIOIV4'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
#best = video.getbest(preftype='webm')     # 'mp4','3gp'
best = video.getbest()
print('best.resolution', best.resolution)


cap=cv2.VideoCapture(best.url)

## Setup mediapipe instance
with mp_pose.Pose(static_image_mode=True,enable_segmentation=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
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
        

        print("=="*10)
        
        
        # Extract landmarks- 하드코딩 - 그래야 보기 편함,배열 형식인데, - 리스트로 변경 - C#에서 받기 쉬움
        # 하드 코딩 한 이유 - 송신자가 어떤것을 보내는지 보기용, 수신자는 어떤것을 받는지 확인용
        #landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x 형식임, 
        try:
            landmarks = results.pose_landmarks.landmark
            #print(landmarks)
            
            list_poselandmark_x = {
            "landmarks[mp_pose.PoseLandmark.NOSE.value].x" : landmarks[mp_pose.PoseLandmark.NOSE.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x
            ,"landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x" : landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x
            ,"landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x" : landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x
            ,"landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x" : landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x" : landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x
            }

            list_poselandmark_y = {
            "landmarks[mp_pose.PoseLandmark.NOSE.value].y" : landmarks[mp_pose.PoseLandmark.NOSE.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y
            ,"landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y " : landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y
            ,"landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y" : landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y
            ,"landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y" : landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y" : landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y
            }


            list_poselandmark_z = {
            "landmarks[mp_pose.PoseLandmark.NOSE.value].z" : landmarks[mp_pose.PoseLandmark.NOSE.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].z
            ,"landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].z" : landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].z
            ,"landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].z" : landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].z
            ,"landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].z" : landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].z
            ,"landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].z" : landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].z
            }

            
                             
            print(list_poselandmark_x)
            print("xx"*20)
            print(list_poselandmark_y)
            print("yy"*20)
            print(list_poselandmark_z)
            print("zz"*20)
            
            
            
            
            #UDP 소켓 통신 - 하드코딩으로 변경
            #그런데 float 형식으로 udp를 못 보내고 str 형태로 udp 를 보낼수있다
            x_data = str(list_poselandmark_x)
            y_data = str(list_poselandmark_y)
            z_data = str(list_poselandmark_z)
            sock.sendto(x_data.encode(), (SOCKET_IP, SOCKET_PORT))
            sock.sendto(y_data.encode(), (SOCKET_IP, SOCKET_PORT))
            sock.sendto(z_data.encode(), (SOCKET_IP, SOCKET_PORT))
            
            
            ###

        except:
            pass
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                 )               
              
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# In[3]:


len(list_poselandmark_x)

