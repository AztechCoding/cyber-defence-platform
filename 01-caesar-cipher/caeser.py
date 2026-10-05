UC_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LC_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMBER_ALPHABET = "0123456789"

def shift_letter(letter, shift):
    position = LC_ALPHABET.find(letter)
    new_position = (position + shift) % 26
    return LC_ALPHABET[new_position]

print(shift_letter("b", 5))
print(shift_letter("y", 4))
print(shift_letter("h", 3))
    