#!/usr/bin/env python

import rosbag

rbag = rosbag.Bag('/data/ai02/didi/approach_1.bag')

topics = []
for topic, msg, _ in rbag.read_messages():
    if topic not in topics:
        fields = [i for i in dir(msg) if not i.startswith('_')]
        print('[ %s ]' % topic)
        for f in fields:
            print('  %s' % f)
        print('')
        topics.append(topic)
rbag.close()

