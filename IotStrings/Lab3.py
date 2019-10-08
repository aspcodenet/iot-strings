s = "I am a C# hacker"

pos = s.rfind("a")
print(pos)

pos = s.find("C")
langd = len(s)
print(f"Pos for C is {pos} and length of string is {langd}")


parts = s.split(' ')
for sub in parts:
    print(sub)

s = s.replace("I", "i")
s = s.replace("a", "A")
s = s.replace("k", "K")
s = s.replace("r", "R")
print(s)
