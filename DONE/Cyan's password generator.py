"""Cyan's password generator"""
name = input()
sur = input()
AGE = int(input())
AGE = str(AGE)
if len(name) >= 5 and len(sur) >= 5:
    password = name[:2] + sur[-1:] + AGE[-1]
else:
    password = name[:1] + AGE + sur[-1]

print(password)
