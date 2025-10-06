"""Virus I"""
virus = input()
COUNT = 0
x = list(virus)
OK = range(len(x))
for i in OK:
    if x[i] == "O":
        continue
    if x[i] == "o":
        COUNT += 1
print(COUNT)
