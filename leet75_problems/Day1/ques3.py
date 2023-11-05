'''
Date: 05-11-2023
Author: er-karan-garg83

Problem:
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
'''


def kidsWithCandies(candies, extraCandies):
    maxi = max(candies)
    result = []
    for i in range(len(candies)):
        if (candies[i] + extraCandies) >= maxi:
            result.append(True)
        else:
            result.append(False)
    return result


# Sample test-case
print(kidsWithCandies([2, 3, 5, 1, 3], 3))

'''
Steps:
1. Calculate the maximum number of the array and store it in a variable.
2. Iterate over the candies array and check in each iteration that whether after adding extraCandies, the 
number is greater than the maximum of array or not. 
3. Store the result of each iteration in a result array with boolean values.
'''



