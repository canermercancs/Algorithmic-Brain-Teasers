"""
author: Caner Mercan

"""

import math

def reduceNto1(n):
    """
    Find minimum number of operations that reduces a given number to one;
    ops are:
    i) decrease by 1
    ii) divide by 2
    iii) divide by 3
    """
    if n == 1:
        return 0
    if n < 0:
        return -1

    # def f(arr, n):
    #     if n<1:
    #         return math.inf
    #     if n != int(n):
    #         return math.inf
    #     if n==1:
    #         return 0
    #     n = int(n)
        
    #     if arr[n-1] != -1:
    #         return arr[n-1]
    #     arr[n-1] = 1+min([f(arr, n-1), f(arr, n/2), f(arr, n/3)])
    #     return arr[n-1]

    def f(n):
        #global arr
        if n<1:
            return math.inf
        if n != int(n):
            return math.inf
        if n==1:
            return 0
        n = int(n)
        
        if arr[n-1] != -1:
            return arr[n-1]
        arr[n-1] = 1+min([f(n-1), f(n/2), f(n/3)])
        return arr[n-1]

    global arr
    arr = [-1] * n     
    return f(n)



def climb_stairs(n):
    """
    Find the number of ways a person can climb stairs with 1,2,3 steps at a time.
    """
    if n <= 0:
        return -1
    
    def f(arr, n):
        if n < 0:
            return 0
        if n <= 1:
            return 1

        if arr[n-1] != -1:
            return arr[n-1]
        arr[n-1] = f(arr, n-1) + f(arr, n-2) + f(arr, n-3)
        return arr[n-1]

    arr = [-1] * n
    return f(arr, n)

