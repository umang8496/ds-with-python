
# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(alphabets, word):
    alphabetsMap = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }

    maxAlphabetWeight = 0
    for alpha in word:
        alphaIndex = alphabetsMap[alpha]
        weight = alphabets[alphaIndex]
        if (weight > maxAlphabetWeight):
            maxAlphabetWeight = weight
    return maxAlphabetWeight * len(word)


if __name__ == '__main__':
    alphabets = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = 'zaba'
    print(designerPdfViewer(alphabets, word))

    