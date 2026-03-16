# function that returns the longest word in a given sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)  #len means lenghts of the words
print(longest_word("Python is an amazing programming language"))