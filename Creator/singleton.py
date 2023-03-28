# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : singleton.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/27/2023
# @Description: 单例模式：可以有多个摄像头读取实例，但只能有一个摄像头管理实例。
# @Upadate    : 
# @Software   : PyCharm
from threading import Thread, Lock
from time import sleep


def synchronized(func):
    lock = Lock()

    def synchronized_func(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    return synchronized_func


def singleton(cls):
    instance = {}

    @synchronized
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class CameraManager:
    def __init__(self):
        sleep(1)


def target():
    manager = CameraManager()
    print(manager)


if __name__ == '__main__':
    threads = [Thread(target=target)for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()