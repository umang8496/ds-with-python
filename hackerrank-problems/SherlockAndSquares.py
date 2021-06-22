
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

def squares(a, b):
    lowerBound = int(a**(1/2))
    upperBound = int(b**(1/2))
    count = 0
    for n in range(lowerBound, upperBound+1):
        entry = n**2
        if ((entry >= a) and (entry <= b)):
            count += 1
    return count

if __name__ == "__main__":
    # a = 3
    # b = 9
    a = 17
    b = 24
    num = squares(a, b)
    print(num)
