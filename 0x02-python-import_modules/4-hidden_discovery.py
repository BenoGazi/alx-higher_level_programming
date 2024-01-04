#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    _hid = dir()
    for i in range(0, len(_hid)):
        if _hid[i][:2] != "__":
            print("{:s}".format(_hid(i)))
