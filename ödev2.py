##ÖDEV:  Kullanıcıdan vize final not girilmesi istensin
# not aralığı 0 ile 100 arasında olmalıdır.
## vize ve finalin ortalaması alınsın.
## 0-44 : Kaldınız
## 45-69: Geçtiniz
## 70-84: İyi
## 85-100: Pekiyi

vize_notu : int = int(input("lütfen 0-100 arası bir sayı giriniz: "))
final_notu : int = int(input("lütfen 0-100 arası bir sayı giriniz: "))

average : float =(vize_notu/2 + final_notu/2 )

if (average > 100) and (average < 0 ):
    print("girmiş olduğunuz sayı 100 den büyük 0 dan küçük olamaz")

elif (average > 0) and (average < 44):
    print("kaldınız")

elif (average > 45) and (average < 69):
    print("geçtiniz")

elif (average > 70) and (average < 84):
    print("iyi")

elif (average > 85) and (average < 100):
    print("pek iyi")

