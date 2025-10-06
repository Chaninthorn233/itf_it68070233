"""BTS MRT"""
day = input()
age = float(input())
cen = float(input())

if day == "Children Day":
    if age < 14 and cen <= 140.0:
        print("FREE")
    else:
        print("PAY")
if day == "Senior Day":
    if age >= 60:
        print("FREE")
    elif age < 14 and cen < 90.0:
        print("FREE")
    else:
        print("PAY")
if day == "Normal Day":
    if age < 14 and cen < 90.0:
        print("FREE")
    else:
        print("PAY")
