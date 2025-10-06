"""Safe Password"""
char = input()
num = int(input())
ANS = "H 4567"
NAH = str(num)
TT = 0
DD = 0
if char in ANS:
    TT = 1
if NAH in ANS:
    DD = 1
if TT == 1 and DD == 1:
    print("safe unlocked")
elif not TT and DD == 1:
    print("safe locked - change char")
elif not DD and TT == 1:
    print("safe locked - change digit")
else:
    print("safe locked")
