# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : template.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 模板模式. DDAI中定义各个算法插件，在主程序中定义管线，注册和使用插件。
#               各个插件输入图像，输出结果和图片,输入输出一致。
#               pipeline先目标检测，在跟踪和姿态估计
# @Upadate    : 
# @Software   : PyCharm
class Detector:
    # 目标检测
    def __call__(self, *args, **kwargs):  # 这里以string代替输出结果
        in_data = args[0]
        res = "目标检测结果;"
        out_data = in_data + res
        return {'res': res, "out_img": out_data}


class Estimation:
    # 姿态估计
    def __call__(self, *args, **kwargs):  # 这里以string代替输出结果
        in_data = args[0]
        res = "姿态估计结果;"
        out_data = in_data + res
        return {'res': res, "out_img": out_data}


class Tracker:
    # 目标跟踪
    def __call__(self, *args, **kwargs):  # 这里以string代替输出结果
        in_data = args[0]
        res = "目标跟踪结果;"
        out_data = in_data + res
        return {'res': res, "out_img": out_data}


def pipeline():
    detector = Detector()
    estimation = Estimation()
    tracker = Tracker()
    in_data = ''
    for algo in [detector, tracker, estimation]:
        res, out_data = algo(in_data).values()
        print("res:", res, " out_img:", out_data)
        in_data = out_data


if __name__ == "__main__":
    pipeline()
