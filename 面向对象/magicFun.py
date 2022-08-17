# 魔法方法
class Washer():
    def __init__(self):
        self.height = 800
        self.width = 500
        self.color = 'red'

    def info(self):
        print(f'宽：{self.width}, 高:{self.height},颜色: {self.color}')


w = Washer()
w.info()


# 带参数的init
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self):
        print(f'改对象的名称是:{self.name},年龄是:{self.age}')

    def __str__(self):  # __str__ 类似于java 的 toString 可自定义
        return f'改对象的名称是:{self.name},年龄是:{self.age} \n'

    def __del__(self):  # 删除这个对象的时候会被自动调用 del 方法
        print(f'{self} 对象被删除拉')


p = Person('小红', 18)
print(p)
