"""Bubble Tea"""
bub = input()
tea = input()
SWEET = int(tea[2:3])
NUM = int(tea[4:])
GRAM = int(bub[2:])
if "H" in bub:
    GRAM = 5*GRAM
elif "O" in bub:
    GRAM = 3*GRAM
elif "J" in bub:
    GRAM = 2*GRAM

if "R" in tea:
    if SWEET == 1:
        tea = 12*NUM
    if SWEET == 2:
        tea = 18*NUM
    if SWEET == 3:
        tea = 25*NUM

elif "T" in tea:
    if SWEET == 1:
        tea = 15*NUM
    if SWEET == 2:
        tea = 20*NUM
    if SWEET == 3:
        tea = 30*NUM

elif "M" in tea:
    if SWEET == 1:
        tea = 10*NUM
    if SWEET == 2:
        tea = 15*NUM
    if SWEET == 3:
        tea = 20*NUM
print(tea+GRAM)
