n = int(input())
a = input()

tmp = a.split(" ")

for i in range(n):
    if i == 0:
        max, min = int(tmp[i]), int(tmp[i])
        continue
    
    if max < int(tmp[i]):
        max = int(tmp[i])
    
    if min > int(tmp[i]):
        min = int(tmp[i])
        
        
print(min, max)