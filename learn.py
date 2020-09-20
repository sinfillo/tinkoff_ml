train = open('текст1.txt', 'r', encoding = 'utf-8') 
endl_symbols = "!.,?\'\"%^&*()[]{}=_-+#№<>`~–"
space_symbols=' \n\t\v\r\f'
dictionary = {}
word = ''
words_from_dict = []
for i in train:
    for j in i:
        if (j in space_symbols):
            words_from_dict.append(word)
            word = ''
        elif (j in endl_symbols):
            words_from_dict.append(word)
            word = j
        else:
            word += j
prev = words_from_dict[0]
dictionary[prev]=[]
for i in range(1, len(words_from_dict)):
    nexxt = words_from_dict[i]
    if prev not in dictionary:
        dictionary[prev]=[]
    dictionary[prev].append(nexxt)
    prev = nexxt


        
            
