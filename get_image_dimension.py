#!/usr/bin/env python

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
