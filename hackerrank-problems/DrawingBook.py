
# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(N, P):
	odd_num_series = [i for i in range(1, N+1, 2)]
	length_of_odd_num_series = len(odd_num_series)
	diff_from_start = P
	diff_from_last = N-P
	
	# N = 11
	# [1, 3, 5, 7, 9, 11]

	default_counter = 0
	counter = 0
	print(diff_from_start > diff_from_last)

	# count from the ending
	if (diff_from_start > diff_from_last):
		if (isEven(N)): # N is even
			for f in range(length_of_odd_num_series-1, -1, -1):
				counter += 1
				if ((odd_num_series[f] - P == 1) or (odd_num_series[f] - P == 0)):
					return counter
		else: # N is odd
			for f in range(length_of_odd_num_series-1, -1, -1):
				if ((odd_num_series[f] - P == 1) or (odd_num_series[f] - P == 0)):
					return counter
				counter += 1
	# count from the beginning
	else:
		for f in range(0, length_of_odd_num_series):
			if ((odd_num_series[f] - P == 1) or (odd_num_series[f] - P == 0)):
				return counter
			counter += 1
	# if the control reaches to this point
	# it means we are either at the start or end of the book
	# hence go for default_counter
	return default_counter
## END		

def isEven(N):
	return (N % 2 == 0)
## END


if __name__ == "__main__":
	# print(pageCount(6, 4)) # should return 1
	# print(pageCount(5, 4)) # should return 0
	# print(pageCount(11, 8)) # should return 1
	# print(pageCount(12, 8)) # should return 2

	# print(pageCount(11, 4)) # should return 2
	# print(pageCount(11, 2)) # should return 1
	# print(pageCount(12, 4)) # should return 2	
	# print(pageCount(12, 2)) # should return 1	

	# print(pageCount(12, 1)) # should return 0
	# print(pageCount(11, 1)) # should return 0

	# print(pageCount(12, 12)) # should return 0
	# print(pageCount(12, 10)) # should return 0
	# print(pageCount(11, 11)) # should return 0
	# print(pageCount(11, 10)) # should return 0
	
	# print(pageCount(6, 3)) # should return 1
	print(pageCount(2, 1)) # should return 1
