"""CoinChangev1"""
CHANGE = int(input())
COIN = 0
while CHANGE >= 25:
    CHANGE -= 25
    COIN += 1

while CHANGE >= 10:
    CHANGE -= 10
    COIN += 1

while CHANGE >= 5:
    CHANGE -= 5
    COIN += 1

while CHANGE >= 1:
    CHANGE -= 1
    COIN += 1

print(COIN)
