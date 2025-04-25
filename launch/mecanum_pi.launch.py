import os
import launch
import yaml
from launch.conditions import IfCondition
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    controller_node_dir = os.path.join('mecanum/mecanum/')
    urg_node2_launch_path = os.path.join(get_package_share_directory('urg_node2'), 'launch')

    controller_node = Node(
        package = 'mecanum',
        executable = 'controller', 
        name = 'mecanum_controller',
        output = 'screen',
    )

    urg_node2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(urg_node2_launch_path, 'urg_node2.launch.py')),
        launch_arguments={
            }.items())
    
    return LaunchDescription([
        controller_node,
        urg_node2_launch

    ])


