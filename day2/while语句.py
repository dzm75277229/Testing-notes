#打印九九乘法表,加上end=' '自动不换行
print("hello",end='')
print("world")
#\t制表符
print("hello\tworld")
print("duzhimei\tgirl")
i=1
while i<=9:
    j=1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j+=1
    i+=1
    print() #进行换行