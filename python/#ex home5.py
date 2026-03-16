#home strings 0
#@ oncesi ve sonrasi alma ornek kod (gemini)
email = "andreea.bogoslov@ulbsibiu.ro"

# '@' karakterinin yerini bulmak için .index() metodu kullanılır
index_of_at = email.index("@") 

# Slicing (Dilimleme)
kullanici_adi = email[0 : index_of_at]  # Baştan (0) '@' sembolüne kadar al
alan_adi = email[index_of_at + 1 : ]    # '@' sembolünden bir sonraki karakterden EN SONA kadar al

print(f"Tam E-posta: {email}")
print(f"Kullanıcı Adı: {kullanici_adi}")
print(f"Alan Adı: {alan_adi}")