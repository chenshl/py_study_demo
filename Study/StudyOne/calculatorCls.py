from Study.StudyOne import myCalcultor as mc

print("请选择运算符：\n"
      "1 is +\n"
      "2 is -\n"
      "3 is *\n"
      "4 is /")
choisnumn = input("请输入选择的运算符：")
cls1 = mc.MyCalcultor()
if choisnumn == "1":
    no1 = int(input("请输入第一个数："))
    no2 = int(input("请输入第二个数："))
    print("%s + %s = $s" % (no1, no2, cls1.add(no1, no2)))
elif choisnumn == "2":
    no1 = int(input("请输入第一个数："))
    no2 = int(input("请输入第二个数："))
    print("%s - %s = %s" % (no1, no2, cls1.jianfa(no1, no2)))
elif choisnumn == "3":
    no1 = int(input("请输入第一个数："))
    no2 = int(input("请输入第二个数："))
    print("%s * %s = %s" % (no1, no2, cls1.chegfa(no1, no2)))
elif choisnumn == "4":
    no1 = int(input("请输入第一个数："))
    no2 = int(input("请输入第二个数："))
    print("%s / %s = %s" % (no1, no2,cls1.chufa(no1, no2)))
else:
    print("请选择正确的运算符！！！")

