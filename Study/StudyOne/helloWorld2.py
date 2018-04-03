# 提示输入的三个数以空格隔开，并判断最大的数
string1 = input("请输入三个数字，数字之间用空格隔开：")
client1 = string1.split(" ", string1.count(" "))
print(client1)
if int(client1[0]) > int(client1[1]) and int(client1[0]) > int(client1[2]):
    print("您输入的最大数字为：%s" % (client1[0]))
elif int(client1[1]) > int(client1[0]) and int(client1[1]) > int(client1[2]):
    print("您输入的最大数字为：%s" % (client1[1]))
else:
    print("您输入的最大数字为：%s" % (client1[2]))

# 假如输入的数字超过3个或者个数不随机(可以将字符串列表转化为int数字列表)
client2 = []
for i in client1:
    client2.append(int(i))
print(client2)
print(max(client2))