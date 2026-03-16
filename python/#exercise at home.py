#exercise at home
urun= "saat"
sayi= 19.89
adet=12
print(urun, type(urun))
print(sayi, type(sayi))
print(adet, type(adet))


#ogrenci donem sonu notu hesaplama
vize=80
final=86
vize_rate= 0.40* vize
final_rate= 0.60* final
donem_sonu_notu= vize_rate+final_rate
print(f"ogrenci notu:{donem_sonu_notu}")


#dökdortgen alan ve cevre hesabi
kisa= int(input("dikdortgen kisa kenari="))
uzun= int(input("dikdortgen uzun kenari="))
alan= kisa*uzun
cevre= 2*(kisa+uzun)
print(f"alani: {alan:.2f}")
print(f"cevresi: {cevre:.2f}")
#ondalik icin :.2f yapmalisin



