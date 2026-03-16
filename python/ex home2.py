#indirim hesaplama
urun_fiyati= float(input("urun fiyati="))
indirim= float(input("indirim orani (yuzde)="))
indirim_tutari= (urun_fiyati*indirim)/100
son_fiyat= urun_fiyati-indirim_tutari
print(f"indirim tutari {indirim_tutari:.2f}")
print(f"urun fiyati: {son_fiyat:.2f}")
