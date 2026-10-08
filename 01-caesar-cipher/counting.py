counts = {"a": 7, "b": 5, "c": 9}
highest = 0
most_common = ""

for letter in counts:
    if counts[letter] > highest:
        highest = counts[letter]
        most_common = letter

print(most_common)
print(highest)
print(counts)