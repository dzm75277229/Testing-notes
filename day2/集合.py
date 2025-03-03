#集合不支持元素重复且无序,集合用大括号{}定义
set1={'黑马程序员','我是'}
#定义空集合,定义空的字典不可以用大括号，大括号用来表示空字典
my_set=set()
print(set1)
#集合无序所以集合不是序列
#添加新元素
my_set.add("duzhimei")
my_set.add("duzhimei")
print(my_set)
#移除元素remove(),pop()
my_set.remove('duzhimei')
print(my_set)
set1={'黑马程序员','我是'}
elem=set1.pop()
print(elem)
#清空
set1.clear()
print(set1)
#去差集，集合一有的但是集合二没有,集合一和集合二不变
set1={1,3,4}
set2={1,2,6}
set3=set1.difference(set2)
print(set3)
print(set1)
print(set2)
#集合一.difference_update(集合二），集合一变化
set1={1,3,4}
set2={1,2,6}
set1.difference_update(set2)
print(set1)
print(set2)
#集合合并,集合一.union(集合二），得到新集合
set1={1,3,4}
set2={1,2,6}
set3=set1.union(set2)
print(set1)
print(set2)
print(set3)
#统计集合个数
set1={1,2}
num=len(set1)
print(num)
#对集合变量只能用for
for elem in set1:
    print(f"集合中的元素{elem}")
#去重复
my_list={'黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best'}
my_set=set()
for elem in my_list:
    my_set.add(elem)
print(my_set)