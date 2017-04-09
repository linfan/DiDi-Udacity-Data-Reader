#!/usr/bin/env python
# 后来发现在ROS数据里本来就包含图片宽度和高度，
# 根本不需要用OpenCV来转换，这个脚本是没必要的

import rosbag
import os
from cv_bridge import CvBridge

rbag = rosbag.Bag('/data/ai02/didi/approach_1.bag')
bridge = CvBridge()

out_dir = 'out'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for topic, msg, time in rbag.read_messages():
    if topic == '/image_raw':
        cv_array = bridge.imgmsg_to_cv2(msg)
        print(cv_array.shape)
        break
rbag.close()
