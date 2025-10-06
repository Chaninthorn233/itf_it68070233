"""Diginity"""
NUM = 1
CUT = 0

while NUM != 0:
    NUM = int(input())
    if NUM == 0:
        break
    elif len(str(NUM)) > 1:
        CUT = NUM

print(CUT)
