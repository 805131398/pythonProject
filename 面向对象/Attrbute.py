# 洗衣机属性添加
class WashingMachine():

    def __init__(self):
        self.width = None
        self.name = ''
        self.height = 0

    def washing(self):
        print("洗衣服")

    def info(self):
        print("name:" + self.name, "高度", self.height, "宽", self.width)
        print(f'宽：{self.width},高：{self.height}')


# 创建一个洗衣机对象（实例）
xiaoMi = WashingMachine()
print(xiaoMi)
xiaoMi.width = 500
xiaoMi.height = 800
# 执行洗衣服的动作（实例方法）
xiaoMi.info()
print(xiaoMi.width)
