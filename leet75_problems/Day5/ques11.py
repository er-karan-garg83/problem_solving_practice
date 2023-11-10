'''
Date: 09-11-2023
Author: er-karan-garg83

Problem:
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index
is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.
'''


def pivotIndex(nums):
    left, right = 0, sum(nums)
    for i in range(len(nums)):
        right -= nums[i]
        if left == right:
            return i
        left += nums[i]
    return -1


# Sample test-case
print(pivotIndex([1, 7, 3, 6, 5, 6]))


'''
Steps:
1. This can be done using two pointers. Initializing left and right variables with 0 and sum of array respectively.
2. Iterating over the nums array, decreasing the value of right by each element, and check the equality of left 
and right.
3. If both becomes same, then return that index, else, increase the value of left by each element.
4. If left and right are not equal in any of the iteration, return -1 
'''



