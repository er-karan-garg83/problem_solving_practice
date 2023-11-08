'''
Date: 07-11-2023 (Happy Birthday to me!)
Author: er-karan-garg83, (Manas & Akash helped)

Problem:
Given an input string s, reverse the order of the words. A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
'''


def reverseWords(s):
    #one line solution
    # return ' '.join([elem.strip(" ") for elem in s.strip(" ").split(" ")[::-1] if elem != ""])

    #explained
    s = [elem.strip(" ") for elem in s.strip(" ").split(" ")[::-1] if elem != ""]
    s = ' '.join(s)
    return s


# Sample test-case
print(reverseWords("  hello world  "))


'''
Steps:
1. I have used list comprehension here to complete it in one line.
2. Convert the string to list using .strip and .split, to make sure to trialing and leading spaces should 
be there.
3. Reversed the list, then check if the element is not an empty string, then strip it.
4. Finally, join the list to string, and return it.
'''



