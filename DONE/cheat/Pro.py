"""Pro"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())

GROUP = z // x
LEFT = z % x

TOTAL = GROUP * y + LEFT
PRICE = TOTAL * a

print(PRICE)
