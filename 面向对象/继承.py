class Father(object):
    def __init__(self):
        self.money = 1

    def info_print(self):
        print("Father")
        print(self.money)


class Mather(object):
    def __init__(self):
        self.money = 2

    def info_print(self):
        print("Mather")
        print(self.money)


# 多继承
class Son(Father, Mather):

    def __init__(self, money):
        super().__init__()
        self.money = money

    # 重写父类方法
    def info_print(self):
        print("Son")
        print(self.money)

    pass

    # 调用父类方法
    def father_info_print(self):
        Father.__init__(self)
        Father.info_print(self)

    # 调用妈类方法
    def mather_info_print(self):
        # Mather.__init__(self)
        Mather.info_print(self)


s = Son(100)


s.info_print()
s.father_info_print()
s.mather_info_print()


#  孙子
class GrandSon(Son):
    pass


gs = GrandSon(1)
gs.info_print()
gs.father_info_print()
gs.mather_info_print()
