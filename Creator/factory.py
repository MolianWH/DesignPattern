# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : factory.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/27/2023
# @Description: 工厂模式：多种姿态估计数据集骨骼（不同关键点个数和形式）绘制
# @Upadate    : 
# @Software   : PyCharm

# abc是虚基类（abstract base class简写）
import abc


# 1.创建接口：定义骨骼基类（抽象产品类）
class Skeleton(metaclass=abc.ABCMeta):
    @abc.abstractmethod  # 装饰器：抽象方法
    def draw(self):
        '''
        抽象骨骼绘制方法
        '''
        pass


# 2.实现接口：不同姿态估计数据库关节点绘制（具体产品类）
class MSCOCO(Skeleton):
    def draw(self):  # 多态
        print("MSCOCO17个关键点")


class MediaPipe(Skeleton):
    def draw(self):  # 多态
        print("MediaPipe33个关键点")

class BODY25(Skeleton):
    def draw(self):  # 多态
        print("BODY_25的25个关键点")


# 3.创建骨骼绘制工厂
class SkeletonFactory(object):
    def get_skel(self, skel_type):
        return eval(skel_type)().draw()

# 4.使用
if __name__=='__main__':
    skel = SkeletonFactory()
    skel_type = input("Which Skeleton Model?(MSCOCO, MediaPipe, BODY25)")
    skel.get_skel(skel_type)
