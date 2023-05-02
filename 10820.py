import sys

# while 1:
#     S = sys.stdin.readline().strip('\n')
#     res = [0] * 4
    
#     if len(S) == 0: break
    
#     for i in S:
#         if i.isalpha():
#             if ord(i)-ord('a') < 0:
#                 res[1] += 1
#             else:
#                 res[0] += 1
                
#         elif i == ' ':
#             res[3] += 1
            
#         else: res[2] += 1
        
#     print(' '.join(map(str,res)))

while 1:
    S = sys.stdin.readline().strip('\n')
    res = [0] * 4
    
    if len(S) == 0: break
    
    for i in S:
        if i.islower():
            res[0] += 1
        
        if i.isupper():
            res[1] += 1
        
        if i.isdigit():
            res[2] += 1
        
        if i.isspace():
            res[3] += 1
        
    print(' '.join(map(str,res)))