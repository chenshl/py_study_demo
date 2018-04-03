# print("Hello World!!")
# print("python我来了！！！")

# name = input(print("请输入您的名字："))
# print("Hello:" + name)

# num1 = int(input(print("请输入第一个数：")))
# num2 = int(input(print("请输入第二个数：")))
# result = num1 + num2
# print("两个数之和为:" + str(result))        #两种写法拼接都可以
# print("两个数之和为：%d" % (result + 100))

# num3 = int(input("请输入一个数字："))
# if num3 > 0:
#     if num3 % 2 == 0:
#         print("%s 是偶数" % (num3))
#     else:
#         print("%s 是奇数" % (num3))
# else:
#     print("你是火星来得么？请正确输入。。。")

# 编写一个提示输入三个数字，注重之间用空格隔开，然后打印出输入的数字中最大的
string1 = input("请输入n个数字，数字之间用空格隔开：")
split1 = string1.split(" ", string1.count(" "))   # 用分割符对输入的字符串截取分割符出现的次数个分字符串
print(split1)
# num1 = int(split1[0])
# num2 = int(split1[1])
# num3 = int(split1[2])
# if num1 > num2 and num1 > num3:
#     print("您输入的最大的数字是：%s" % (num1))
# elif num2 > num1 and num2 > num3:
#     print("您输入的最大的数字是：%s" % (num2))
# else:
#     print("您输入的最大的数字是：%s" % (num3))
split2 = []
for i in split1:
    split2.append(int(i))
print(split2)
print(max(split2))
