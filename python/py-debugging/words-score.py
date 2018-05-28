# Python > Debugging > Words Score
# Calculate the total score of the list of words.
#
# https://www.hackerrank.com/challenges/words-score/problem
# challenge id: 66426
#

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

# (skeliton_tail) ----------------------------------------------------------------------
n = int(input())
words = input().split()
print(score_words(words))
