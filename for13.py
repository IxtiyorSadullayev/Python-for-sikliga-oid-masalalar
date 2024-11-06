n=int(input("n sonini kiriting: "))
s=0
son=1.1
for x in range(1,n+1):
    s+=son*(-1*(-1)**x)
    son+=0.1
print(s)