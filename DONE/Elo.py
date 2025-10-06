"""EloIjudge"""
ra = int(input())
rb = int(input())
player = input()

ea = 1 / (1 + 10 ** ((rb - ra)/400))
eb = 1 - ea

if player == "A":
    print(f"{ea:.2f}")
elif player == "B":
    print(f"{eb:.2f}")
