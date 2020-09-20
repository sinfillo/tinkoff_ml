import pickle
import random
with open('dictionary.pickle', 'rb') as f:
    dictionary = pickle.load(f)
with open('words_from_dict.pickle', 'rb') as f:
    words_from_dict = pickle.load(f)
word = random.choice(words_from_dict)
endl_symbols = "!.,?\'\"%^&*()[]{}=_-+#№<>`~–"
while (word in endl_symbols):
    word = random.choice(words_from_dict)
print(word, end=' ')
t = 0
while (t < 500 and word in dictionary and len(dictionary[word]) != 0):
    word = random.choice(dictionary[word])
    print(word, end = ' ')
    t += 1

