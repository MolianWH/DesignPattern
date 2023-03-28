# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : adapter.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 适配器模式：客户端仅知道如何调用execute()方法，并不知道如何调用Synthesizer和Human类的play() 和speak()。
#               在不改变类的前提下，我们该如何做才能让代码有效？
# @Upadate    : 
# @Software   : PyCharm

# 想要什么
class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


# 有什么
class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


# 适配器
class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))


if __name__ == "__main__":
    main()
