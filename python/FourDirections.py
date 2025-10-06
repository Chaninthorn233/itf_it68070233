"""Four Directions"""
Direct = input()
L1 = str()
L2 = str()
L3 = str()
L4 = str()
L5 = str()

for i in range(len(Direct)):
    if "U" in Direct:
        L1 = L1 + "  *  "
        L2 = L2 + " *** "
        L3 = L3 + "* * *"
        L4 = L4 + "  *  "
        L5 = L5 + "  *  "
    if "D"in Direct:
        L1 = L1 + "  *  "
        L2 = L2 + "  *  "
        L3 = L3 + "* * *"






