nummin = input("请输入区间最小值：")
nummax = input("请输入区间最大值：")
client1 = range(int(nummin), int(nummax)+1)
for i in client1:
    if i % 2 == 0 and i % 3 == 0:
        print("BeebeebeeMoomoomoo")
    elif i % 2 == 0:
        print("Beebeebee")
    elif i % 3 == 0:
        print("Moomoomoo")
    else:
        print(i)
