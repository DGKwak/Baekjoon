from sys import stdin as st

N, B = st.readline().split()
B = int(B)

result = 0
n = 0

for i in reversed(N):
    if i.isalpha():
        tmp = 10 + (ord(i) - ord('A'))
        result += B**n * tmp
    
    if i.isdigit():
        result += B**n * int(i)
    
    n += 1
    
print(result)