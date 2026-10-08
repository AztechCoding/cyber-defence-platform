ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def shift_letter(letter, shift):
    position = ALPHABET.find(letter)
    new_position = (position + shift) % 26
    return ALPHABET[new_position]

def shift_character(character, shift):
    lower = character.lower()
    if lower in ALPHABET:
        position = ALPHABET.find(lower)
        new_letter = ALPHABET[(position + shift) % 26]
        if character.isupper():
            return new_letter.upper()
        return new_letter
    else:
        return character

def shift_text(text, shift):
    result = ""
    for character in text:
        result += shift_character(character, shift)
    return result

def encrypt(text, shift):
    return shift_text(text, shift)

def decrypt(text, shift):
    return shift_text(text, -shift)

secret = encrypt("Caeser Test!!", 5)

def count_letters(text):
    counts = {}
    for character in text.lower():
        if character in ALPHABET:
            counts[character] = counts.get(character, 0) + 1
    return counts

print(count_letters("Hello, World!"))
print(count_letters("Aa!"))
print(decrypt(secret, 5))
print(secret)
print(shift_text("Hi!", 1))
print(shift_text("abc", 1))
print(shift_character("5", 3))
print(shift_character("z", 1))
print("[", shift_character(" ", 5), "]", sep="")
print(shift_character("!", 3))
print(shift_character("h", 3))
print(shift_character("H", 3))
print(shift_letter("b", 5))
print(shift_letter("y", 4))
print(shift_letter("h", 3))
print(shift_letter("y", 5))
print(shift_letter("M", 3))
print(shift_letter("m", 0))
print(shift_letter("m", 26))
    