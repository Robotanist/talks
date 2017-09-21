# The following puzzle comes from the checkio website and is used as the
# basis for a group problem-solving session during one of our PyHawaii sessions
# https://py.checkio.org/mission/the-longest-palindromic/

# Your task is to write a function that finds the longest palindromic substring
# of a given string.

# If you find more than one substring you should return the one which is closer
# to the beginning.

# VERSION 1 -------------------------------------
def longest_palindromic(text):
    '''Parse through the palindrome examining each substring (sub)
    spanning from first character to the last character.

    Then shift to examine the next substring
    spanning from the second character to the last character.

    Continue shifting across text to make ever shorter substrings.
    '''

    pal_list = []

    for x, _ in enumerate(text):
        for y in range(x+1, len(text)+1):

            # snip text from x up to but not including y
            #    compare the reversed version to the forward version
            sub = text[x:y]
            if sub[::-1] == sub:
                pal_list.append(sub)

    return max(pal_list, key=len)


# VERSION 2 -------------------------------------
'''
from itertools import combinations as C
​
def longest_palindromic(text):
    subs = (text[start: end] for start, end in C(range(len(text) + 1), 2))
    return max((s for s in subs if s == s[::-1]), key=len)
'''

if __name__ == '__main__':

    assert longest_palindromic("artrartrt") == "rtrartr"
    assert longest_palindromic("abacada") == "aba"
    assert longest_palindromic("aaaa") == "aaaa"
    print('All tests passed successfully')
