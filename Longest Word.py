** start of main.py **

def get_longest_word(sentence):
    sentence = sentence.split()
    char_number = dict()
    biggest_word = ''
    for word in sentence:
        count = 0
        word = word.replace('.','')
        for char in word:
            count += 1

        char_number[word] = count

    biggest_word = max(char_number,key = char_number.get)
    return biggest_word



** end of main.py **

