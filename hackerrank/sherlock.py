#!/usr/bin/python3
# Challenge description: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
from collections import Counter


def isValid(s):
    letter_occurences = Counter(s)
    letter_counts = list(letter_occurences.values())

    least = min(letter_counts)
    most = max(letter_counts)

    if least == most:
        return 'YES'
    if most - least == 1 and letter_counts.count(most) == 1:
        return 'YES'
    if least == 1 and letter_counts.count(least) == 1 and\
            all((count in {least, most} for count in letter_counts)):
        return 'YES'

    return 'NO'
