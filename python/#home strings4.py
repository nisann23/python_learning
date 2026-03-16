#home strings4
def counter():
 paragraph= input("Write the paragraph:")
 character= len(paragraph)
 and_check= "and" in paragraph
 word_sum= len(paragraph.split())
 print(f"Character number: {character}")
 print(f"And lower: {and_check}")
 print(f"How many words: {word_sum}")

counter()
