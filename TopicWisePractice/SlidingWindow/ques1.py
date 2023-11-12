'''
Date: 12-11-2023
Author: er-karan-garg83

Problem:
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that
meet the following conditions:
- It has a length of k.
- It is a divisor of num.
Given integers num and k, return the k-beauty of num.
'''


def divisorSubstrings(num, k):
    s = str(num)
    count = 0
    for i in range(len(s)-k+1):
        w = int(s[i:i+k])
        if num % w == 0:
            count += 1
    return count


# Sample test-case
print(divisorSubstrings(240, 2))
'''
Steps:
1. Convert the number num to string s.
2. Iterate over the string s, for each iteration, create a sliding window, and check if it is a divisor of 
num or not. If yes, increase the count by 1.
3. Finally return count.
'''



