from sys import stdin as st

T = int(st.readline())

era = [False, False]+[True]*999999

for i in range(2, 1001):
    if era[i]:
        for j in range(2*i, len(era), i):
            era[j] = False

for _ in range(T):
    N = int(st.readline())
    cnt = 0
    
    for k in range(2, int(N/2)+1):
        if era[k] and era[N-k]:
            cnt += 1
            
    print(cnt)