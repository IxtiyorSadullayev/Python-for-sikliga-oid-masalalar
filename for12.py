n=int(input("n sonini kiriting: "))
son=1.1
kopaytma=1
for x in range(n):
    kopaytma*=son 
    son+=0.1
print(kopaytma)