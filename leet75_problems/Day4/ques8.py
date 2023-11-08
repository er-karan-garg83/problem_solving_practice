'''
Date: 08-11-2023
Author: er-karan-garg83

Problem:
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''


def findDifference(nums1, nums2):
    return [set(nums1) - set(nums2), set(nums2) - set(nums1)]


# Sample test-case
print(findDifference([1, 2, 3], [2, 4, 6]))

'''
Steps:
1. Using set in python, we can find the unique elements between two lists by using '-' operator.
2. Simple returned the output in list.
'''



