'''
Date: 06-11-2023
Author: er-karan-garg83

Problem:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''


def reverseVowels(s):
    s = list(s)
    v2 = []
    v = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if (i in v):
            v2.append(i)
    v2 = v2[::-1]
    j = 0
    for i in range(len(s)):
        if(s[i] in v):
            s[i] = v2[j]
            j +=1
    res = ''.join(str(i) for i in s)
    return res


# Sample test-case
print(reverseVowels('hello'))

'''
Steps:
1. Convert the string to list, to do operations.
2. Create a list having all the vowels.
3. Iterate over the list and store the vowels present in another list.
4. Reverse the newly created list of vowels in Step 3.
5. Iterate over the main list (s) again and if the iteration is having vowel, just change the element 
with the vowel from list v2.
6. Finally, convert the list to string and return the output.
'''



