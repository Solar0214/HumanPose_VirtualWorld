import cv2
import pafy
import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt
from matplotlib import cm

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For static images:
IMAGE_FILES = []
BG_COLOR = (192, 192, 192) # gray
with mp_pose.Pose(
    static_image_mode=True,
    model_complexity=2,
    enable_segmentation=True,
    min_detection_confidence=0.5) as pose:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_height, image_width, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if not results.pose_landmarks:
      continue
    print(
        f'Nose coordinates: ('
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
        f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
    )

    annotated_image = image.copy()
    # Draw segmentation on the image.
    # To improve segmentation around boundaries, consider applying a joint
    # bilateral filter to "results.segmentation_mask" with "image".
    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
    bg_image = np.zeros(image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    annotated_image = np.where(condition, annotated_image, bg_image)
    # Draw pose landmarks on the image.
    mp_drawing.draw_landmarks(
        annotated_image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)
    # Plot pose world landmarks.
    mp_drawing.plot_landmarks(
        results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)

# For webcam input:

# url = 'https://www.youtube.com/watch?v=IZAv5Tj8a8A'
# url = 'https://www.youtube.com/watch?v=9FRVCN_5ATc'
url = 'https://www.youtube.com/watch?v=9FRVCN_5ATc'
video = pafy.new(url)
best = video.getbest()
cap=cv2.VideoCapture(best.url)

# cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))

    # draw skeleton 3d map

    # data = [[lmk.x, lmk.y, lmk.z] for lmk in results.pose_landmarks.landmark]

    # fig = plt.figure()
    # fig.set_size_inches(15, 15)
    # ax = plt.axes(projection='3d')
    # surf = ax.contour3D(data_x, data_y, data_z, 50, cmap=cm.coolwarm)
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')
    # ax.set_title('3D contour')
    # plt.show()

    # data = [[lmk.x, lmk.y, lmk.z] for lmk in results.pose_landmarks.landmark]
    # print(data)

    if cv2.waitKey(5) & 0xFF == 27:
      break

data = [[lmk.x, lmk.y, lmk.z] for lmk in results.pose_landmarks.landmark]
# data = np.transpose(data)
#
# data_x = data[0]
# data_y = data[1]
# data_z = data[2]

cap.release()

#############################################GRPC

def getData():
    global data
    return data

from concurrent import futures
import time

import grpc

import virtual_pb2 as user_messages
import virtual_pb2_grpc as users_service

class data_Streaming(users_service.data_streamServicer):
    dataXYZ = None
    def __init__(self):
        self.dataXYZ = getData()
    def streaming(self, request, context):
        dataXYZ = np.transpose(self.dataXYZ)
        data_x = dataXYZ[0]
        data_y = dataXYZ[1]
        data_z = dataXYZ[2]

        data = user_messages.data
            (landmark_x1 = data_x[0],
                landmark_y1 = ,
                landmark_z1 = ,

                landmark_x2 = ,
                landmark_y2 = ,
                landmark_z2 = ,

                landmark_x3 = ,
                landmark_y3 = ,
                landmark_z3 = ,

                landmark_x4 = ,
                landmark_y4 = ,
                landmark_z4 = ,

                landmark_x5 = ,
                landmark_y5 = ,
                landmark_z5 = ,

                landmark_x6 = ,
                landmark_y6 = ,
                landmark_z6 = ,

                landmark_x7 = ,
                landmark_y7 = ,
                landmark_z7 = ,

                landmark_x8 = ,
                landmark_y8 = ,
                landmark_z8 = ,

                landmark_x9 = ,
                landmark_y9 = ,
                landmark_z9 = ,

                landmark_x10 = ,
                landmark_y10 = ,
                landmark_z10 = ,

                landmark_x11 = ,
                landmark_y11 = ,
                landmark_z11 = ,

                landmark_x12 = ,
                landmark_y12 = ,
                landmark_z12 = ,

                landmark_x13 = ,
                landmark_y13 = ,
                landmark_z13 = ,

                landmark_x14 = ,
                landmark_y14 = ,
                landmark_z14 = ,

                landmark_x15 = ,
                landmark_y15 = ,
                landmark_z15 = ,

                landmark_x16 = ,
                landmark_y16 = ,
                landmark_z16 = ,

                landmark_x17 = ,
                landmark_y17 = ,
                landmark_z17 = ,

                landmark_x18 = ,
                landmark_y18 = ,
                landmark_z18 = ,

                landmark_x19 = ,
                landmark_y19 = ,
                landmark_z19 = ,

                landmark_x20 = ,
                landmark_y20 = ,
                landmark_z20 = ,

                landmark_x21 = ,
                landmark_y21 = ,
                landmark_z21 = ,

                landmark_x22 = ,
                landmark_y22 = ,
                landmark_z22 = ,

                landmark_x23 = ,
                landmark_y23 = ,
                landmark_z23 = ,

                landmark_x24 = ,
                landmark_y24 = ,
                landmark_z24 = ,

                landmark_x25 = ,
                landmark_y25 = ,
                landmark_z25 = ,

                landmark_x26 = ,
                landmark_y26 = ,
                landmark_z26 = ,

                landmark_x27 = ,
                landmark_y27 = ,
                landmark_z27 = ,

                landmark_x28 = ,
                landmark_y28 = ,
                landmark_z28 = ,

                landmark_x29 = ,
                landmark_y29 = ,
                landmark_z29 = ,

                landmark_x30 = ,
                landmark_y30 = ,
                landmark_z30 = ,

                landmark_x31 = ,
                landmark_y31 = ,
                landmark_z31 = ,

                landmark_x32 = ,
                landmark_y32 = ,
                landmark_z32 = ,

                landmark_x33 = ,
                landmark_y33 = ,
                landmark_z33 = )
        return user_messages.streamReply(data)