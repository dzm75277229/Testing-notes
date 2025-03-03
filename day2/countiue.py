#continue和break
'''
for i in range(1,6):
    if i==3:
        continue
    print(i)
    i+=1
'''

money=10000
for i in range(1,21):
    import random
    jixiao=random.randint(1,10)
    if i<5:
        print(f"员工{i},绩效{jixiao},低于5，不发工资，下一个")
        continue
    else:
        money-=1000
        if money>=0:
            print(f"向员工{i}发放工资1000元，账户余额为{money}")
        else:
            print("工资放完了，下个月再领取")
            break


