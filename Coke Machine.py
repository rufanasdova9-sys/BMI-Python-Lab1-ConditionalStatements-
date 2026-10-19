qiymet = 50
kod = True
while kod:
    print("qiymet:", qiymet)
    qepik = int(input("insert qepik: "))
    if qepik == 25:
        qiymet = qiymet- 25
    elif qepik == 10:
        qiymet =qiymet- 10
    elif qepik == 5:
        qiymet -= 5
    if qiymet <= 0:
        active = False
deyisiklik = abs(qiymet)
print("deyisiklik:", deyisiklik)
