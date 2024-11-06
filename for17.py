n=int(input("n sonini kiriting: "))
a=int(input("a sonini kiriting: "))
yigindi=1
for x in range(1, n+1):
    yigindi+=a**x
print(yigindi)
