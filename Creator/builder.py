# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : builder.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/27/2023
# @Description: 建造者模式  多种姿态估计方法推理及结果获取的管线
# @Upadate    : 
# @Software   : PyCharm
import cv2


# 创建实例类
class PoseEstimation:
    def __init__(self, name):
        self.name = name  # 算法名称
        self.in_img = None  # 输入图像
        self.skeleton = None  # 关键点坐标
        self.res_img = None  # 输出图像
        self.fps = None  # 推理帧率

    def __str__(self):
        info = ("Name: {}".format(self.name),
                "Skeleton: {}".format(self.skeleton),
                "Res Image: {}".format(self.res_img),
                "Fps: {}".format(self.fps))
        return '\n'.join(info)

    def get_skeleton(self):
        return self.skeleton

    def get_res_img(self):
        return self.res_img

    def get_fps(self):
        return self.fps


# 抽象建造者
class PoseEstimationBuilder:
    name = None

    def __init__(self):
        self.in_img = cv2.imread("test.jpg")
        self.estimation = PoseEstimation(self.name)

    def build_in_img(self):
        self.estimation.in_img = self.in_img


# 具体建造者
class OpenPose(PoseEstimationBuilder):
    name = 'OpenPose'

    def build_skeleton(self):
        self.estimation.skeleton = 'openpose skeleton'  # 这里简写，只做示例

    def build_res_img(self):
        self.estimation.res_img = 'openpose res img'

    def build_fps(self):
        self.estimation.fps = 'openpose fps'


class AlphaPose(PoseEstimationBuilder):
    name = 'AlphaPose'

    def build_skeleton(self):
        self.estimation.skeleton = 'AlphaPose skeleton'  # 这里简写，只做示例

    def build_res_img(self):
        self.estimation.res_img = 'AlphaPose res img'

    def build_fps(self):
        self.estimation.fps = 'AlphaPose fps'


# 指挥者
class InferPipeLine:
    def __init__(self):
        self.builder = None

    def pipeline(self, builder):
        self.builder = builder
        [step() for step in (self.builder.build_in_img,
                             self.builder.build_skeleton,
                             self.builder.build_res_img,
                             self.builder.build_fps)]

    @property
    def infer(self):
        return self.builder.estimation


def main():
    method = input("Choose a  Estimation method.(OpenPose, AlphaPose)")
    builder = eval(method)()
    pipeline = InferPipeLine()
    pipeline.pipeline(builder)
    estimation_res = pipeline.infer
    print(estimation_res)


if __name__ == "__main__":
    main()
