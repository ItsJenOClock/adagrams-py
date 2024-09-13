import random

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():
    letters_available = []
    letters_drawn = []

    for letter, quantity in LETTER_POOL.items():
        for i in range(quantity):
            letters_available.append(letter)
    
    for i in range(10):
        random_number = random.randint(0, len(letters_available) - 1)
        letters_drawn.append(letters_available[random_number])
        letters_available.pop(random_number)
    
    return letters_drawn

def uses_available_letters(word, letter_bank):
    word = word.upper()
    letter_bank_dict = {}
    letter_count = 0

    for letter in letter_bank:
        if letter not in letter_bank_dict.keys():
            letter_bank_dict[letter] = 1
        else:
            letter_bank_dict[letter] += 1

    for letter in word:
        if letter not in letter_bank_dict.keys() or letter_bank_dict[letter] == 0:
            return False
        else:
            letter_bank_dict[letter] -= 1

    return True

def score_word(word):
    score_chart = {
        'A': 1, 
        'B': 3, 
        'C': 3, 
        'D': 2, 
        'E': 1, 
        'F': 4, 
        'G': 2, 
        'H': 4, 
        'I': 1, 
        'J': 8, 
        'K': 5, 
        'L': 1, 
        'M': 3, 
        'N': 1, 
        'O': 1, 
        'P': 3, 
        'Q': 10, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'U': 1, 
        'V': 4, 
        'W': 4, 
        'X': 8, 
        'Y': 4, 
        'Z': 10
    }
    score = 0
    word = word.upper()

    for letter in word:
        score += score_chart[letter]

    if 7 <= len(word) <= 10:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    highest_score = 0
    highest_word = ["", 0]

    for word in word_list:
        score = score_word(word)

        if score > highest_score:
            highest_score = score
            highest_word[0] = word
            highest_word[1] = highest_score
        elif score == highest_score:
            if len(highest_word[0]) == 10:
                continue
            elif len(word) == 10:
                highest_word[0] = word
            elif len(word) == len(highest_word[0]):
                continue
            elif len(word) < len(highest_word[0]):
                highest_word[0] = word
    
    return tuple(highest_word)