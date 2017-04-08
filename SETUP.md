# 运行环境准备

## ROS工具文档

参考`http://wiki.ros.org/kinetic/Installation/Ubuntu`

## 添加ROS的apt仓库

```
# sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
# apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
# apt update
```

## 安装ROS工具

>> For Python 2 Only

```
# apt install -y ros-kinetic-ros-base ros-kinetic-cv-bridge
# rosdep init
# rosdep update
# echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
# source /opt/ros/kinetic/setup.bash
```

## 验证安装

```
# python -c 'import rospy'
# python -c 'import rosbag'
```
没有提示找不到Module则安装正确
