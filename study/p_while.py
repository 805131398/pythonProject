# 该实例演示了数字猜谜游戏
import random

var = random.randint(1, 100)
print("随机生成一个要猜的数:", var)
cai_1 = 0
cai_2 = 100
b = 1
while b:
    print("请输入您要猜的数值")
    try:
        cai = int(input())
        if (cai < cai_1) | (cai > cai_2):
            print("范围已经锁定在了", cai_1, "与", cai_2, "之间")
        else:
            if cai == var:
                b = 0
                print("恭喜您猜对了")
            elif cai < var:
                cai_1 = cai
            elif cai > var:
                cai_2 = cai
            if b != 0:
                print("该值大于", cai_1, "小于", cai_2)
    except ValueError:
        print("您输入的不是一个数字")

