
# Fibonacci Number
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 53, ... 

# iterative approach
def getKthFibonacciNumberIteratively(N):
    if (N == 1):
        return 0
    if ((N == 2) or (N == 3)):
        return 1

    F0 = 1
    F1 = 1
    fib = 0
    for f in range(4, N+1):
        fib = F0 + F1
        F0 = F1
        F1 = fib
    return fib
## END


# recursive approach
def getKthFibonacciNumberRecursively(N):
    return getFibonacci(N)
## END

def getFibonacci(N):
    if (N == 1):
        return 0
    if (N == 2):
        return 1

    return getFibonacci(N - 1) + getFibonacci(N - 2)
## END


# Dynamic Programming approach
def getKthFibonacciNumberByDynamicProgramming(N):
    memoize = [-1 for f in range(0, N+1)]
    return getFibonacciByDynamicProgramming(N, memoize)
## END

def getFibonacciByDynamicProgramming(N, memoize):
    if (memoize[N] != -1):
        return memoize[N]
    if (N == 1):
        return 0
    if (N == 2):
        return 1

    memoize[N] = getFibonacci(N - 1) + getFibonacci(N - 2)
    return memoize[N]
## END


if __name__ == '__main__':
    print("Fibonacci Numbers by Iterative Approach")
    print('1st fibonacci number:', getKthFibonacciNumberIteratively(1))
    print('2nd fibonacci number:', getKthFibonacciNumberIteratively(2))
    print('5th fibonacci number:', getKthFibonacciNumberIteratively(5))
    print('10th fibonacci number:', getKthFibonacciNumberIteratively(10))
    print('20th fibonacci number:', getKthFibonacciNumberIteratively(20))
    print()

    print("Fibonacci Numbers by Recursive Approach")
    print('1st fibonacci number:', getKthFibonacciNumberRecursively(1))
    print('2nd fibonacci number:', getKthFibonacciNumberRecursively(2))
    print('5th fibonacci number:', getKthFibonacciNumberRecursively(5))
    print('10th fibonacci number:', getKthFibonacciNumberRecursively(10))
    print('20th fibonacci number:', getKthFibonacciNumberRecursively(20))
    print()
    
    print("Fibonacci Numbers by Dynamic Programming Approach")
    print('1st fibonacci number:', getKthFibonacciNumberByDynamicProgramming(1))
    print('2nd fibonacci number:', getKthFibonacciNumberByDynamicProgramming(2))
    print('5th fibonacci number:', getKthFibonacciNumberByDynamicProgramming(5))
    print('10th fibonacci number:', getKthFibonacciNumberByDynamicProgramming(10))
    print('20th fibonacci number:', getKthFibonacciNumberByDynamicProgramming(20))

