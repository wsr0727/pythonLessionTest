__author__ = 'Administrator'
Word = input()
if eval(Word) == 0:
    print("Hello World")
elif eval(Word) > 0:
    print("He\nll\no \nWo\nrl\nd")
elif eval(Word) < 0:
    print("H\ne\nl\nl\no\n \nW\no\nr\nl\nd")
else:
    print("参数错误")