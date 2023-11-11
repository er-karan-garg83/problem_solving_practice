'''
Date: 10-11-2023
Author: er-karan-garg83, (took help from ChatGPT to optimize)

Problem:
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.
'''


def findMaxAverage(nums, k):
    win_sum = sum(nums[:k])
    max_avg = win_sum/k

    for i in range(1,len(nums)-k+1):
        win_sum = win_sum - nums[i-1] + nums[i+k-1]
        max_avg = max(max_avg,win_sum/k)
    return max_avg


# Sample test-case
print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
'''
Steps:
1. We are given an array and sliding window size. Find the first window sum and average using python slicing.
2. Then iterate over the array, find the window sum dynamically this by removing the prev element from the first
window sum and adding the new element from right side. (ref line 17).
3. Then using that window sum, find the max average, compare between the first max avg and new one and store it.
4. Finally return the maximum average.
'''



