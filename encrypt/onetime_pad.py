import math
import random

def generate_encryption(message):
    one_time_pad = generate_one_time_pad(message)
    one_time_pad_bin = str2bin(one_time_pad)
    message_bin = str2bin(message)
    encryption = []

    if (len(one_time_pad_bin) != len(message_bin)):
        print('message and one time pad must be the same length')
        return
    
    for i in range(len(message_bin)):
        new_bin = xor(message_bin[i], one_time_pad_bin[i])
        encryption.append(new_bin)

    return "".join(encryption)

def xor(a, b):
    binary = ''

    print(a)
    print(b)
    for i in range(len(a)):
        print('aaaaaa', a[i])
        num = bin(int(a[i]) ^ int(b[i]))
        binary = binary + str(num)

def str2bin(message):
    binary = ' '.join(format(ord(x), 'b') for x in message)
    return binary

def generate_random_word(length, alpha):
    a = list(alpha)
    word = []

    i = 0
    while (i < length):
        rand = random.randint(0, len(a) - 1)

        if (i == 0 and rand == 26) or (i == length - 1 and rand == 26):
            pass
        elif (rand == 26 and word[len(word) - 1] == ' '):
            pass
        i = i + 1

        word.append(a[rand])

    return "".join(word)
    
def generate_one_time_pad(message):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
    copy = message.split(' ', 1)
    one_time_pad = []

    i = 0
    while (i < len(copy)):
        random_word = generate_random_word(len(copy[i]), alpha)
        rand = random.randint(0, len(alpha) - 1)

        one_time_pad.append(random_word)

        if (i < len(copy) - 1):
            one_time_pad.append(alpha[rand])
        
        i = i + 1
    
    return ''.join(one_time_pad)

if __name__ == '__main__':
    message = 'hey there kiddo this is the one time pad'
    result = generate_encryption(message)
    print(result)
