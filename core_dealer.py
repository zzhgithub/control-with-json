# -*- coding:utf-8 -*-
import json

# Note:The call core is to controller hardware
# like XiaoMi .Then should define a struct for
# what to do.following just write to file
def dealer(**kwargs):
    print("here is in dealer!")
    f = open("test", "a+")
    f.write(str(kwargs) + "\n")
    f.close()
    # 这里对接硬件接口