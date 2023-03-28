# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : mediator.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 中介模式：有两个类A和B，类中各有一个数字，并且要保证类B中的数字永远是类A中数字的100倍。
#               当修改类A的数时，将这个数字乘以100赋给类B，而修改类B时，要将数除以100赋给类A。
#               类A类B互相影响，称为同事类
# @Upadate    : 
# @Software   : PyCharm

"""Mediator Pattern with Python Code
"""

from abc import abstractmethod, ABCMeta


class AbstractColleague(metaclass=ABCMeta):
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def updateNumber(self, number):
        self.number = number

    @abstractmethod
    # am 为一个中介者
    def setNumber(self, am, number):
        pass


class ColleagueA(AbstractColleague):
    def setNumber(self, am, number):
        self.number = number
        am.AaffectB()


class ColleagueB(AbstractColleague):
    def setNumber(self, am, number):
        self.number = number
        am.AaffectA()


class AbstractMediator(metaclass=ABCMeta):
    def __init__(self, a: AbstractColleague, b: AbstractColleague):
        self.A = a
        self.B = b

    @abstractmethod
    def AaffectA(self):
        pass

    @abstractmethod
    def AaffectB(self):
        pass


class Mediator(AbstractMediator):
    def __init__(self, a: AbstractColleague, b: AbstractColleague):
        AbstractMediator.__init__(self, a, b)

    # 处理A对B的影响
    def AaffectB(self):
        number = self.A.getNumber()
        self.B.updateNumber(number * 100)

    # 处理B对A的影响
    def AaffectA(self):
        number = self.B.getNumber()
        self.A.updateNumber(number / 100)


class Client(object):
    def main(self):
        collA = ColleagueA(0)
        collB = ColleagueB(0)

        am = Mediator(collA, collB)

        print("==========通过设置A影响B==========")
        collA.setNumber(am, 1000)
        print("collA的number值为：%d" % collA.getNumber())
        print("collB的number值为A的10倍：%d" % collB.getNumber())

        print("==========通过设置B影响A==========")
        collB.setNumber(am, 1000)
        print("collB的number值为：%d" % collB.getNumber())
        print("collA的number值为B的0.1倍：%d" % collA.getNumber())


if __name__ == "__main__":
    Client().main()
