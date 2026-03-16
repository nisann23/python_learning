#home strings3
# e-posta bilgisi gizleme
def hide_mail():
 posta=input("Mail adresinizi giriniz:")
 at= posta.index("@")
 kalan= posta[at:]
 dilimle= posta[: at]
 ilkiki= posta[:2]
 koy= "*" * (len(dilimle) -2)
 son= ilkiki+ koy+ kalan
 print(f"son hali= {son}")

hide_mail()
