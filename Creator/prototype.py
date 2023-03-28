# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : prototype.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/27/2023
# @Description: 原型模型: 相似的训练，在保留原始训练情况下，copy一个并作适当的迭代、学习率、优化方法等的微调
# @Upadate    : 
# @Software   : PyCharm

import copy
from collections import OrderedDict


class Train:
    def __init__(self, name, epoch, learn_rate, **rest):
        self.name = name
        self.epoch = epoch
        self.learn_rate = learn_rate
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
        mylist.append('\n')
        return ''.join(mylist)


class ProtoType:
    def __init__(self):
        self.train = dict()

    def regist(self, id, train):
        self.train[id] = train

    def unregist(self, id):
        del self.train[id]

    def clone(self, id, **attr):
        found = self.train.get(id)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(id))
        train = copy.deepcopy(found)
        train.__dict__.update(attr)
        return train


def main():
    t1 = Train('train-5000', 5000, 0.1)
    prototype = ProtoType()
    prototype.regist("01", t1)
    t2 = prototype.clone("01", name='train-10000', epoch=10000)
    for i in (t1, t2):
        print(i)


if __name__ == '__main__':
    main()
