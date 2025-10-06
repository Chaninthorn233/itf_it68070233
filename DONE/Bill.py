"""BillIJUDGE"""
money = int(input())
SERVICE = money * 0.1
if SERVICE < 50:
    SERVICE = 50
elif SERVICE > 1000:
    SERVICE = 1000
vat = (money + SERVICE)*0.07
som = vat + money + SERVICE
print(f"{som:.2f}")
