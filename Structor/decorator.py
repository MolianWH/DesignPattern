# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : decorator.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 装饰器模式，比如动态添加日志功能，发送数据前对数据转base64等等。
#               如下面是通信日志装饰器简单示例。这里展示了类装饰器怎么用。
# @Upadate    : 
# @Software   : PyCharm
import socket


class LogSocket:
    @staticmethod
    def log(func):
        def wrapper(*args):
            print("Visit Func %s" % func.__name__)
            return func(*args)

        return wrapper


@LogSocket.log
def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2401))
    server.listen(1)

    try:
        while True:
            client, addr = server.accept()
            respond(client)
    finally:
        server.close()
