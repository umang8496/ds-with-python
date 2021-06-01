
# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(arr):
	N = len(arr)
	counter = 0
	for f in range(N):
		if (arr[f] == -1):
			continue
		for k in range(f+1, N):
			if (arr[k] == -1):
				continue
			if (arr[f] == arr[k]):
				counter += 1
				arr[f] = -1
				arr[k] = -1
				break
	return counter


if __name__ == "__main__":
	arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
	# should return 3

	print(sockMerchant(arr))

