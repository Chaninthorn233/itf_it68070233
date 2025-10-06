""" Largest Number """
a = input().strip()
b = input().strip()
c = input().strip()

COM1 = int(a+b+c)
COM2 = int(a+c+b)
COM3 = int(b+a+c)
COM4 = int(b+c+a)
COM5 = int(c+a+b)
COM6 = int(c+b+a)

TOTAL = COM1
if COM2 > TOTAL:
    TOTAL = COM2
if COM3 > TOTAL:
    TOTAL = COM3
if COM4 > TOTAL:
    TOTAL = COM4
if COM5 > TOTAL:
    TOTAL = COM5
if COM6 > TOTAL:
    TOTAL = COM6

print(TOTAL)
