
# https://www.codechef.com/problems/VNRCF01

def canTheTargetBeReachable(N, numbers):
    if (N == 0):
        return True
    if (N < 0):
        return False
    
    for f in numbers:
        if(canTheTargetBeReachable(N-f, numbers) == True):
            return True
    
    return False

if __name__ == '__main__':
    # targetSum = 7
    # numbers = [5, 3, 4, 7]
    targetSum = 10
    numbers = [2, 5, 3, 6]
    print(canTheTargetBeReachable(targetSum, numbers))

