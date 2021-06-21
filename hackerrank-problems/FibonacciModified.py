
# https://www.hackerrank.com/challenges/fibonacci-modified/problem

# T(i+2) = T(i) + (T(i+1))^2

def getModifiedFibonacci(t1, t2, N):
    nthTerm = 0
    for n in range(3, N+1):
        nthTerm = t1 + t2**2
        t1 = t2
        t2 = nthTerm
    return nthTerm

if __name__ == '__main__':
    t1 = 0
    t2 = 1
    numberOfTerms = 5

    result = getModifiedFibonacci(t1, t2, numberOfTerms)
    print("nth term of the modified fibonacci series:", result)

