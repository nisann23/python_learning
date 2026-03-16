#ex home 3
#kullanicidan ders notu
not= int(input("Ders notunu girin(0-100 arasi:)"))
if not<=49:
    print("harf notu FF ogrenci kaldi")
elif not<69:
    print("harf notu DD")
elif not<79:
    print("harf notu CC")
elif not<89:
    print("harf notu BB")
elif not <=100:
    print("harf notu AA")
else:
    print("hatali giris")


#BU SEKİLDE YAPARSAN - DEGER GİRİLDİGİNDE DE FF VERİR BU YUZDEN YUKARDAN ASAGİ YAP DOGRUSU:
notu = int(input("Ders notunu girin (0-100 arasi): "))

# 1. Önce geçersiz notları kontrol et
if notu < 0 or notu > 100:
    print("Hatalİ Giriş! Lütfen 0 ile 100 arasİnda bir değer girin.")
# 2. Sonra en yüksek nottan başla
elif notu >= 90:  # 90-100 aralığı (100 zaten üstte kontrol edildi)
    print("Harf Notu: AA")
elif notu >= 80:  # 80-89 aralığı (çünkü 90+ olsaydı ilk if'e girerdi)
    print("Harf Notu: BB")
elif notu >= 70:  # 70-79 aralığı
    print("Harf Notu: CC")
elif notu >= 50:  # 50-69 aralığı
    print("Harf Notu: DD")
else:  # Geriye kalan tek olasılık (0-49 aralığı)
    print("Harf Notu: FF (Kaldİnİz)")