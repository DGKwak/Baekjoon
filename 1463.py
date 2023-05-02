n = int(input())

def calCount(n):
    mem = [0]*(n+1)
    
    for i in range(n+1):
        if i < 2: 
            mem[i] = 0
        elif i%2==0 and i%3==0: 
            mem[i] = min(mem[i//2], mem[i//3])+1
        elif i%2==0:
            mem[i] = min(mem[i//2], mem[i-1])+1
        elif i%3==0:
            mem[i] = min(mem[i//3], mem[i-1])+1
        else:
            mem[i] = mem[i-1]+1
            
    return mem[-1]

print(calCount(n))