#内置函数len(),input(),int(),float(),type(),str(),range(),
str="duzhimei"
length=len(str)
print(length)
count=0
for i in str:
    count+=1
print(f"字符串{str}的长度为{count}")
'''
函数定义def 函数名（参数）:
    函数体
    return 返回值
'''
#a与b为形参，1和2为实参
def sum(a,b):
    #print(a+b)
    #print("欢迎来到python世界\n我爱你")
    return a+b
a=sum(1,2)
print(a)
#函数返回类型为none
def hello():
    print("hello")
b=hello()
print(f"无返回值的函数，返回的内容为{b},返回类型为{type(b)}")
def check_age(age):
    if age>18:
        return "sucess"
    else:
        return None
result=check_age(16)
#None表示0可以用做逻辑判断里面,not None表示1
if not result:
    print("未成年")