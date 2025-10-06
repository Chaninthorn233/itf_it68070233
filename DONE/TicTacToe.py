"""TICTACTOE"""

first = input()
second = input()
third = input()
TL = str()
ML = str()
DL = str()
TC = str()
MC = str()
DC = str()
TR = str()
MR = str()
DR = str()


if first[0:1] == "O":
    TL = "O"

if second[0:1] == "O":
    ML = "O"

if third[0:1] == "O":
    DL = "O"

if first[1:2] == "O":
    TC = "O"

if second[1:2] == "O":
    MC = "O"

if third[1:2] == "O":
    DC = "O"

if first[2:3] == "O":
    TR = "O"

if second[2:3] == "O":
    MR = "O"

if third[2:3] == "O":
    DR = "O"

if first[0:1] == "X":
    TL = "X"

if second[0:1] == "X":
    ML = "X"

if third[0:1] == "X":
    DL = "X"

if first[1:2] == "X":
    TC = "X"

if second[1:2] == "X":
    MC = "X"

if third[1:2] == "X":
    DC = "X"

if first[2:3] == "X":
    TR = "X"

if second[2:3] == "X":
    MR = "X"

if third[2:3] == "X":
    DR = "X"

if TL+TC+TR == "OOO":
    print("O WIN")

elif ML+MC+MR == "OOO":
    print("O WIN")

elif DL+DC+DR == "OOO":
    print("O WIN")

elif TL+ML+DL == "OOO":
    print("O WIN")

elif TC+MC+DC == "OOO":
    print("O WIN")

elif TR+MR+DR == "OOO":
    print("O WIN")

elif DL+MC+TR == "OOO":
    print("O WIN")

elif TL+MC+DR == "OOO":
    print("O WIN")

elif TL+TC+TR == "XXX":
    print("X WIN")

elif ML+MC+MR == "XXX":
    print("X WIN")

elif DL+DC+DR == "XXX":
    print("X WIN")

elif TL+ML+DL == "XXX":
    print("X WIN")

elif TC+MC+DC == "XXX":
    print("X WIN")

elif TR+MR+DR == "XXX":
    print("X WIN")

elif DL+MC+TR == "XXX":
    print("X WIN")

elif TL+MC+DR == "XXX":
    print("X WIN")

else:
    print("DRAW")
