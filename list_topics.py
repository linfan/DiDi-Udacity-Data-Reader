#!/usr/bin/env python

import rosbag
import os

path = '/data/ai02/didi/'

files = os.listdir(path)
for f in files:
    if f.endswith('.bag'):
        file = os.path.join(path, f)
        print('[ %s ]' % f)
        topicMap = {}
        bag = rosbag.Bag(file)
        totalTopics = 0
        for topic, _, _ in bag.read_messages():
            if topic not in topicMap:
                topicMap[topic] = 1
            else:
                topicMap[topic] += 1
            totalTopics += 1
        bag.close()
        topics = topicMap.keys()
        topics.sort()
        for topic in topics:
            print('  %s => %d' % (topic, topicMap[topic]))
        print('Total: %d\n' % totalTopics)
