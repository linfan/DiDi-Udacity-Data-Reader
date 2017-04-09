#!/usr/bin/env python

import rosbag
import os
from PIL import Image

path = '/data/ai02/didi/'
skip_cycle = 20
height = 512

files = os.listdir(path)
for f in files:
    if f.endswith('.bag'):
        print('[ %s ]' % f)
        file = os.path.join(path, f)
        bag = rosbag.Bag(file)
        out_dir = f.replace('.bag', '_out')
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        i = 0
        for topic, msg, time in bag.read_messages():
            if topic == '/image_raw':
                width = len(msg.data) / height
                if i == 0:
                    print('Image data size: %s x %s = %s' % (width, height, len(msg.data)))
                if i % skip_cycle == 0:
                    im = Image.frombytes('L', (width, height), msg.data)  # Extract image
                    im.save('%s/%s.png' % (out_dir, (i / skip_cycle)))    # Save to file
                    print('Extracted %s images' % (i / skip_cycle))
                i += 1
        bag.close()
