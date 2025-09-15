#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
arduinoData =serial.Serial('/dev/ttyUSB0',9600)

class SerialNode(Node):
    def __init__(self):
        super().__init__("led_node_ros")

        #Initialize serial communication with Arduino

        #Create subscriber for motor control commands
        self.subscription=self.create_subscription(
            String,
            'led_Control',
            self.command_callback,
            10
        )

        self.get_logger().info("Serial node initialized")

        while True:
            mycmd=input('please input your command:')
            mycmd=mycmd+'\r'
            arduinoData.write(mycmd.encode())

    def command_callback(self,msg):
        self.get_logger().info("sending command: %s" % msg.data)

def main(args=None):
    rclpy.init(args=args)
    serial_node=SerialNode()
    rclpy.spin(serial_node)
    serial_node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()