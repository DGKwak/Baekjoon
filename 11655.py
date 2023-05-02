import sys

S = sys.stdin.readline().strip('\n')
res = ''

for i in S:   
    if i.isalpha():
        if i.islower():
            if ord(i)+13 > 122:
                res += chr(ord(i)+13-26)
                continue

        if i.isupper():
            if ord(i)+13 > 90:
                res += chr(ord(i)+13-26)
                continue
        
        res += chr(ord(i)+13)
        
    else:
        res += i
        
print(res)