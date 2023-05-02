from sys import stdin as st

A, B = map(int, st.readline().split())
m = int(st.readline())
N = list(map(int, st.readline().split()))

tmp = 0
result = ''

for i in range(len(N)):
    tmp += N.pop() * (A ** i)


while tmp:
    result = str(tmp % B) + ' ' + result
    
    tmp = tmp//B
    
print(result.strip())