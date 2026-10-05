ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def shift_letter(letter, shift):
    position = ALPHABET.find(letter)
    new_position = (position + shift) % 26
    return ALPHABET[new_position]

print(shift_letter("b", 5))
print(shift_letter("y", 4))
print(shift_letter("h", 3))
print(shift_letter("y", 5))
print(shift_letter("M", 3))
print(shift_letter("m", 0))
print(shift_letter("m", 26))
    