counts = {}

for character in "aab":
    counts[character] = counts.get(character, 0) + 1

print(counts)