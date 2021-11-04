"""
TARGET GAME MODULE
"""
from typing import List
import string
import random
import sys

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = [[],[],[]]
    for i in range(len(grid)):
        for _ in range(len(grid)):
            grid[i].append(random.choice(string.ascii_uppercase))
    return grid

def letter_count(word, letters):
    """
    Returns tuple consisting of letter name and
    the amount of times it occurs in line
    """
    tup_letter_count = []
    word = word.lower()
    for i in range(len(word)):
        if i == 0:
            tup_letter_count.append((word[i], word.count(word[i])))
        elif word[i] not in word[:i] and i != 0:
            tup_letter_count.append((word[i], word.count(word[i])))
    # counter = 0
    for i in range(len(tup_letter_count)):
        if tup_letter_count[i][1] > letters.count(tup_letter_count[i][0]):
            return False
    #         counter += 1
    # if counter == len(tup_letter_count):
    return True
# print(letter_count("aaron", [el for el in 'jniarnoah']))
def get_words(filename: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(filename, "r") as file:
        words = []
        # if len(letters) == 9:
        for line in file:
            word = line.lower().replace("\n", "")
            if (len(word) >= 4) and (len(word) <= 9) and letters[4] in word:
                # lst = list(word)
                # for i in range(len(lst)):
                    # if lst[i] in letters:
                    #     counter += 1
                    #     if counter == len(lst):
                if letter_count(word,letters) == True:
                    words.append(word)
        # else:
        #     for line in file:
        #         letters_new = list(letters[0])
        #         line = line.lower().replace("\n", "")
        #         if len(line) >= 4 and len(line) <= 9 and letters_new[4] in line:
        #             lst = list(line)
        #             counter = 0
        #             for i in range(len(lst)):
        #                 if lst[i] in letters_new:
        #                     counter += 1
        #                     if counter == len(lst):
        #                         if letter_count(line,letters):
        #                             words.append(line)
    return words

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = []
    for word in sys.stdin.readlines():
        if word.islower() and word not in words:
            words.append(word)
    return words

def word_rule_check(line, letters):
    if len(line) >= 4 and letters[4] in line:
        lst = list(line)
        counter = 0
        for i in range(len(lst)):
            if lst[i] in letters:
                counter += 1
                if counter == len(lst):
                    if letter_count(line):
                        return True
                    return False


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    # required_letter = letters[4]
    # pure_user_words = []
    # for word in user_words:
    #     if (required_letter in word) and (len(word) >= 4):
    #         counter = 0
    #         for char in word:
    #             counter += 1
    #             if char not in letters:
    #                 break
    #             elif counter == len(word) - 1:
    #                 words.append(word)
    pure_user_words = []
    for word in user_words:
        if word_rule_check(word,letters) and word not in words_from_dict:
            pure_user_words.append(word)
    return pure_user_words


def results():
    letters = generate_grid()
    letters = letters[0] + letters[1] + letters[2]
    right_words = []
    right_words_count = 0
    dict_words = get_words("en", letters)
    user_words = get_user_words()
    wrong_words = get_pure_user_words(user_words, letters, dict_words)

    for word in user_words:
        if word in dict_words:
            right_words_count += 1
            right_words.append(word)
            dict_words.remove(word)
    print("Number of right words: " + right_words_count)
    print("Words you did not guess: " + dict_words)
    print("Wrong words: " + wrong_words)

    with open("results.txt", "w", encoding='UTF-8') as result:
        result.write(str(right_words_count) + '\n')
        result.write('\n'.join(dict_words))
        result.write('\n'.join(wrong_words))
if __name__ == "__main__":
    results()