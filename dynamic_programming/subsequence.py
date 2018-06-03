"""
author: Caner Mercan
"""

def lis(arr):    
    """
    LONGEST INCREASING SUBSTRING/SUBSEQUENCE in O(nlogn)
    loop over the array only once; 
        list (T) for the positions of the current longest increasing subsequence 
        Precedence list (P) to denote the subsequent values in the increasing subsequence. 
    P is crucial as the values of T will often be overridden with new values.
    T is kept sorted;
        A new value greater than T[0] and less than T[-1] will be settled 
        to its position using binary search on T.

    """
    T = [0]
    P = [-1] * len(arr)
    t = 0
    # loop over the array
    for i in range(1, len(arr)):
        val = arr[i]
        # if array value is less than the smallest value in the substring
        if val < arr[T[0]]:
            T[0] = i
        # if array value is greater than the smallest value in the substring    
        elif val > arr[T[t]]:
            t += 1
            T.append(i)
            P[i] = T[-2]
        # if array value is greater than the smallest and less than the greatest value in the substring
        else:
            idx = binaryPositionSearch([arr[i] for i in T], val)
            T[idx] = i if idx != -1 else T[idx]
            P[i] = T[idx-1]

    # backtrack the longest subsequence using the precedence list.
    idx = T[-1] 
    subseq = [0]*(len(T)-1)+[arr[idx]]
    for i in range(len(T)-2,-1,-1):
        idx = P[idx]
        subseq[i] = arr[idx]

    return subseq, T, P

def binaryPositionSearch(T, val):
    return binaryPositionSearch_(T, 0, len(T)-1, val)
def binaryPositionSearch_(T, i, j, val):
    if i>=j: 
        return -1
    mid = (i+j)//2
    if T[mid] < val and val <= T[mid+1]:
        return mid+1
    if val < T[mid]:
        return binaryPositionSearch_(T, i, mid, val)
    return binaryPositionSearch_(T, mid+1, j, val)



