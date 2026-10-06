ALPHABET = "abcdefghijklmnopqrstuvwxyz"
character = "5"

if character in ALPHABET:
    print("Character is in the alphabet")
elif character in "0123456789":
    print("Character is a number")
else:
    print("Character is not in the alphabet or a number")

shift = 3

if shift == 5:
    print("Shift is 3")
else:
    print("Shift is not 3")
