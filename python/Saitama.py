"""Saitama Wannabe"""
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
b1 = int(input())
b2 = int(input())
b4 = int(input())
b3 = int(input())

C1 = b1
C2 = b2
C3 = b3
C4 = b4
COUNT1 = 0
COUNT2 = 0
COUNT3 = 0
COUNT4 = 0
D1 = 0
D2 = 0
D3 = 0
D4 = 0

if a1 >= b1:
    for COUNT1 in range(a1+1):
        if D1 > a1:
            b1 = a1
            break
        D1 += C1

if a2 >= b2:
    for COUNT2 in range(a2+1):
        if D2 > a2:
            b2 = a2
            break
        D2 += C2
        COUNT2 += 1

if COUNT1 > COUNT2:
    COUNT2 = COUNT1
else:
    COUNT1 = COUNT2

if a3 >= b3:
    for COUNT3 in range(a3+1):
        if D3 > a3:
            b3 = a3
            break
        D3 += C3
        COUNT3 += 1

if COUNT3 > COUNT1:
    COUNT1 = COUNT3
else:
    COUNT3 = COUNT1

if a4 >= b4:
    for COUNT4 in range(a4+1):
        if D4 > a4:
            b4 = a4
            break
        D4 += C4
        COUNT4 += 1

if COUNT4 > COUNT1:
    COUNT1 = COUNT4
else:
    COUNT4 = COUNT1

print(COUNT1)
