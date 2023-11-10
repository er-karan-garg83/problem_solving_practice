'''
Date: 09-11-2023
Author: er-karan-garg83

Problem:
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''


def largestAltitude(gain):
    n = len(gain)
    arr = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        arr[i] = arr[i - 1] + gain[i - 1]
    return max(arr)


# Sample test-case
print(largestAltitude([-5, 1, 5, 0, -7]))

'''
Steps:
1. This question can be done using Prefix Sum. Create a new array with zero as all the elements, and keep
the size same as that of gain array.
2. No, iterate over both the arrays, starting from 1, assign elements to the new array by adding prefix sum
of the gain array.
3. Finally check the maximum element of the new array and return the same.
'''



