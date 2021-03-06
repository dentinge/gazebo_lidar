<?xml version="1.0"?>

<robot name="mira">

    <link name="base_link">
        <visual>
        <origin rpy="0 0 0" xyz="0 0 0"/>
        <geometry>
            <cylinder radius="0.06" length="0.09"/>
        </geometry>
        </visual>
    </link>
  
    <link name="roll_M1_link">
        <visual>
            <origin rpy="0 0 0" xyz="0 0 0"/>
            <geometry>
                <cylinder radius="0.06" length="0.09"/>
            </geometry>
        </visual>
    </link>
    
    <joint name="roll_joint" type="revolute">
        <parent link="base_link"/>
        <child link="roll_M1_link"/>
        <origin xyz="0.0023 0 -0.0005" rpy="0 0 0"/>
        <limit lower="-0.2" upper="0.2" effort="0.1" velocity="0.005"/>
        <axis xyz="1 0 0"/>
    </joint>
    

    <joint name="laser_joint" type="fixed">
        <origin xyz="0.1 0 0.2" rpy="0 0 0" />     
        <parent link="base_link"/>
        <child link="laser"/>
    </joint>
    
    <link name="laser_link">
    </link>
    

    <gazebo reference="laser_link">
    <sensor type="gpu_ray" name="head_hokuyo_sensor">
      <pose>0 0 0 0 0 0</pose>
      <visualize>false</visualize>
      <update_rate>40</update_rate>
      <ray>
        <scan>
          <horizontal>
            <samples>720</samples>
            <resolution>1</resolution>
            <min_angle>-1.570796</min_angle>
            <max_angle>1.570796</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.10</min>
          <max>30.0</max>
          <resolution>0.01</resolution>
        </range>
        <noise>
          <type>gaussian</type>
          <!-- Noise parameters based on published spec for Hokuyo laser
               achieving "+-30mm" accuracy at range < 10m.  A mean of 0.0m and
               stddev of 0.01m will put 99.7% of samples within 0.03m of the true
               reading. -->
          <mean>0.0</mean>
          <stddev>0.01</stddev>
        </noise>
      </ray>
      <plugin name="gazebo_ros_head_hokuyo_controller" filename="libgazebo_ros_gpu_laser.so">
        <topicName>/rrbot/laser/scan</topicName>
        <frameName>hokuyo_link</frameName>
      </plugin>
    </sensor>
  </gazebo>
     
  
</robot>
