
# https://www.hackerrank.com/challenges/between-two-sets/problem

import math

def getTotalX(A, B):
	lcmOfA = LcmOfArray(A)
	gcdOfB = GcdOfArray(B)
	divisorsForB = []
	count = 0

	# print("A:", A, "LCM:", lcmOfA)
	# print("B:", B, "GCD:", gcdOfB)

	for F in range(lcmOfA, gcdOfB+1):
		is_F_a_factor = True
		for ele in B:
			eval = (ele % F)
			if(eval != 0):
				is_F_a_factor = False
		if (is_F_a_factor):
			divisorsForB.append(F)
	# print("divisorsForB:", divisorsForB)

	integersToBeReturned = []
	for D in divisorsForB:
		is_D_a_divisor = True
		for ele in A:
			eval = (D % ele)
			if(eval != 0):
				is_D_a_divisor = False
				break
		if (is_D_a_divisor):
			integersToBeReturned.append(D)
	# print("integersToBeReturned:", integersToBeReturned)

	return len(integersToBeReturned)
## END

    
def LcmOfArray(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        lcm = lcm*arr[i]//math.gcd(lcm, arr[i])
    return lcm
## END


def GcdOfArray(arr):
    gcd = arr[0]
    for i in range(1,len(arr)):
        gcd = math.gcd(gcd, arr[i])
    return gcd
## END


if __name__ =="__main__":
	# a = [2, 6]
	# b = [24, 36]
	# should return 2

	# a = [2, 4]
	# b = [16, 32, 96]
	# should return 3

	# a = [3, 4]
	# b = [24, 48]
	# should return 2

	a = [1]
	b = [20, 30, 12]
	# should return 1

	# a = [51]
	# b = [50]
	# should return 0

	# a = [1]
	# b = [100]
	# should return 9
	
	print(getTotalX(a,b))

