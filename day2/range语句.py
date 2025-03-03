#range(5)：[0,1,2,3,4]
#range(5,10):[5,6,7,8,9]
#range(5,10,2):[5,7,9],range序列配合for语句使用
range(10)
for x in range(10):
    print(x)
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()#换行,还可以通过\n来实现