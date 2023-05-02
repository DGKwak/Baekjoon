from sys import stdin as st

N, B = map(int, st.readline().split())

result = ''

while N:
    tmp = N % B
    
    if tmp >= 10:
        result = chr(ord('A')+(tmp-10)) + result
        
    if tmp < 10:
        result = str(tmp) + result
        
    N = N//B
    
print(result)