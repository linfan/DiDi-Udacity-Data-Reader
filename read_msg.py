#!/usr/bin/env python

import rosbag

numbers = 32   # 32 topics each frame
rbag = rosbag.Bag('/data/ai02/didi/approach_1.bag')

for topic, msg, _ in rbag.read_messages():
    if numbers < 1:
        break
    numbers -= 1
    print('%s => %s' % (topic, msg.__str__()[:100]))
rbag.close()
