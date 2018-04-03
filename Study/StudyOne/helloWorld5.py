# 打印等腰三角形/宝塔，用空格和*号做输出填充
# 使用一个for循环直接打印
hight = int(input("请输入塔高："))
num1 = -1
# for i in range(0, hight):
#     num1 += 2
#     hight -= 1
#     print((" " * hight ) + ("*" * num1))

# 使用多个for循环打印
for i in range(0, hight):
    num1 += 2
    hight -= 1
    for h in range(0, hight):
        print(" ", end="")
    for n in range(0, num1):
        print("*", end="")
    print("")