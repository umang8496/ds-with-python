
# Given two dimensional m by n matrix, 
# write an algorithm to count all possible paths from top left corner to bottom-right corner. 
# You are allowed to move only in two directions, move right OR move down.

# this is a recursive approach
def getNumberOfWays(matrix):
    m, n = matrix[0], matrix[1]
    return countNumberOfWays(m, n)
## END

def countNumberOfWays(m, n):
    if ((m == 0) or (n == 0)):
        return 0
    if ((m == 1) and (n == 1)):
        return 0

    if ((m == 2) and (n == 1)):
        return 1
    if ((m == 1) and (n == 2)):
        return 1

    # make the right move or make the down move
    return countNumberOfWays(m-1, n) + countNumberOfWays(m, n-1)    
## END


if __name__ == '__main__':
    print("Recursive Programming Approach")
    matrix = (1, 1)
    print("Number of ways for (1,1)", getNumberOfWays(matrix))
    matrix = (1, 0)
    print("Number of ways for (1,0)", getNumberOfWays(matrix))
    matrix = (0, 1)
    print("Number of ways for (0,1)", getNumberOfWays(matrix))

    matrix = (2, 2)
    print("Number of ways for (2,2)", getNumberOfWays(matrix))
    matrix = (2, 3)
    print("Number of ways for (2,3)", getNumberOfWays(matrix))

    matrix = (3, 3)
    print("Number of ways for (3,3)", getNumberOfWays(matrix))
    matrix = (4, 4)
    print("Number of ways for (4,4)", getNumberOfWays(matrix))
    matrix = (5, 5)
    print("Number of ways for (5,5)", getNumberOfWays(matrix))
    matrix = (6, 6)
    print("Number of ways for (6,6)", getNumberOfWays(matrix))
    matrix = (7, 7)
    print("Number of ways for (7,7)", getNumberOfWays(matrix))
    matrix = (8, 8)
    print("Number of ways for (8,8)", getNumberOfWays(matrix))
    matrix = (9, 9)
    print("Number of ways for (9,9)", getNumberOfWays(matrix))
    matrix = (10, 10)
    print("Number of ways for (10,10)", getNumberOfWays(matrix))

