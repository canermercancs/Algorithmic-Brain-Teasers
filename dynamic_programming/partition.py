"""
author: Caner Mercan
"""


def equalSums(arr):
    """
    Can an array be divided into two parts whose sum are equal?
    """
    sum_arr = 0
    
    # O(n) time
    for a in arr:
        sum_arr += a
    if sum_arr%2 == 1:
        return False
    
    # O(sum_arr) space
    T = [True] + [False] * (sum_arr-1) # idx i is True if sum of two or more values in arr equals to i
    
    for i,a in enumerate(arr):
        comp_a = sum_arr - a
        for t in range(comp_a,-1,-1):
            if T[t]:
                T[t+a] = True
                if t+a == sum_arr/2: # stop when the index is exactle at the half of len(T)
                    return True
    return False