"""sseason"""
month = int(input())
day = int(input())

if month in [3,6,9,12] and day < 21:
    if month == 3:
        print("winter")
    elif month == 6:
        print("spring")
    elif month == 9:
        print("summer")
    elif month == 12:
        print("fall")

elif month in [3,6,9,12] and day >= 21:
    if month == 3:
        print("spring")
    if month == 6:
        print("summer")
    if month == 9:
        print("fall")
    if month == 12:
        print("winter")

elif month in[1,2]:
    print("winter")

elif month in[4,5]:
    print("spring")

elif month in[7,8]:
    print("summer")

elif month in [10,11]:
    print("fall")
