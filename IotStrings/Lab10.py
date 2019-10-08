
inmatning = input("Skriv in en text")

inmatning = inmatning.replace(" ", "")

reverseString = ""
for index in range(len(inmatning)-1,-1,-1):
    reverseString = reverseString + inmatning[index]

print(inmatning)
print(reverseString)

if(inmatning == reverseString):
    print("Det är en palindrom")