def maxsumsubarr(arr, n):
    current_max = arr[0]
    max_so_far = arr[0]
    for i in range(1, n):
        current_max = max(arr[i], current_max + arr[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far


arr = [-3, 4, 1, 2, -1, -4, 3]
print("Maximum sub-array sum is:", maxsumsubarr(arr, len(arr)))
