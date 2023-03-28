# -*- coding: utf-8 -*-
# @Copyright
# @FileName   : strategy.py
# @Author     : MJJ
# @Version    : 0.X.23XXXX
# @Date       : 3/28/2023
# @Description: 策略模式。同样是多种姿态估计算法，根据用户需求选择某一种算法。
#               这里展示的是书中例子。有两种算法可以判断输入串中是否包含相同字母。
# @Upadate    : 
# @Software   : PyCharm

import time

SLOW = 3  # 单位为秒
LIMIT = 5  # 字符数
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    '''
    对字符串进行排序并逐对比较所有字符。
    Args:
        s: 输入的串

    Returns: 不包含相同字符返回真，否则返回假

    '''
    if len(s) > LIMIT:
        print(WARNING)
    time.sleep(SLOW)
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    """
    使用集合快速实现，提高速度
    Args:
        s: 输入字符

    Returns: 不包含相同字符返回真，否则返回假

    """
    if len(s) < LIMIT:
        print(WARNING)
    time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    '''
    策略集合
    Args:
        s: 输入字符
        strategy: 策略对象。allUniqueSort或allUniqueSet

    Returns:

    '''
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')
            if word == 'quit':
                print('bye')
                return
            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair > ')
                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))
                    print()


if __name__ == '__main__':
    main()
