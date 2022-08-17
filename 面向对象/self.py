# 洗衣机
class WashingMachine():
    def washing(self):  # self 调用改实例方法的对象
        print("self", self)

# 一个类可以创建多个对象，每个对象是不一样的
# 创建一个洗衣机对象（实例）
xiaoMi = WashingMachine()
xiaoMi1 = WashingMachine()
xiaoMi2 = WashingMachine()
xiaoMi3 = WashingMachine()
print("obj", xiaoMi)  # print("self", self)
xiaoMi.washing()  # 执行洗衣服的动作（实例方法）
print("obj", xiaoMi1)  # print("self", self)
xiaoMi1.washing()
print("obj", xiaoMi2)  # print("self", self)
xiaoMi2.washing()
print("obj", xiaoMi3)  # print("self", self)
xiaoMi3.washing()
