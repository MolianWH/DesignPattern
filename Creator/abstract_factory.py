# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : abstract_factory.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/27/2023
# @Description: 
# @Upadate    : 
# @Software   : PyCharm

from abc import abstractmethod, ABCMeta


# 1.抽象工厂类接口
class Method(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def turn_page(self):
        pass


# 2.具体工厂类接口
class Speech(Method):
    def open(self):
        return OpenWithSpeech()

    def close(self):
        return CloseWithSpeech()

    def turn_page(self):
        return TurnPageWithSpeech()


class HandPose(Method):
    def open(self):
        return OpenWithPose()

    def close(self):
        return CloseWithPose()

    def turn_page(self):
        return TurnPageWithPose()


# 3.抽象产品类接口
class Open(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class Close(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


class TurnPage(metaclass=ABCMeta):
    @abstractmethod
    def operation(self):
        pass


# 4.具体产品类接口
class OpenWithSpeech(Open):
    def operation(self):
        print(type(self).__name__, "has been run.")


class OpenWithPose(Open):
    def operation(self):
        print(type(self).__name__, "has been run.")


class CloseWithSpeech(Close):
    def operation(self):
        print(type(self).__name__, "has been run.")


class CloseWithPose(Close):
    def operation(self):
        print(type(self).__name__, "has been run.")


class TurnPageWithSpeech(TurnPage):
    def operation(self):
        print(type(self).__name__, "has been run.")


class TurnPageWithPose(TurnPage):
    def operation(self):
        print(type(self).__name__, "has been run.")


# 客户想要一个手势控制的PPT翻页互动算法
class Interaction:
    def __init__(self):
        pass

    def main(self, method, operation):
        self.method = eval(method)()
        if operation == "open":
            self.operation = self.method.open()
        elif operation == "close":
            self.operation = self.method.close()
        elif operation == "turn page":
            self.operation = self.method.turn_page()
        self.operation.operation()


if __name__ == "__main__":
    interaction = Interaction()
    interaction.main("HandPose", "turn page")
