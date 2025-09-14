** start of main.py **

def reverse_sentence(sentence):
    sentence_2 = list()
    sentence_3 = ''
    sentence = sentence.strip()
    sentence_1 = sentence.split()
    length = len(sentence_1) - 1
    for i in range(length,-1,-1):
        sentence_2.append(sentence_1[i])
    for word in sentence_2:
        sentence_3 += ' ' + word

    sentence_3 = sentence_3.strip()
    return sentence_3

reverse_sentence("push commit git")

** end of main.py **

