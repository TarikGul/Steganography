import math
import random

def str2bin(message):
    binary = ' '.join(format(ord(x), 'b') for x in message)
    return binary

def generate_random_word(length, alpha):
    a = alpha.split('')
    word = []

    i = 0
    while (i < length):
        random = random.randint(0, len(a))

        if (i == 0 and random == 26) or (i == length - 1 and random == 26):
            pass
        elif (random == 26 and word[len(word) - 1] == ' '):
            pass
        i = i + 1

        word.append(a[random])
    
    return word.join('')
    
def generate_one_time_pad(message):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
    copy = message.split(' ')
    one_time_pad = []

    for word in copy:
        random_word = generate_random_word(len(word), alpha)
        random = random.randint(0, len(alpha))

        one_time_pad.append(random_word)

        if (i < len(copy) - 1):
            one_time_pad.append(alpha[random])
    
    return one_time_pad.join('')

if __name__ == '__main__':
    str2bin('hey')
