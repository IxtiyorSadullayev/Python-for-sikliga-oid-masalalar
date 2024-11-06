n=int(input("n sonini kiriting: "))
yigindi=0
kopaytma=1
for x in range(1, n+1):
    kopaytma*=x 
    yigindi+=kopaytma
print(yigindi)