'''
Date: 08-11-2023
Author: er-karan-garg83

Problem:
Given an array of integers arr,return true if the number of occurrences of each value in the array
is unique or false otherwise.
'''


def uniqueOccurrences(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    lv = d.values()
    lvs = set(lv)
    if len(lvs) < len(lv):
        return False
    else:
        return True


# Sample test-case
print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))

'''
Steps:
1. Iterating over the array and storing the occurences of the elements in a dictionary.
2. Storing the values of the dictionary in a list.
3. Create a set of the dict values list.
4. Compare the lengths of the the values list and set.
5. If the length of set is less than the list, then it means there are elements present with the same 
number of occurences, return False otherwise True.
'''



