#!/usr/bin/env python

import rosbag
import os

path = '/data/ai02/didi/'

files = os.listdir(path)
for f in files:
    if f.endswith('.bag'):
        file = os.path.join(path, f)
        print('[ %s ]' % f)
        topics = []
        bag = rosbag.Bag(file)
        for topic, _, _ in bag.read_messages():
            if topic not in topics:
                topics.append(topic)
                print('  %s' % topic)
        bag.close()
