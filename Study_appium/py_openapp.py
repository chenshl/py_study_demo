#!/usr/bin/python
# coding:utf-8
# @author ://csl
# @date   : 2018/04/22 10:27
# appium打开apk安装包

from appium import webdriver
import time

desired_caps = {
                'platformName': 'Android',
                'deviceName': 'hol_t00',
                'platformVersion': '4.2.2',
                'appPackage': 'com.android.jinvovocni',
                'appActivity': 'com.android.jinvovocni.ui.login.WelcomeActivity',
                'unicodeKeyboard': 'True',
                'resetKeyboard': 'True'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(10)
