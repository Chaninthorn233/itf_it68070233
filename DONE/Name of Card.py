"""NameofCard"""
card = input()
UP = card.upper()
if len(card) == 3:
    if "D" in UP:
        print("10 of Diamonds")
    if "H" in UP:
        print("10 of Hearts")
    if "S" in UP:
        print("10 of Spades")
    if "C" in UP:
        print("10 of Clubs")
else:
    NUM = UP[:1]
    HEAD = UP[1:]
    if "A" in NUM:
        NUM = "Ace"
    if "Q" in NUM:
        NUM = "Queen"
    if "J" in NUM:
        NUM = "Jack"
    if "K" in NUM:
        NUM = "King"

    if "H" in HEAD:
        HEAD = " of Heart"
    if "C" in HEAD:
        HEAD = " of Club"
    if "D" in HEAD:
        HEAD = " of Diamond"
    if "S" in HEAD:
        HEAD = " of Spade"
    print(NUM+HEAD+"s")
