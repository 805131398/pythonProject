# 烤地瓜
# 需求: 通过用户定义的瓜的制作方法,反馈瓜属性
# 制作方法:
#       1. 时间
#       2. 调料

class SweetPotato:
    statusList = ('生', '熟', '糊')

    def __init__(self, time):
        self.time = time
        self.seasoning = '原味'

    def status(self):  # 初始状态是生的地瓜
        if 0 < self.time <= 3:
            return self.statusList[0]
        elif 3 < self.time <= 7:
            return self.statusList[1]
        else:
            return self.statusList[2]

    def __str__(self):
        print(f'现在这个烤地瓜已经烤了{self.time}分钟,处于{self.status()}状态,口味是: {self.seasoning} ')


# 定义一个卖烤地瓜的商家
class Vendors:
    def __init__(self, name, ingredients):
        self.name = name
        self.mainBusiness = '烤地瓜'
        self.sweetPotatoes = {}  # 要烤制的地瓜的列表,也可以理解为订单
        self.ingredients = ingredients  # 这家店支持的口味

    def making(self, customer):
        print(f'''
        热烈欢迎 {customer.name} 到 {self.name} 的店消费!
        请输入要烤制的地瓜的时间(分钟,友情提示0-3分钟烤不熟,4-7分钟正好,8分钟以上直接烤糊了不能吃~):
                ''')
        time = int(input())  # 用户要烤制的时间
        sp = SweetPotato(time)
        print(f'开始制作商品[{self.mainBusiness}]')
        print("美食制作中~")
        print("DING , 可以选择口味啦~")
        choose = True  # 用于判断是否选择了正确的配料
        while choose:
            index = 1
            print(f'''请选择您的口味: ''')
            print('0. 原味')
            for i in self.ingredients:
                print(f'{index}.{i}')
                index = index + 1
            try:
                chooseVar = int(input())
                if chooseVar != 0:
                    sp.seasoning = self.ingredients[int(input()) - 1]
                choose = False
            except IndexError:
                print("没有这个口味嗷,请重新选择:")
        print(sp)

    def __str__(self):
        return f'商店名称是:{self.name},商店主营业务是:{self.mainBusiness}\r\n'


# 定义一个人
class Person:
    def __init__(self, name):
        self.name = name  # 姓名
        self.itemList = None  # 物品列表


# 小红开始买烤地瓜
xiaoHong = Person("小红")
# 商店列表
roastedSweetPotatoStandWang = Vendors("小王的地瓜摊", ['盐', '酱油', '糖', '醋'])
roastedSweetPotatoStandTai = Vendors("小台的地瓜摊", ['沙拉', '甜面酱', '黑胡椒', '奶油'])
roastedSweetPotatoStoreList = {1: {
    'name': roastedSweetPotatoStandWang.name,
    'store': roastedSweetPotatoStandWang
}, 2: {
    'name': roastedSweetPotatoStandTai.name,
    'store': roastedSweetPotatoStandTai
}}

# 创建可以做的事的列表
things = {1: {
    "name": "购买烤地瓜",
    "type": "storeList",  # 通过这个字段遍历
    "storeList": roastedSweetPotatoStoreList  # 地瓜摊的商户列表
}}
b = True
while b:
    print(f'请选择小红接下来要做什么事: \r\n')
    for number in things:
        print(number, ".", things[number]['name'])
    try:
        thingNumber = int(input())  # 用户输入序号判断要做什么事情
        thingsType = things[thingNumber]['type']  # 用户要做的事情的类型
        storeList = things[thingNumber][thingsType]  # 对应类型的商户的列表
        for storeNumber in storeList:
            storeName = storeList[storeNumber]['name']
            print(storeNumber, '.', storeName)
        storeNumber = int(input())  # 用户输入序号判断要去那家店消费
        store = storeList[storeNumber]['store']  # 获取商店对象
        store.making(xiaoHong)  # 执行制作方法
    except ValueError:
        print("您输入的不是一个序号即可")
    except KeyError:
        print("请输入范围内的数字")
