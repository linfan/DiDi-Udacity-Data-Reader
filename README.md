# DiDi-Udacity-Data-Reader
DiDi-Udacity Self-Driving Car Challenge 2017 Raw Data Reader

## 第一阶段数据：单一车辆障碍物
使用摄像头、Radar 和 LIDAR 数据来检测单一车辆障碍物。
- 数据集 [torrent](https://didi.udacity.com/data/76352487923a31d47a6029ddebf40d9265e770b5.torrent), [百度盘](https://pan.baidu.com/s/1dEJj7vr)
- 传感器校准文档 [torrent](https://didi.udacity.com/data/d9e413a9fbd07f668fd5370d53ee2691404ae32c.torrent), [百度盘](https://pan.baidu.com/s/1c2cOrWc)

## 文件说明
- `INTRODUCTION.md` 第一阶段的官方说明+简易翻译 
- `SETUP.md` 安装ROS依赖的步骤
- `list_topics.py` 列出每个ROS文件中各Topic数量
- `list_topics.out` 上一个脚本运行结果
- `read_msg.py` 从ROS文件读取Topic数据的测试
- `get_image_dimension.py` 检查图片维度和长宽的脚本
- `extract_image.py` 从ROS文件中提取摄像头图片数据
- `find_fields_with_data.py` 检查还有哪些Topic包含Data数据
