def kadane_algo(A):
	max_all = 0
	curr_max= 0
	for i in A:
		curr_max = curr_max + i
		curr_max= max(curr_max, 0)
		max_all = max(max_all,curr_max)
	return max_all

if __name__ == '__main__':
	A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	print("The largest sum is",kadane_algo(A))

