#counting vowels code (unlu harfleri sayma kodu)
def count_vowels(s):
    vowels= "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)  #for char in s s icindeki her karakter(char) icin dongu yapar ve if ten sonraki kisim sadece vowels varsa devam et kosulu
#basindaki 1 de her kosul saglandiginda 1 degeri ver demek
print(count_vowels("Algorithms and Data STructures"))