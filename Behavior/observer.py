# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : observer.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 观察者模式：数据格式化程序。默认格式化程序是以十进制格式展示一个数值。
#              这个例子中将添加一个十六进制格式化程序和一个二进制格式化程序。
#              每次更新默认格式化程序的值时，已注册的格式化程序就会收到通知，并采取行动
# @Upadate    :
# @Software   : PyCharm

class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name,
                                               self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name, hex(publisher.data)))


class BinaryFormatter:
    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,
                                                      publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)
    print()
    hf = HexFormatter()

    df.add(hf)
    df.data = 3
    print(df)
    print()

    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)
    print()

    df.remove(hf)
    df.data = 40
    print(df)
    print()

    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)
    print()

    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()
