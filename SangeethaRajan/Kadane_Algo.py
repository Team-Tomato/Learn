a = [3, 4, -1, 12, -9]
def Kadane_Algo(a, n):
    maxsum = a[0]
    tempsum= a[0]
    for i in range(1, n):
        maxsum = max(a[i], maxsum + a[i])
        if maxsum > tempsum:
            tempsum = maxsum
    return tempsum
print("Maximum sum of subarray:",Kadane_Algo(a, len(a)))