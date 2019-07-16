__author__ = 'Administrator'
#1
#dayup = pow(1.001,365)
#daydown = pow(0.999,365)

#2
#dayfactor = 0.005
#dayup = pow(1+dayfactor,365)
#daydown = pow(1-dayfactor,365)
#print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))

#3
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001 #dayfactor加上0.001
print("工作日的力量：{:.3f}".format(dayfactor))



