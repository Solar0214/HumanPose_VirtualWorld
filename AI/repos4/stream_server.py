#############################################GRPC

from concurrent import futures
import time

import grpc

import virtual_pb2 as user_messages
import virtual_pb2_grpc as users_service

class data_Streaming(users_service.data_streamServicer):
    def streaming(self, request, context):
        global data_x
        global data_y
        global data_z
        data = user_messages.data
            (landmark_x1 = ,
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