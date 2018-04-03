#!usr/bin/python
# _*_ coding : UTF-8 _*_
# @author : csl
# @date   : 2018/02/27 22:58
'''
模拟注册登录作业：1、把账号和密码写入到一个文件（注册）；2、用户输入账号密码，写一个脚本自动查看文件中现有的账号和密码，
如果有对应的账号密码，允许登录成功
'''
import os,sys

urlpath = os.path.abspath(".")  #获取当前工作路径
usr_file = urlpath + "/usr_data.txt"

def study_register(rname,rpassword):
    #注册方法
    with open(usr_file,"a+") as file:
        file.write(rname + "," + rpassword + "\n")

def study_login(lname,lpassword):
    #登录方法
    with open(usr_file,"r") as file:
        user_data = file.readlines()  #读取出登录文件中的用户数据
    user_input = lname + "," + lpassword + "\n"
    for data in user_data:
        if data == user_input:
            print("***********")
            print("登录成功")
            print("%s 欢迎您！" % lname)
        else:
            print("登录中，请稍后。。。")

#  用户注册
print("***************")
print("请输入您要注册的用户名：")
rname = input()
print("您输入的注册用户名为：%s" %rname)
print("请输入您要设置的密码：")
rpassword = input()
print("您设置的密码为：%s" %rpassword)
print("确认提交请按Y;放弃请按N")
inr = input()
if inr == "Y":
    with open(usr_file, "r") as file:
        user_data_exist = file.readlines()  # 读取文件对比是否已经存在该用户名
        for data_exist in user_data_exist:
            name_exist = data_exist.split(",", 1)
            if rname == name_exist[0]:
                print("%s用户名已经存在" % rname)
                quit(0)
            else:
                print("注册中，请稍后。。。")
    study_register(rname, rpassword)
    print("恭喜您注册账号成功成功！")
    print("如果立即登录请按A；退出请按Q")
    inl = input()
    if inl == "A":
        study_login(rname,rpassword)
    elif inl == "Q":
        print("您已退出程序！！！")
        quit(0)  #正常退出程序
    else:
        print("您的输入不符合要求，程序已经退出，欢迎下次使用！")
        quit(1)  # 异常退出程序
elif inr == "N":
    print("您已放弃注册！程序退出！")
else:
    print("您已退出程序！！！")
    quit(1)  # 异常退出程序
