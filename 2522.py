n = int(input())
tmp = 2*n

for i in range(1,tmp):
    if i > n:
        i = 2*n-i
    print(" "*(n-i)+"*"*i)