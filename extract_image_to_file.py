#!/usr/bin/env python

import rosbag
import os
from PIL import Image

path = '/data/ai02/didi/'
skip_cycle = 20

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
                if i % skip_cycle == 0:
                    im = Image.frombytes('L', (msg.width, msg.height), msg.data)  # Extract image
                    im.save('%s/%s.png' % (out_dir, (i / skip_cycle)))  # Save to file
                    print('Extracted %s images' % (i / skip_cycle))
                i += 1
        bag.close()
