namn = "Detta är en sträng som du skall ändra"

namn = namn.replace(" ", "*")

antal = 0
for ch in namn:
    if ch == "*":
        antal = antal + 1

print(namn)
print(antal)
print(namn.count("*"))