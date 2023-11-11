# Sliding Window implementation:

arr = [1, 12, 36, 78, 96]
k = 3
n = len(arr)
for i in range(n-k+1):
    w = arr[i:i+k]
    print(w)
