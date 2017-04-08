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
        byte = [elem.encode("hex") for elem in msg.data]  # string to byte array
        raw_data = [int(n, 16) for n in byte]      # byte array to int array
        reshape_raw_data = np.reshape(raw_data, (512, 1400)).astype('uint8')  # reshape to 2-dim array
        im = Image.fromarray(reshape_raw_data)     # monochromatic image
        im_rgb = Image.merge('RGB', (im, im, im))  # color image
        im_rgb.save('%s/%s.png' % (out_dir, i))    # save image
        i += 1
        print('Extracted %s images' % i)
        if i >= 20:
            break
rbag.close()
