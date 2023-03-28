# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : bridge.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 桥接模式：同样是手势语音互动，打开PPT采用语音方式识别，关闭PPT采用手势控制识别。
# @Upadate    : 
# @Software   : PyCharm
from abc import abstractmethod, ABCMeta


class Operation:
    def __init__(self, method):
        self.method = method

    def operate(self):
        pass


class OpOpenPPT(Operation):
    def operate(self):
        self.method.recognize()
        print("已检测到打开PPT")


class OpClosePPT(Operation):
    def operate(self):
        self.method.recognize()
        print("已检测到关闭PPT")


class Method(metaclass=ABCMeta):
    @abstractmethod
    def recognize(self):
        pass


class MSpeech(Method):
    def recognize(self):
        print("语音识别结果")


class MPose(Method):
    def recognize(self):
        print("手势识别结果")


def main():
    open = OpOpenPPT(MSpeech())
    close = OpClosePPT(MPose())
    open.operate()
    print("===================")
    close.operate()


if __name__ == "__main__":
    main()
