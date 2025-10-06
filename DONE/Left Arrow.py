"""leftarrow"""
k = int(input())
n = int(input())
MID = n //2

for i in range(n):
    space = abs(MID - i)
    line = " " * space + "*" * k
    print(line)
