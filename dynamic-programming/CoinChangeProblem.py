
# https://www.hackerrank.com/challenges/coin-change/problem


####################################################################################################
# finds the number of all the distinct ways (while preserving the order) of reaching the target sum recursively
####################################################################################################
def getTheDistinctNumberOfWays(N, numbers):
    count = []
    result = recursivelyCountTheNumbers(N, numbers, count)
    return sum(result)

def recursivelyCountTheNumbers(N, numbers, count):
    if (N == 0):
        count.append(1)
        return 1
    if (N < 0):
        return 0

    for f in numbers:
        recursivelyCountTheNumbers(N-f, numbers, count)
    return count


####################################################################################################
# finds the number of all the distinct ways (without preserving the order) of reaching the target sum recursively
####################################################################################################
def getNumberOfWays(N, numbers):
    return countTheWays(N, numbers, len(numbers)-1)

# N: given target sum
# numbers: given coin denominations
# index: last index value of the denominations array
def countTheWays(N, numbers, index):
    if (N == 0): return 1
    if ((N < 0) or (index < 0)): return 0

    # include the current coin and reduce the required target-sum and proceed further with the same number of coins
    incl = countTheWays(N - numbers[index], numbers, index)
    # exlude the current coin and do not reduce the required target-sum and then proceed with the remaining coins
    excl = countTheWays(N, numbers, index - 1)
 
    return incl + excl


####################################################################################################
# finds the number of all the distinct ways (without preserving the order) 
# of reaching the target sum recursively using the dynamic programming method
####################################################################################################
def getNumberOfWaysUsingLookup(N, numbers):
    lookup = {}
    return countTheWaysUsingLookup(N, numbers, len(numbers)-1, lookup)

# N: given target sum
# numbers: given coin denominations
# index: last index value of the denominations array
def countTheWaysUsingLookup(N, numbers, index, lookup):
    if (N == 0): return 1
    if ((N < 0) or (index < 0)): return 0

    key = (index, N)

    if key not in lookup:
        # include the current coin and reduce the required target-sum and proceed further with the same number of coins
        incl = countTheWaysUsingLookup(N - numbers[index], numbers, index, lookup)
        
        # exlude the current coin and do not reduce the required target-sum and then proceed with the remaining coins
        excl = countTheWaysUsingLookup(N, numbers, index - 1, lookup)
        
        # assign total ways by including or excluding current coin
        lookup[key] = incl + excl

    # return solution to the current subproblem
    return lookup[key]

####################################################################################################
if __name__ == '__main__':
    # targetSum = 7
    # numbers = [5, 3, 4, 7]

    targetSum = 10
    numbers = [2, 5, 3, 6]
    
    # targetSum = 3
    # numbers = [1, 2]
    
    # print(getTheDistinctNumberOfWays(targetSum, numbers))
    # print(getNumberOfWays(targetSum, numbers))
    print(getNumberOfWaysUsingLookup(targetSum, numbers))

####################################################################################################

