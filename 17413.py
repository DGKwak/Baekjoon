import sys

str = sys.stdin.readline().strip()
result = []
chk = 0
cnt = 0

for i in range(len(str)):
    if str[i] == '<':
        result.append(str[i])
        chk = 1
    
    elif str[i] == '>':
        result.append(str[i])
        chk = 0
        cnt = i+1
    
    elif chk == 1:
        result.append(str[i])
        
    elif chk == 0 and str[i] == ' ':
        result.append(str[i])
        cnt = i+1
    
    else:
        result.insert(cnt, str[i])

print(''.join(result))