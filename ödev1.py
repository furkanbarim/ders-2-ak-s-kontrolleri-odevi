# Ödev :
#  Kullanıcıdan 1-7 arası sayı alın.
# Bu alınan sayıyı islami gün isimlerine göre ekrana yazın
#  Örn: 1. gün  Yevmu’l-İs̠neyn
#  Pazar: Yevmu’l-Eḥad
# Pazartesi: Yevmu’l-İs̠neyn
# Salı: Yevmu’s̠-S̠ülās̠ā’
gun_sayisi: int = int(input("lütfen 1-7 arası bir sayı giriniz: "))
if gun_sayisi > 7:
    print("girmiş olduğunuz sayı 7'den büyük olamaz")
elif gun_sayisi == 1:
    print("Yevmu’l-İs̠neyn")

elif gun_sayisi == 2:
    print("Yevmu’s̠-S̠ülās̠ā’")

elif gun_sayisi == 3:
    print("Yevmu’l-Erbi‘ā’")

elif gun_sayisi == 4:
    print("Yevmu’l-Hamīs")

elif gun_sayisi == 5:
    print("Yevmu’l-Cumu'a")

elif gun_sayisi == 6:
    print("Yevmu’s-Sebt")

elif gun_sayisi == 7:
    print("Yevmu’l-Eḥad")
