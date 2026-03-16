from collections import defaultdict
 
with open("text.txt", "r") as file:
    text = file.read()
#prossessing the text: convert to lowecase and split into words
words= text.lower().split()
word_groups = defaultdict(list)

for word in words:
    first_letter = word[0]
    word_groups[first_letter].append(word)

for letter,group in sorted(word_groups.items()):
    print(f"{letter.upper()}: {','.join(group)}")

#baya bir sure calismadi 3 nokta open folder kismindan text file folderini visual studio da acmalisin
