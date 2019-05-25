#!/usr/bin/env python
# -*- coding: utf-8 -*-

def skipIf(status, expectstatus):
    def wrapper(func):

        def inner_wrapper(*args, **kwargs):
            print(status, "333333333333")
            print(expectstatus, "444444444444444444444")
            if status.find(expectstatus) != -1:
                return func(*args, **kwargs)
            else:
                print("状态不是 {}".format(expectstatus))
                return 
        return inner_wrapper
    return wrapper

        
