


inmatning = input("Mata in epostadress")


if inmatning.find("@") != -1:
    pos = inmatning.rfind(".")
    teckenEfter = len(inmatning) -1 - pos
    if pos > -1 and (teckenEfter == 2 or teckenEfter == 3):
        print("ok")

#Carl
#while True:
#    email = input("Ange din epostadress: ")
#    emailReversed = email[::-1]
#    if email.count("@") == 1:
#        if emailReversed[2] == "." or emailReversed[3] == ".":
#            print("Du har matat in en korrekt epostadress.")
#            break

#        else:
#            print("Du har matat in en felaktig epostadress.")
#    else:
#        print("Du har matat in en felaktig epostadress.")