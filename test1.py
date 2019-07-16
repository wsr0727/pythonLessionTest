#uncode = utf-8
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
#TemConvert.py
TempStr = input("请输入带有符号的温度值：") #获得输入值,并且向temstr赋值，单一=为赋值
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入错误")