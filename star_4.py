n=5
for i in range(n):
    for j in range(4-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
