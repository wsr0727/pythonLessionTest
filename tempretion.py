coin = input("")
if coin[0:3] == "RMB":
    U = eval(coin[3:])/6.78
    print("USD{:.2f}".format(U))
elif coin[0:3] == "USD":
    R = eval(coin[3:])*6.78
    print("RMB{:.2f}".format(R))