#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
from mmaction.apis import init_recognizer, inference_recognizer

config_file = 'configs/recognition/tsn/tsn_r50_video_inference_1x1x3_100e_kinetics400_rgb.py'
device = 'cuda:0' # or 'cpu'
device = torch.device(device)

model = init_recognizer(config_file, device=device)
# inference the demo video
inference_recognizer(model, 'demo/demo.mp4')


# In[ ]:


"""
이것은 공식 문서에서 설치 완료후 정상적으로 설치가 되었는지 확인하는 코드

정상작동  - 주피터에서는 정상작동 - 파이참 같은 환경인데 왜지?


"""

