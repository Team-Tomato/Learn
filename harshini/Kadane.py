
def kadane(A):
	max_current = max_global = A[0]
	for i in range(len(A)-1):
		max_current = max(A[i],max_current+A[i])
		if max_current > max_global:
			max_global = max_current
			#print (max_current,max_global)

	return max_global

A = [-2, -3, 4, -1, -2, 1, 5, -3]  

print (kadane(A))



