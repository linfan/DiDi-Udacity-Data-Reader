#!/usr/bin/env python

import rosbag
import numpy as np
from PIL import Image

rbag = rosbag.Bag('/data/ai02/didi/approach_1.bag')

for topic, msg, time in rbag.read_messages():
    if topic == '/image_raw':
        # Convert To nD-Array
        byte_array = [elem.encode("hex") for elem in msg.data]  # string to byte array
        int_array = [int(n, 16) for n in byte_array]            # byte array to int array
        uint_array_2d = np.reshape(int_array, (msg.height, msg.width)).astype('uint8')  # reshape to 2-dim array

        # Save To File
        im = Image.fromarray(uint_array_2d)                     # monochromatic image
        im_rgb = Image.merge('RGB', (im, im, im))               # color image
        im_rgb.save('out.png')                                  # save image

        break
rbag.close()
