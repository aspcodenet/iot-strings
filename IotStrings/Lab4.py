namn = "kurt andersson"

nyttNamn = ""
delar = namn.split(" ")
for n in delar:
    if nyttNamn != "":
        nyttNamn += " "
    nyttNamn += n[0].upper()
    for rest in range(1,len(n)):
        nyttNamn += n[rest]

print(nyttNamn)