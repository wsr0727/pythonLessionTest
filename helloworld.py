__author__ = 'Administrator'
# -*- coding: utf-8 -*-
#TemConvert.py
TempStr = input("")
if TempStr[0] in ['F','f']:
    C = (eval(TempStr[1:]) - 32)/1.8
    print("{:.2f}C".format(C))
elif TempStr[0] in ['C','c']:
    F = 1.8*eval(TempStr[1:]) + 32
    print("F{:.2f}".format(F))
else:
    print("")