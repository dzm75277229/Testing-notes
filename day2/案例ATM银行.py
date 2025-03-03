#定义全局变量
money=5000000
name=None
#对name赋值
name=input("请输入您的名字：")
#定义查询函数
def query():
    print("----------查询余额-------------")
    print(f"{name},您好，您的余额为：{money}")
#定义存款函数
def saving(num):
    global money#money在函数体内部定义为全局变量
    money+=num
    print("----------存款-------------")
    print(f"{name},您好，您存款{num}元成功")
    #定义query函数查
    query()
#定义取款函数
def get_money(num):
    global money
    money-=num
    print("----------取款-------------")
    print(f"{name},您好，您取款{num}元成功")
    query()
#定义主菜单函数
def main():
    print("----------主菜单-------------")
    print(f"{name},您好，欢迎来到银行，请选择操作")
    print(f"查询余额\t【输入1】")
    print(f"存款\t\t【输入2】")
    print(f"取款\t\t【输入3】")
    print(f"退出\t\t【输入4】")
    return input("请输入您的选择：")
    while True:
        key_input=main()
        if key_input==1:
            query(True)
            continue
        elif key_input==2:
            num=int(input("您想要存多少钱："))
            saving(num)
            continue
        elif key_input==3:
            num = int(input("您想要取多少钱："))
            get_money(num)
            continue
        else:
            print("程序退出")
            break
main()
