n = int(input())

for i in range(1,n+1):
    a = " " * (n-i) + "*" + " " * (2*(i-1)-1) + "*"
    if i == 1:
        a = " " * (n-i) + "*"
            
    if i == n:
        a = "*" * (2*n-1)
    print(a)