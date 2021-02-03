import json


# Note:The call core is to controller hardware
# like XiaoMi .Then should define a struct for
# what to do.following just write to file
def dealer(**kwargs):
    f = open("test", "a+")
    f.write(json.dump(kwargs))
    f.close()
