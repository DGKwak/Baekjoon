from sys import stdin as st

N = int(st.readline())

L = [False, False] + [True]*9999999

for i in range(int(10000000**0.5)+1):
    if L[i]:
        for j in range(2*i, len(L), i):
            L[j] = False
            
while N != 1:
    for i in range(2, len(L)):
        if L[i] and N % i ==0:
            tmp = i
            print(tmp)
            break
        
    N = N//tmp