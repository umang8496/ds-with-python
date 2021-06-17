# Given an array A[] consisting 0s, 1s and 2s. 
# The task is to write a function that sorts the given array. 
# The functions should put all 0s first, then all 1s and all 2s in last.

# Input: {0, 1, 2, 0, 1, 2}
# Output: {0, 0, 1, 1, 2, 2}

# Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}


def sortZeroOneAndTwo(arr):
    l = 0
    m = 0
    h = (len(arr) - 1)
    while(m <= h):
        if (arr[m] == 0):
            swap = arr[l]
            arr[l] = arr[m]
            arr[m] = swap
            l += 1
            m += 1
        elif (arr[m] == 1):
            m += 1
        else:
            swap = arr[h]
            arr[h] = arr[m]
            arr[m] = swap
            h -= 1
    ## END
    return arr
## END


if __name__ == '__main__':
    # arr = [0, 1, 2, 0, 1, 2]
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(sortZeroOneAndTwo(arr))
