"""
author: Caner Mercan
"""

def knapsack(cap, item_wt, item_val):
    """
    0/1 Knapsack Problem, solved with Dynamic Programming

    """
    # initialize the matrix
    T = [[0]*(cap+1) for _ in range(len(item_wt))]
    for j in range(item_wt[0], len(T[0])):
        T[0][j] = item_val[0]
    
    for i in range(1, len(T)):
        for j in range(1, len(T[0])):
            if j < item_wt[i]:
                # if capacity is less than the current item weight; take the previous T value
                T[i][j] = T[i-1][j]
            else:
                # if capacity is more than the current item weight; do comparison;
                # previous T value or current item value + previous T value without current item
                T[i][j] = max([ T[i-1][j], (item_val[i] + T[i-1][j-item_wt[i]]) ])
    return T

def backtrack(T, item_wt, item_val):
    # start from the end of the matrix.
    i = len(T)-1
    j = len(T[0])-1
    
    # backtrack, add to bag as you 
    bag = {}
    while i > 0:
        if T[i][j] != T[i-1][j]:
            bag[item_wt[i]] = item_val[i]
            j = j-item_wt[i]
        i = i-1
    if j > 0:
        bag[item_wt[i]] = item_val[i]    
    return bag
