#for 临时变量 in 待处理数据集
name='duzhimei'
for x in name:
    print(f"{x}",end='')
str='itheima is a brand of itcast'
count=0
for i in str:
    if i=='a':
        count+=1
print(f"a字符串有{count}")