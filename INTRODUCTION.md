Udacity is using a new dataset production method that allows for quick processing and release cycles.
Instead of spending weeks (or months) waiting on 3D annotation data to be produced by third-party companies,
we have elected to try out something new that enables datasets to be released immediately after they are recorded.
While we do lose some sample distribution on each individual dataset due to the same obstacles being used for each session,
the massive speedup in production and reduction in cost allows us to release new datasets daily (and with different obstacles with each session).
In this manner,
we can directly control the type of data being recorded so that we can cover all situations without hoping for them to happen on real roads,
and we have extreme precision on obstacle location with differential RTK GPS technology.

Due to this new approach, there are some major differences from the Kitti datasets.
It is important to note that recorded positions are recorded with respect to the base station, not the capture vehicle.
The NED positions in the rtkfix topic are therefore in relation to a FIXED POINT, NOT THE CAPTURE OR OBSTACLE VEHICLES.
The relative positions can be calculated easily, as the NED frame is cartesian space, not polar. The XML tracklet files will,
however, be in the frame of the capture vehicle. This means that the capture vehicle is also included in the recorded positions,
and is denoted by the ROS topic ‘/gps/rtkfix’ in this first dataset.
The single obstacle vehicle in this dataset is located in the 'obs1/' topic namespace,
but this will be changed to '/obstacles/obstacle_name' in future releases to accomodate the creation of XML tracklet files for multiple obstacles.
Orientation of obstacles are not evaluated in Round 1, but will be evaluated in Round 2.
The pose section of the ROS bags included in this release IS NOT A VALID QUATERNION,
and does not represent either the pose of the capture vehicle or the obstacle.

As we are still working this new method of data collection, this first release has some important quirks to take note of while developing your solution.
There is no XML tracklet file included with these datasets. They will be released as soon as they are available,
in conjunction with the opening of the online leaderboard. Also, we have included the "Noisy" folder, which has partially useable data that we collected,
but most likely has unuseable position information. The camera, radar, and LIDAR data is still present, and may prove useful.
Additionally, this will be the only dataset with the '/velodyne_points' topic.
To save bandwidth,
future releases will only include the '/velodyne_packets' and the standard Velodyne ROS driver will need to be used to create the points data.

Good luck!

---------

Udacity使用了新方法采集数据，以便加速数据处理和释放的周期。
相比过去需要花几周甚至几个月时间等待第三方公司进行数据的3D标记，我们选择尝试了一些新的功能，使数据集在记录后能够立即被释放。
由于每个Session都使用相同的障碍物，我们在每个数据集中丢弃了一些样本，这样在实际运行时将极大的提高采集效率并降低成本，
使我们每天能都够发布新的数据集（并且每个Session都有不同的障碍物）。通过这种方式，我们可以直接控制实时记录的数据，在测试中覆盖更多的情况，
不必到在真正上路使用时候才发现问题，同时我们还可以使用差分RTK GPS技术在障碍物位置识别上获得极高的精度。

由于这种新方法，此数据集与Kitti数据集有一些主要的区别。其中最重要的是，记录的位置是相对于基站而不是捕获车辆的。
因此，在rtkfix主题中的NED位置与固定点相关，而不是拍摄车本身。因为NED记录使用的是笛卡尔坐标，而不是极坐标，障碍物与拍摄车的相对位置可以容易地计算出来。
然而，XML tracklet文件依然将使用基于拍摄车的位置记录。这意味着包括拍摄车本身的位置也会被记录，存放在ROS文件'/gps/rtkfix'主题的第一个数据集。
该数据集中的单个障碍物位于'obs1/'主题中，但是在将来的版本中将被更改为'/barriers/barriers_name'，以适应有多个障碍物情况的XML tracklet文件。
障碍物的行驶方向在第1轮不需要评估，但将在第2轮里需要进行评估。本版本中包含的ROS包的pose字段不是有效的四元数数据，并不表示拍摄车或障碍物的姿势。

由于这种新的数据收集方法仍然在研发中，因此在开发第一个版本解决方案时有一些需要特别注意的地方。
这些数据集还不包含XML tracklet文件，一旦这些文件可用，我们将在第一时间发布，同时还会发布在线的排行榜。
此外，我们还包括一个“Noisy”文件夹，其中有我们收集的部分可用数据，但很可能有不可靠的位置信息。包括相机、雷达和激光雷达数据，他们可能会有些帮助作用。
此外，这将是唯一直接提供'/velodyne_points'主题的数据集。为了节省空间，未来发布的版本都只会包含'/velodyne_packets'主题，
可以使用Velodyne激光雷达的标准ROS驱动程序来将其转换为真实的点阵数据。

祝好运！

---------

Dataset Information:

             [ 数据集 ]            [ 场景 ]
             approach_1.bag        直接驶向前方车辆
             approach_2.bag        从前方车辆的侧面经过
             approach_3.bag        快速掉头然后驶向前方车辆
             corner_pass.bag       在路口观察左右经过的车辆
             intersection_1.bag    车辆从前方很近的地方穿过
             sitting.bag           前方车辆静止不动
             spin_shoreline.bag    在空旷的地方疾驰
             spin.bag              观察前方左右疾驰的车辆
             NOISY_spin_2.bag      一边疯狂转向一边狂飙
             spin_3.bag            一边不停转向一边疾驰
             overtake.bag          对方车辆从后面超车
             5mph.bag              前方车辆时近时远

types:

             bond/Status                            [eacc84bf5d65b6777d4c50f463dfb9c8]
             diagnostic_msgs/DiagnosticArray        [60810da900de1dd6ddd437c3503511da]
             diagnostic_msgs/DiagnosticStatus       [d0ce08bc6e5ba34c7754f563a9cabaf1]
             dynamic_reconfigure/Config             [958f16a05573709014982821e6822580]
             dynamic_reconfigure/ConfigDescription  [757ce9d44ba8ddd801bb30bc456f946f]
             nav_msgs/Odometry                      [cd5e73d190d741a2f92e81eda573aca7]
             radar_driver/RadarTracks               [6a2de2f790cb8bb0e149d45d297462f8]
             rosgraph_msgs/Log                      [acffd30cd6b6de30f120938c17c593fb]
             sensor_msgs/Image                      [060021388200f6f0f447d0fcd9c64743]
             sensor_msgs/NavSatFix                  [2d3a8cd499b9b4a0249fb98fd05cfa48]
             sensor_msgs/PointCloud2                [1158d486dd51d683ce2f1be655c3c181]
             sensor_msgs/Range                      [c005c34273dc426c67a020a87bc24148]
             sensor_msgs/TimeReference              [fded64a0265108ba86c3d38fb11c0c16]
             tf2_msgs/TFMessage                     [94810edda583a504dfda3829e70d7eec]
             velodyne_msgs/VelodyneScan             [50804fc9533a0e579e6322c04ae70566]

topics:

             /cloud_nodelet/parameter_descriptions  : dynamic_reconfigure/ConfigDescription
             /cloud_nodelet/parameter_updates       : dynamic_reconfigure/Config
             /diagnostics                           : diagnostic_msgs/DiagnosticArray       (3 connections)
             /diagnostics_agg                       : diagnostic_msgs/DiagnosticArray       (2 connections)
             /diagnostics_toplevel_state            : diagnostic_msgs/DiagnosticStatus      (2 connections)
             /gps/fix                               : sensor_msgs/NavSatFix
             /gps/rtkfix                            : nav_msgs/Odometry
             /gps/time                              : sensor_msgs/TimeReference
             /image_raw                             : sensor_msgs/Image
             /obs1/gps/fix                          : sensor_msgs/NavSatFix
             /obs1/gps/rtkfix                       : nav_msgs/Odometry
             /obs1/gps/time                         : sensor_msgs/TimeReference
             /radar/points                          : sensor_msgs/PointCloud2
             /radar/range                           : sensor_msgs/Range
             /radar/tracks                          : radar_driver/RadarTracks
             /rosout                                : rosgraph_msgs/Log                     (7 connections)
             /tf                                    : tf2_msgs/TFMessage
             /velodyne_nodelet_manager/bond         : bond/Status                           (3 connections)
             /velodyne_packets                      : velodyne_msgs/VelodyneScan
             /velodyne_points                       : sensor_msgs/PointCloud2

