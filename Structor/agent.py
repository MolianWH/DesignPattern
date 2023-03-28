# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : agent.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/27/2023
# @Description: 代理模式：代理负责检查用户是否注册成功，有注册码且注册成功可继续访问算法，否则拒绝访问。
# @Upadate    : 
# @Software   : PyCharm

# 用户，进行注册，访问
class Client:
    def __init__(self):
        self.status = False

    def get_code(self):
        self.reg_code = "01"
        self.status = True

    def get_status(self):  # 可以判断是否获取注册码，是否过期
        return self.status

    def visit(self):
        print("Successful.")

    def refuse(self):
        print("Failed. Please get register code fist.")


class Agent:
    def __init__(self):
        pass

    def work(self):
        self.client = Client()
        if self.client.get_status():
            self.client.visit()
        else:
            self.client.refuse()
            self.client.get_code()
