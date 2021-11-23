#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# In[2]:


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
        

        print("=="*50)
        
        
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
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


# 원호님 - 좌표들 확인용 
data = [[lmk.x, lmk.y, lmk.z] for lmk in results.pose_landmarks.landmark]
print(data)


# In[4]:


print(results.pose_landmarks.landmark)


# In[5]:


results.pose_landmarks.landmark.__doc__


# In[6]:


type(results.pose_landmarks.landmark)


# In[7]:


type(landmarks)


# In[8]:


landmarks.__doc__


# In[9]:


for lndmrk in mp_pose.PoseLandmark:
    print(lndmrk)


# In[ ]:


#좌표값 확인 예시


# In[10]:


landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].visibility


# In[11]:


landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x


# In[12]:


landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y


# In[17]:


landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z


# In[13]:


list_poselandmark = [mp_pose.PoseLandmark.NOSE
,mp_pose.PoseLandmark.LEFT_EYE_INNER
,mp_pose.PoseLandmark.LEFT_EYE
,mp_pose.PoseLandmark.LEFT_EYE_OUTER
,mp_pose.PoseLandmark.RIGHT_EYE_INNER
,mp_pose.PoseLandmark.RIGHT_EYE
,mp_pose.PoseLandmark.RIGHT_EYE_OUTER
,mp_pose.PoseLandmark.LEFT_EAR
,mp_pose.PoseLandmark.RIGHT_EAR
,mp_pose.PoseLandmark.MOUTH_LEFT
,mp_pose.PoseLandmark.MOUTH_RIGHT
,mp_pose.PoseLandmark.LEFT_SHOULDER
,mp_pose.PoseLandmark.RIGHT_SHOULDER
,mp_pose.PoseLandmark.LEFT_ELBOW
,mp_pose.PoseLandmark.RIGHT_ELBOW
,mp_pose.PoseLandmark.LEFT_WRIST
,mp_pose.PoseLandmark.RIGHT_WRIST
,mp_pose.PoseLandmark.LEFT_PINKY
,mp_pose.PoseLandmark.RIGHT_PINKY
,mp_pose.PoseLandmark.LEFT_INDEX
,mp_pose.PoseLandmark.RIGHT_INDEX
,mp_pose.PoseLandmark.LEFT_THUMB
,mp_pose.PoseLandmark.RIGHT_THUMB
,mp_pose.PoseLandmark.LEFT_HIP
,mp_pose.PoseLandmark.RIGHT_HIP
,mp_pose.PoseLandmark.LEFT_KNEE
,mp_pose.PoseLandmark.RIGHT_KNEE
,mp_pose.PoseLandmark.LEFT_ANKLE
,mp_pose.PoseLandmark.RIGHT_ANKLE
,mp_pose.PoseLandmark.LEFT_HEEL
,mp_pose.PoseLandmark.RIGHT_HEEL
,mp_pose.PoseLandmark.LEFT_FOOT_INDEX
,mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]


# In[14]:


len(list_poselandmark)

