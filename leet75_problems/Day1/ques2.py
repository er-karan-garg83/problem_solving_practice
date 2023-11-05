'''
Date: 05-11-2023
Author: er-karan-garg83

Problem:
For two strings s and t, we say "t divides s" if and only if s = t + ... + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''
from math import gcd


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 == str2 + str1:
        return str1[:gcd(len(str1, ), len(str2))]
    else:
        return ""


# Sample test-case
print(gcdOfStrings('ABCABC', 'ABC'))

'''
Steps:
1. Check whether str1+str2 is equal to str2+str1. If not, return empty string.
2. If the condition in step 1 is passed, then find the GCD (Greatest Common Divisor) of the length of
the input string.
3. Finally, return str1 till the length equal to GCD.
'''