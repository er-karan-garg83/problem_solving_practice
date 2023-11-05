'''
Date: 05-11-2023
Author: er-karan-garg83

Problem:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto
the end of the merged string. Return the merged string.
'''


def mergeAlternately(word1: str, word2: str) -> str:
    ans = ""
    shortest_string = min([word1, word2], key=len)
    longest_string = max([word1, word2], key=len)
    for i in range(len(shortest_string)):
        ans += word1[i]
        ans += word2[i]
    ans += longest_string[len(shortest_string):]
    return ans


# Sample test-case
print(mergeAlternately('abc', 'pqr'))

'''
Steps:
1. Find the shortest and the longest strings by length and assign to some variables.
2. Start a for loop till the length of the shortest string.
3. Store the alternate letters in a variable (answer or result).
4. Append the left over letters in the longest string to the answer variable.
'''



