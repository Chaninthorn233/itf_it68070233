"""sigmastep"""
x = int(input())
y = int(input())
n = int(input())
SUM = 0
NUM = x
if n < y:
    while NUM < y:
        SUM += NUM
        NUM += n

else:
    print(SUM)
