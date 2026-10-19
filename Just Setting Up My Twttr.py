metn = input("Input: ")
cavab = ""
for herif in metn:
    if herif.lower() not in "aeiou":
        cavab += herif
print(cavab)
