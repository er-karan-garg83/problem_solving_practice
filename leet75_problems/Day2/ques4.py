'''
Date: 06-11-2023
Author: er-karan-garg83

Problem:
You have a long flowerbed in which some of the plots are planted, and some are not.
 However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
 return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
 rule and false otherwise.
'''


def canPlaceFlowers(flowerbed, n):
    c = 0
    if (n == 0):
        return True
    if len(flowerbed) == 1:
        if (flowerbed[0] == 1):
            return False
        else:
            return True
    for i in range(len(flowerbed)):
        if (flowerbed[i] == 1):
            continue
        else:
            if (i == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                c += 1
            elif (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0):
                flowerbed[i] = 1
                c += 1
            elif (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                c += 1
    if c >= n:
        return True
    else:
        return False


# Sample test-case
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))

'''
Steps:
1. Check if n=0, if yes, then directly return True as it is the possible scenerio.
2. Check if the length of the array is equal to 1, if yes then check if that element value, if 1 return True
otherwise return False. (It is pre-assumed that n is greater than 1 as we already crossed the 1st condition
(step1)).
3. Now iterate over the flowerbed array, check if the value at that index is 1, then skip that iteration, 
otherwise check the previous and following elements, if both are zero, increase the count value.
4. Finally, check if the value of count is greater than or equal to n, return True otherwise False.
'''



