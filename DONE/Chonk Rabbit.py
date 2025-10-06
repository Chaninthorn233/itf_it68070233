"""Chonk Rabbit"""
n = int(input())
COUNT = 0
WEI2 = 0
NAME2 = str()
for i in range(n):
    name, wei = input().split()
    wei = int(wei)
    if wei > 15:
        COUNT += 1 + i - i

    if wei > WEI2:
        NAME2 = name
        WEI2 = wei

WEI2 = str(WEI2)
print(COUNT)
print(NAME2 + " " + WEI2)
