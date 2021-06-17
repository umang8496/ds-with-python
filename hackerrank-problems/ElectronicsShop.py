
# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards, drives, budget):
    globalMaximum = -1
    for k in keyboards:
        for d in drives:
            localMaximum = (k + d)
            if (localMaximum > globalMaximum):
                if (localMaximum <= budget):
                    globalMaximum = localMaximum
    return globalMaximum


if __name__ == '__main__':
    # budget = 10
    # keyboards = [3, 1]
    # drives = [5, 2, 8]

    budget = 5
    keyboards = [4]
    drives = [5]

    print(getMoneySpent(keyboards, drives, budget))

