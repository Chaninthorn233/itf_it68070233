"""113"""
s = input()

RESULT = ""

for c in s:
    RESULT += c
    if len(RESULT) >= 3:
        if RESULT[-3:] == "113":
            RESULT = RESULT[:-3]

print(RESULT)
