from random import randint
WORDS = ['laptop', 'television', 'kitchen', 'policeman', 'computer', 'firetruck']

def random_word(WORDS):
    word = randint(0, len(WORDS))
    return WORDS[word]

word = random_word(WORDS)