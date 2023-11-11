'''
Date: 11-11-2023
Author: er-karan-garg83

Problem:
Given a string s and an integer k, return the maximum number of vowel letters in any substring of
s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
'''


def maxVowels(s, k):
    v = 'aeiou'
    max_vow = 0
    for i in range(len(s)-k+1):
        w = s[i:i+k]
        count = sum(w.count(vow) for vow in v)
        max_vow = max(count, max_vow)
    return max_vow


# Sample test-case
print(maxVowels('abciiidef', 3))

'''
Steps:
1. create a string variable having all the vowels lowercase (as per problem).
2. initialize a variable to store the maximum vowel count.
3. Iterate over the sliding window, store the dynamic sliding window string in a variable.
4. Store the count of vowels in each window in a variable.
5. Finally, compare the count with maximum vowel count and return it.
'''



