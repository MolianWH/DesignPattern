# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : iterator.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 迭代器。对数据的正序和逆序访问
# @Upadate    : 
# @Software   : PyCharm

"""Iterator Pattern with Python Code
"""

from abc import abstractmethod, ABCMeta

# 迭代器抽象类
class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def First(self):
        pass

    @abstractmethod
    def Next(self):
        pass

    @abstractmethod
    def Isdone(self):
        pass

    @abstractmethod
    def CurrItem(self):
        pass


# 聚集抽象类
class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def CreateIterator(self):
        pass


# 具体迭代器类
class ConcreteIterator(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = 0

    def First(self):
        return self.aggregate[0]

    def Next(self):
        ret = None
        self.curr += 1
        if self.curr < len(self.aggregate):
            ret = self.aggregate[self.curr]
        return ret

    def Isdone(self):
        return True if self.curr+1 >= len(self.aggregate) else False

    def CurrItem(self):
        return self.aggregate[self.curr]


# 具体聚集类
class ConcreteAggregate(Aggregate):
    def __init__(self):
        self.ilist = []

    def CreateIterator(self):
        return ConcreteIterator(self)


class ConcreteIteratorDesc(Iterator):
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = len(aggregate)-1

    def First(self):
        return self.aggregate[-1]

    def Next(self):
        ret = None
        self.curr -= 1
        if self.curr >= 0:
            ret = self.aggregate[self.curr]
        return ret

    def Isdone(self):
        return True if self.curr-1<0 else False

    def CurrItem(self):
        return self.aggregate[self.curr]


class Client(object):
    def main(self):
        ca = ConcreteAggregate()
        ca.ilist.append("1")
        ca.ilist.append("2")
        ca.ilist.append("3")
        ca.ilist.append("4")

        itor = ConcreteIterator(ca.ilist)
        print(itor.First())
        while not itor.Isdone():
            print(itor.Next())
        print("倒序:")
        itordesc = ConcreteIteratorDesc(ca.ilist)
        print(itordesc.First())
        while not itordesc.Isdone():
            print(itordesc.Next())


if __name__=="__main__":
    Client().main()
