from collections import Counter
 
 #python dosyasna kaydettigim text file cagiriyoruz
 #calismasi icin ayni dosyaya kaydedilmis olmasi gerekiyor
 #reading thr file
with open("text.txt", "r") as file:
    text = file.read()
#prossessing the text: convert to lowecase and split into words
words= text.lower().split()

#counting word frequencies
word_counts= Counter(words)

#display the most frequent words
for word, count in word_counts.most_common():
    print(f"{word}: {count}")