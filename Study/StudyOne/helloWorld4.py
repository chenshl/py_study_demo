def add(num1, num2):
    print("%s + %s = %s" % (num1, num2, num1+num2))

def minus(num1, num2):
    print("%s - %s = %s" % (num1, num2, num1-num2))

def multiply(num1, num2):
    print("%s * %s = %s" % (num1, num2, num1*num2))

def divide(num1, num2):
    print("%s / %s = %s" % (num1, num2, num1/num2))
print("选择运算：\n"
      "1 is +\n"
      "2 is -\n"
      "3 is *\n"
      "4 is /")
choice = input("输入你的选择：")
if choice == "1":
    num1 = int(input("输入第一个数："))
    num2 = int(input("输入第二个数："))
    add(num1, num2)
elif choice == "2":
    num1 = int(input("输入第一个数："))
    num2 = int(input("输入第二个数："))
    minus(num1, num2)
elif choice == "3":
    num1 = int(input("输入第一个数："))
    num2 = int(input("输入第二个数："))
    multiply(num1, num2)
elif choice == "4":
    num1 = int(input("输入第一个数："))
    num2 = int(input("输入第二个数："))
    divide(num1, num2)
else:
    print("这不是一个合法的运算符！！！")