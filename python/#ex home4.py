
sepet = float(input("Sepet tutarı = "))
kupon = input("Kupon var mı (var/yok): ")

if sepet > 500:
    if kupon == "var":
        tutar = sepet * 0.15
        print("Sepet 500 TL ve üzeri, kupon mevcut: %15 indirim uygulandi.")
    else:
        tutar = sepet * 0.10
        print(f"Sepet 500 TL ve üzeri: %10 indirim uyguland. İndirim tutarı: {tutar:.2f} TL")

elif sepet <= 499 and sepet > 200:
    tutar = sepet * 0.05
    print(f"Sepet 200 TL ve üzeri: %5 indirim uygulandı. İndirim tutarı: {tutar:.2f} TL")

else:
    tutar = 0
    print("İndirim için minimum sepet tutarı 200 TL'dir.")

son_fiyat = sepet - tutar

print(f"\nSepet Toplamı: {sepet:.2f} TL")
print(f"İndirim Tutarı: {tutar:.2f} TL")
print(f"Ödenecek Tutar: {son_fiyat:.2f} TL")


