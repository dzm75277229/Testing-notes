'''
age=10
if age>20:
    print("我成年了")
elif age>10:
    print("我没成年")
else:
    print("我是小孩")
num=1
if int(input("请输入一个数字："))==num:
    print("猜对了")
elif int(input("再猜一次："))==num:
    print(("恭喜猜对了"))
else:
    print("对不起，猜错了")
'''
#猜数字
import random
num=random.randint(1,10)
guess =int(input("猜一个整数："))
if guess==num:
    print("猜对了")
else:
    if guess>num:
        print("猜大了")
    else:
        print("猜小了")
guesstwo =int(input("再猜一个整数："))
if guesstwo==num:
    print("猜对了")
else:
    if guesstwo>num:
        print("猜大了")
    else:
        print("猜小了")

