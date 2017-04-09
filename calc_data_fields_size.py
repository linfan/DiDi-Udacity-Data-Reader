#!/usr/bin/env python

import rosbag

rbag = rosbag.Bag('/data/ai02/didi/approach_1.bag')

topicMap = {}
for topic, msg, time in rbag.read_messages():
    if hasattr(msg, 'data'):
        if topic not in topicMap:
            topicMap[topic] = msg.data
rbag.close()

for topic in topicMap.keys():
    print('%s => %s' % (topic, len(topicMap[topic])))

# /radar/points => 216
# /velodyne_points => 1264256
# /image_raw => 716800
