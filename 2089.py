from sys import stdin as st

N = int(st.readline())

result = 0
i = 0

while N:
    if N % -2:
        N = (N//-2) + 1
        result += 10**i
    else:
        N = N//-2
    
    i+= 1
    
print(result)