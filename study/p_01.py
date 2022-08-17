counter = 100
miles = 100.0
name = "asd"

print(counter)
print(miles)
print(name)

a = b = c = 1
aa, bb, cc = 1, 2, "run"
print(a)
print(b)
print(c)
print(aa)
print(bb)
print(cc)

print(type(a))
print(type(miles))
print(type(cc))

# 判断一个变量是不是一种父类类型
print(isinstance(a, int))


class A:
    a = 1


class B(A):
    b = 2


isA = isinstance(A(), A)

isB = isinstance(B(), A)

print(isA)
print(isB)
print("---------------------")
print(type(B()) == B)
print(type(A()) == B)
print(type(B()) == A)
print(type(B()))
print(A)

print("---------- String start ----------")
str = "zhanghao"
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个[下标第二个]开始到第五个字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次，也可以写成print(2 * str)
print(str + "TEST")  # 连接字符串
print("---------- String end ----------")

print("------- 转移字符 start ---------")
print(r"nihao\nma")
print("nihao\nma")
print("------- 转移字符 end ---------")

word = "Python"
print(word[0], word[5])
print(word[-1], word[-6])

print("----------列表-------------")
list = [1, 2, 3, 4, "wqe", A()]
tinyList = [123, 'tinyList']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list * 3)
print(list + tinyList)

print(tinyList)
print(list[1:4:2])
print("----------列表 end -------------")

print("元组")
tuple = ('abcd', 789, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple * 2)
print(tuple + tinytuple)

print("集合")
sites = {'Google', 'Taobao', 'Runoob', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set 可以进行集合运算
print('集合运算')
a = set('abcsdskdj')
b = set('ajsdijwi')

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 字典
print("Dictionary - 字典")
dict = {'one': "1 - 菜鸟", 2: "2 - 小鸟"}

tinydict = {'name': 'runoob', 'code': 1, 'site': 'baidu.com'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())


def reverseWords(input):
    # 通过空格将字符串分隔
    inputWords = input.split(" ")

    inputWords = inputWords[-1::-1]

    output = '  '.join(inputWords)

    return output


if __name__ == "__main__":
    input = "i love you"
    rw = reverseWords(input)
    print(rw)
