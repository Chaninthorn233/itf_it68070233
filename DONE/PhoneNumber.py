"""PHONENUMBEWR"""
num = input()
DORI = input()
NUM0 = str()
NUM1 = str()
NUM2 = str()
if DORI == "Domestic":
    if len(num) == 9:
        NUM1 = num[1:5]
        NUM2 = num[5:]
        print("0 "+NUM1+" "+NUM2)
    if len(num) == 10:
        NUM0 = num[1:2]
        NUM1 = num[2:6]
        NUM2 = num[6:]
        print("0"+NUM0+" "+NUM1 + " " + NUM2)
if DORI == "International":
    if len(num) == 9:
        NUM1 = num[1:5]
        NUM2 = num[5:]
        print("+66 "+NUM1+" "+NUM2)
    if len(num) == 10:
        NUM0 = num[1:2]
        NUM1 = num[2:6]
        NUM2 = num[6:]
        print("+66"+NUM0+" "+NUM1 + " " + NUM2)
