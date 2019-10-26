# coding=utf8

# 本题目适合用于呈现计算思维不同于数学思维之处
# 算法题目：穷举法
# 知识点：列表、条件结构、while循环
# 难点：位置关系的数学公式表达

"""
Ex676 养鸟：（二年级奥数题）
爷爷退休了，终于有时间养鸟。
他把7个鸟笼分别编上1-7号，首尾连成一个环形，每只笼子养上一种鸟，
分别是：麻雀、鸽子、鹦鹉、喜鹊、乌鸦、黄鹂鸟、布谷鸟
已知：
（1）麻雀与鸽子相隔一个鸟笼
（2）鹦鹉的笼子号码比喜鹊的大
（3）乌鸦在麻雀和黄鹂鸟中间
（4）布谷鸟在1号笼，乌鸦在5号笼子
求解：每个笼子里分别装的什么鸟？
"""

import random


# return True if all conditions are met
def do_experiment(data):
    result = True
    # condition 4
    if data[4] != 5 or data[6] != 1:
        result = False
    # condition 1
    elif abs(data[0] - data[1]) not in [2, 5]:
        result = False
    # condition 2
    elif data[2] < data[3]:
        result = False
    # condition 3
    elif not (abs(data[0] - data[4]) in [1, 6] and
              abs(data[4] - data[5]) in [1, 6]):
        result = False

    return result


# if don't know whether a solution exists ...
def run_rounds(n):
    cage = list(range(1, 8))
    for _ in range(n):
        # let the values of cage be 1 to 7 in random orders
        random.shuffle(cage)
        if do_experiment(cage):
            print(cage)


# if sure of the existence of one solution at least ...
def main():
    result = False
    cage = list(range(1, 8))
    rounds = 0
    while not result:
        rounds += 1
        random.shuffle(cage)
        result = do_experiment(cage)
    print('After doing %i experiments, we came to the solution as:' % rounds)
    print(cage)


if __name__ == '__main__':
    main()
