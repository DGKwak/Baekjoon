from sys import stdin

N ='0b'+ stdin.readline().strip()

print(format(int(N, 2), 'o'))