# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : memento.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 备忘录模式：
#               我们在编程的时候，经常需要保存对象的中间状态，当需要的时候，可以恢复到这个状态。
#               比如，可以使用Ctrl+Z来进行撤销步骤。这时我们便可以使用备忘录模式来实现。
#
#               代码演示了一个单状态单备份的例子，逻辑非常简单：
#               Originator类中的state变量需要备份，以便在需要的时候恢复；
#               Memento类中，也有一个state变量，用来存储Originator类中state变量的临时状态；
#               而Caretaker类就是用来管理备忘录类的，用来向备忘录对象中写入状态或者取回状态。

# @Upadate    : 
# @Software   : PyCharm


"""Memento Pattern with Python Code
"""


class Memento(object):
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state


class Originator(object):
    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def createMemento(self):
        return Memento(self.state)

    def restoreMemento(self, memento: Memento):
        self.setState(memento.getState())


class Caretaker(object):
    def getMemento(self):
        return self.memento

    def setMemento(self, memento: Memento):
        self.memento = memento


class Client(object):
    def main(self):
        originator = Originator()
        originator.setState("状态1");
        print("初始状态:" + originator.getState())
        caretaker = Caretaker()
        caretaker.setMemento(originator.createMemento())
        originator.setState("状态2")
        print("改变后状态:" + originator.getState())
        originator.restoreMemento(caretaker.getMemento())
        print("恢复后状态:" + originator.getState())


if __name__ == "__main__":
    Client().main()
