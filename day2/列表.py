#定义空列表list1=[],list2=list()
list2=list()
#列表里面可以是列表，整型，字符串等
list1=['itheima','python','000',True,[1,2]]
print(type(list1))
print(list1)
#通过下标索引访问列表内的元素
print(list1[0])
#反向索引-1取得是倒数第一个元素
print(list1[-1])
#嵌套索引
list3=[[1,2,3],[4,5,6]]
print(list3[1][0])
#列表常用方法也叫类
'''
class Student:
    def sum(x,y):
        return x+y
student=Student()
num=student.sum(1,3)
print(num)
'''
#列表常用方法：列表.index(元素),若元素不存在就会报错
mylist=['itheima','duzhimei']
index=mylist.index('duzhimei')
print(f"duzhimei在mylist的小标为{index}")
#对列表特定位置进行赋值,不能对超出列表的长度进行赋值
mylist[1]='nihao'
print(mylist)
#对列表进行插入：列表.insert（下表，元素）
mylist.insert(1,'duzhimei')
print(mylist)
#对列表尾部进行追加：列表。append(下标，元素)
mylist.append(123)
print(mylist)
#对列表添加很多元素：列表.extend(其他数据容器)
mylist2=[1,2]
mylist.extend(mylist2)
print(mylist)
#元素删除：del 列表[下标]或者列表.pop(下标）,pop可以返回被删除的元素
del mylist[-1]
print(mylist)
elem=mylist.pop(-1)
print(f"通过pop删除的元素为{elem}")
print(mylist)
mylist.extend(mylist2)
print(mylist)
#删除列表第一个匹配的元素：列表.remove(元素）
mylist.remove(1)
print(mylist)
#列表清空：列表.clear()
'''
mylist.clear()
print(mylist)
'''
mylist.insert(1,2)
print(mylist)
#统计元素在列表中的数量：列表.count(元素）
num=mylist.count(2)
print(num)
length=len(mylist)
print(f"列表元素长度{length}")
#列表遍历while
def list_while():
    '''
    读取列表中的元素
    :return:
    '''
    global mylist
    index=0
    while index<length:
        elem=mylist[index]
        print(elem)
        index+=1
list_while()
#列表遍历for循环
def list_for():
    global mylist
    for elem in mylist:
        print(elem)
list_for()