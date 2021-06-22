
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValidString(givenString):
    mapOfCharacters = {}
    for ch in givenString:
        if (ch in mapOfCharacters.keys()):
            mapOfCharacters[ch] += 1
        else:
            mapOfCharacters[ch] = 1
    freqList = list(mapOfCharacters.values())
    baseFreq = min(freqList)
    permissibileModification = 1
    actualModification = 0
    for f in range(0, len(freqList)):
        diff = (freqList[f] - baseFreq)
        # if diff is negative, then make it positive
        if (diff < 0):
            diff = diff * (-1)
        # if diff is greater than 2, then the givenString is not valid
        if (diff >= 2):
            return 'NO'
        # id diff is exactly 1
        if (diff == 1):
            # if modification has been performed, then return NO
            if (actualModification == 1):
                return 'NO'
            else:
                # perform the only permissible modification
                actualModification = permissibileModification
    return 'YES'


def isValid(s):
    d = Counter(s)
    counts = Counter(d.values())
    if len(counts) == 1:
        return "YES"
    elif len(counts) > 2:
        return "NO"
    else:
        max_v = max(counts.values())
        k1, k2 = counts.keys()
        if (max_v == len(d) - 1):
            if (abs(k1 - k2) == 1):
                return "YES"
            elif (min(k1, k2) == 1):
                if counts[1] == 1:
                    return "YES"
                else:
                    return "NO"
            else:
                return "NO"
        else:
            return "NO"


if __name__ == '__main__':
    # givenString = 'abc'
    # givenString = 'abcc'
    # givenString = 'abccc'
    # givenString = 'abcdefghhgfedecba'
    # givenString = 'aabbcd'
    givenString = 'aabbc'
    booleanResult = isValid(givenString)
    print(booleanResult)

