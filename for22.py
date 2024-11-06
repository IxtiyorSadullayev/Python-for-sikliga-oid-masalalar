n=int(input("n ni kiriting: "))
x=int(input("x ni kiriting: "))
yigindi=1
kopaytma=1
for x in range(1, n+1):
    kopaytma*=x
    yigindi+=(x**n)/kopaytma
print(yigindi)