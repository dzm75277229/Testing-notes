#字符串和元组一样不可修改
mystr="itheima and itcast"
value=mystr[1]
print(value)
#index()
index_=mystr.index('and')
print(f"在{mystr}中and的下标为{index_}")
#字符串替换：字符串。replace（字符串1，字符串2），将字符串中的字符串1全部替换为字符串2
mynewstr=mystr.replace('it','程序')
print(f"替换后的字符串为{mynewstr}")
#字符串分割：字符串.split(分隔符字符串),将字符串转为列表
my_str="hello python itheima itcast"
my_str_list=my_str.split(" ")
print(f"字符串{my_str}进行切割后为{my_str_list}")
#字符串.strip():不传入参数去除字符串中的空格，字符串.strip('特定字符')：用来去除字符串前后指定元素,
# 第一个字符是'1'，属于`chars`集合中的字符，会被移除。
#第二个字符是'2'，同样属于`chars`集合中的字符，会被移除。
#第三个字符是空格，不属于`chars`集合，停止移除。
my_str1="    i like python  "
new_my_str1=my_str1.strip()
print(f"字符串{my_str1}被strip后，结果为{new_my_str1}")
my_str1="12 34 12   i like python  21"
new_my_str1=my_str1.strip('12')
print(f"字符串{my_str1}被strip后，结果为{new_my_str1}")
#count()
count=my_str1.count('12')
print(f"{my_str1}中的'12'的个数为{count}")
#len()
length=len(my_str1)
print(length)