s = 'zhan'
print(s)
print(list(s))

setNew = {i ** 2 for i in (1, 2, 3)}
print(setNew)

a = {x for x in 'bcdedit' if x not in 'abc'}
print(a)

a = (x for x in range(1, 10))
print(a)  # 返回的是生成器对象

a = tuple(a)
print(a)
