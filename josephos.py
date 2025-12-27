def josephos(n,k):
    if n==1:
        return 0
    return(josephos(n-1,1)+k)%n
print(josephos(n:100,k:2))
