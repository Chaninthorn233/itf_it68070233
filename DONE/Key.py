"""Key"""
Card = input()
TOTAL = 0
for digit in Card:
    TOTAL += int(digit)

LAST = int(str(Card)[-3:]) * 10
TOTAL = TOTAL + LAST

if TOTAL < 1000:
    TOTAL += 1000
if TOTAL >= 10000:
    TOTAL = str(TOTAL)
    TOTAL = TOTAL[-4:]
print(TOTAL)
