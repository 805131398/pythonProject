num = int(input("输入一个数字"))
if num % 2 == 0:
    if num % 3 == 0:
        print("2  3")
    else:
        print("2 no 3")
else:
    if num % 3 == 0:
        print("3 no 2")
    else:
        print("no 3 no 2")

