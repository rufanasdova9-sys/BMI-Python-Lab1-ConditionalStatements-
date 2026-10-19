plate = input("plate:")
valid = True
uzunluq = 0
for c in plate:
    uzunluq= uzunluq + 1
if uzunluq < 2 or uzunluq > 6:
    valid = False
else:
    herfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    numberler = "0123456789"
    herf1, herf2 = False
    for h in herfler:
        if plate[0] == h:
            herf1 = True
        if plate[1] == h:
            herf2 = True
    if not (herf1 and herf2):
        valid = False
    else:
        number = False
        for s in plate:
            numberdir = False
            for h in herfler:
                if s == h:
                    herfdir = True
            for r in numberler:
                if s == r:
                    numberdir = True
            if not herfdir and not numberdir:
                valid = False
            if numberdir:
                if not number and s == "0":
                    valid = False
                number = True
            elif number:
                valid = False
if valid:
    print("valid")
else:
    print("invalid")
