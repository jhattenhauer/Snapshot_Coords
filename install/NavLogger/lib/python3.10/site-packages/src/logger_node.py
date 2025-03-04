import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from mavros_msgs.msg import State
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
import csv


file =  open('/home/james/Documents/dev/Snapshot_Coords/landmarks.csv', 'a', newline='')

class logger(Node):
    def __init__(self):
        super().__init__('logger')

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.subscription = self.create_subscription(
            NavSatFix,
            '/mavros/global_position/global',
            self.listener_callback,
            qos_profile  # Apply the QoS setting here
        )

    def listener_callback(self, global_msg):   
        input("Hit Enter to Capture Point")
        try:        
            message = [round(global_msg.latitude, 6), round(global_msg.longitude, 6)]            
            writer = csv.writer(file)
            writer.writerow(message)
            print(message)
        except:
            print("An Error Occured")

def main(args=None):
    rclpy.init(args=args)
    node = logger()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

