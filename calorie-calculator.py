 
#kalori hesplayıcı

kilo = int(input("Kilo:  "))
boy = int(input("Boy: "))
yas = int(input("Yas: "))
print("-Antrenman Sitemi-")
print("Az Haraket'se = 1 seç")
print("Orta Haraket'se = 2 seç")
print("Yoğun Haraket'se = 3 seç")
secim = int(input("Secim: "))
bmr = 10 * kilo + 6.25 * boy - 5 * yas + 5

if secim == 1:
    hesap = bmr * 1.2
    print("Sonuç: ",hesap)
elif secim == 2:
    hesap = bmr * 1.55
    print("Sonuç: ",hesap)
elif secim == 3:
    hesap = bmr * 1.9
    print("Sonuç: ",hesap)
