#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import socket
import json

ego_host_name = socket.gethostname()
print("ego_host_name = %s" % ego_host_name)

def chatter_CB(msg):
    rospy.loginfo("<" + rospy.get_caller_id() + "> I heard: %s", msg.data)
    _msg_dict = json.loads(msg.data)
    print("----------------")
    print("hostname = %s" % _msg_dict["hostname"])
    print("data = %s" % _msg_dict["data"])
    print("----------------")
    print("")


def main():
    pub = rospy.Publisher('/chatter', String, queue_size=10)
    #
    rospy.init_node('cross_compulter_chatter', anonymous=False)
    # Subscribers
    rospy.Subscriber("/chatter", String, chatter_CB)
    #
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        #
        _msg_dict = dict()
        _msg_dict["hostname"] = ego_host_name
        _msg_dict["data"] = hello_str
        _json_str = json.dumps(_msg_dict)
        #
        print("===================")
        print("_json_str to send = \n%s" % _json_str)
        print("===================")
        print("")
        pub.publish(_json_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
