#home strings2
#kelime degistirici
def change():
 sentence=input("Please enter a sentence:")
 changing= input("whic word do you want to change:")
 new_word= input("what is your new word:")
 new= sentence.replace(changing, new_word)
 print(f"New Sentence:   {new}")

change()
