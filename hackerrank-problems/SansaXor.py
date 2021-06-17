
# https://www.hackerrank.com/challenges/sansa-and-xor/problem

def sansaXor(arr):
    xor_result = 0
    N = len(arr)

    if(N % 2 == 0):
        return 0
    else:
        for i in range(0, N, 2):
            xor_result = xor_result ^ arr[i]
    return xor_result
# END


if __name__ == "__main__":
    #arr = [1,2,3]
    arr = [4, 5, 7, 5]
    result = sansaXor(arr)

    print(result)
