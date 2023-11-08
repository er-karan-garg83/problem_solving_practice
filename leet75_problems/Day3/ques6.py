'''
Date: 07-11-2023 (Happy Birthday to me!)
Author: er-karan-garg83, (Akram & Manas helped)

Problem:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''


def moveZeroes(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums


# Sample test-case
print(moveZeroes([0, 1, 0, 3, 12]))


'''
Steps:
1. initialize a new variable 'index' to store the new index of the array.
2. Iterate over the array, check if a value is not equal to zero, then again assign it to the array at 'index'.
3. This way we will be having only non-zero elements in the array, then we just need to add number of zeros 
at the end to complete the length of the array.
4. For the purpose in step 3, iterate over the array again, this time, keep the range from index to the length
of the array. Assign zero to those indices.
4. Finally, return the same array.
'''



