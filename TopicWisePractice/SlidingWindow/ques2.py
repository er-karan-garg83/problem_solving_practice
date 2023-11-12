'''
Date: 12-11-2023
Author: er-karan-garg83

Problem:
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of
the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
You are also given an integer k, which is the desired number of consecutive black blocks.
In one operation, you can recolor a white block such that it becomes a black block.
Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
'''


def minimumRecolors(blocks, k):
    fw = blocks[0:k]
    min_ops = fw.count('W')
    for i in range(1, len(blocks)-k+1):
        w = blocks[i:i+k]
        ops = w.count('W')
        min_ops = min(min_ops,ops)
    return min_ops


# Sample test-case
print(minimumRecolors("WWBBBWBBBBBWWBWWWB", 16))
'''
Steps:
1. Store the first window and the corresponding number of operation required in a variable. Initalize the 
min_ops variable with the operation count of the first window.
2. Iterate over the string, and get the operations count of each iteration and compare it with the min_ops
variable.
3. Return the mininum number of operations as min_ops.
'''



