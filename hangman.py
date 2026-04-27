import random
from words import word
print(word)
def get_word(words):
    word = random.choice(word)
    while '-' in word or ' '  in word:
        word = random.choice(word)
    return word

def hugman()
