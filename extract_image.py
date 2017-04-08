#!/usr/bin/env python

import rosbag
import os
import numpy as np
from PIL import Image

rbag = rosbag.Bag('/data/ai02/didi/approach_1.bag')

out_dir = 'out'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

i = 0
for topic, msg, time in rbag.read_messages():
    if topic == '/image_raw':
        im = Image.frombytes('L', (1400, 512), msg.data)
        im.save('%s/%s.png' % (out_dir, i))
        i += 1
        print('Extracted %s images' % i)
        if i >= 10:
            break
rbag.close()
