"""temperature"""
num = float(input())
have = input()
want = input()
TEM = num
if have == "C" and want == "F":
    TEM = num * 9/5 +32

if have == "C" and want == "K":
    TEM = num + 273.15

if have == "C" and want == "R":
    TEM = (num+273.15) * 9/5

if have == "C" and want == "C":
    TEM = num

if have == "F" and want == "C":
    TEM = (num-32)/9*5

if have == "F" and want == "K":
    TEM = ((num-32)/9*5)+273.15

if have == "F" and want == "R":
    TEM = num+459.67

if have == "F" and want == "F":
    TEM = num

if have == "K" and want == "K":
    TEM = num

if have == "K" and want == "C":
    TEM = num-273.15

if have == "K" and want == "F":
    TEM = (num-273.15) *9/5+32

if have == "K" and want == "R":
    TEM = num*9/5

if have == "R" and want == "R":
    TEM = num

if have == "R" and want == "C":
    TEM = num *5/9 -273.15

if have == "R" and want == "F":
    TEM = (num *5/9 -273.15)*9/5+32

if have == "R" and want == "K":
    TEM = num *5/9
print(f'{TEM:.2f}')
