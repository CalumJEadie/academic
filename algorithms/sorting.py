#! /usr/bin/python

"""
Functions implementing algorithms for Algorithms I - Sorting.
"""

import random

def binaryInsertSort(a):
    """BEHAVOIR: Run the binary sort algorithm on the integer array a, sorting it in place.
    
    PRECONDITION: Array a contains len(a) integer values.
    
    POSTCONDITION: Array a contains the same integer values as before, but now they are sorted in ascending order."""
    
    for k in range(len(a)):
        # ASSERT: The array positions before a[k] are already sorted.
        
        # Perform binary search on a[0:k] to find location to insert a[k].
        lowerLimit = 0 # lower limit of search region
        upperLimit = k # upper limit of search region
        while upperLimit > lowerLimit+1:
            mOffset = (upperLimit-lowerLimit)/2
            if a[k] < a[lowerLimit+mOffset]:
                upperLimit = lowerLimit+mOffset
            else:
                lowerLimit = lowerLimit+mOffset
            
        # Base case. Region is a single element of array.
        if a[k] < a[lowerLimit]:
            insertPos = lowerLimit
        else:
            insertPos = upperLimit

        # Put a[k] in position insertPos. Unless it's already there, this means right
        # shifting by one every other item in a[i:k].
        if insertPos != k:
            tmp = a[k]
            for j in range(k-1,insertPos,-1):
                a[j+1] = a[j]
            a[insertPos] = tmp

def mergeSort(a):            
    """BEHAVIOUR: Run the merge sort algorithm on the integer array a, sorting it in place.

    PRECONDITION: Array a contains len(a) integer values.

    POSTCONDITION: Array a contains the same
    integer values originally in a, but sorted in ascending order."""
    
    mergeSortSubArray(a,0,len(a))
            
def mergeSortSubArray(a,lowerLimit,upperLimit):
    """BEHAVIOUR: Run the merge sort algorithm on the integer array a[lowerLimit:upperLimit], sorting it in place.

    PRECONDITION: Array a[lowerLimit:upperLimit] contains len(a) integer values.

    POSTCONDITION: Array a[lowerLimit:upperLimit] contains the same
    integer values originally in a, but sorted in ascending order."""
    
    # Don't need to modify array of length one as already sorted.
    if upperLimit == lowerLimit+1:
        return
    
    # Divide problem into sorting two sub arrays.
    mOffset = (upperLimit-lowerLimit)/2
    mergeSortSubArray(a,lowerLimit,lowerLimit+mOffset)
    mergeSortSubArray(a,lowerLimit+mOffset,upperLimit)
        
    # Merge the sub arrays together.
    tmp = [0]*(upperLimit-lowerLimit)
    aLowerIndex = lowerLimit
    aUpperIndex = lowerLimit+mOffset
    tmpIndex = 0
    while aLowerIndex<mOffset or aUpperIndex<upperLimit:
        print a
        # ASSERT: tmpIndex < upperLimit-lowerLimit
        # Insert the next smallest value in the sub arrays into the tmp array.
        # Add from lower sub array if next smallest could come from either to preserver
        # order in original array.
        if a[aUpperIndex] > a[aLowerIndex]:
            tmp[tmpIndex] = a[aUpperIndex]
            aUpperIndex += 1
        else:
            tmp[tmpIndex] = a[aLowerIndex]
            aLowerIndex += 1
        tmpIndex += 1
    # ASSERT: tmpIndex = upperLimit-lowerLimit
    a[lowerLimit,upperLimit] = tmp
    
def quicksort(a):
    """BEHAVOIR: Run the quicksort algorithm on the integer array a, sorting it in place.
    
    PRECONDITION: a contains len(a) integer values.
    
    POSTCONDITION: a contains the same integer values originally in a, but sorted in ascending order."""
    quicksortSlice(a,0,len(a)-1)
    
def quicksortSlice(a,l,u):
    """BEHAVOIR: Run the quicksort algorithm on the integer array slice a[l:u], sorting it in place.
    
    PRECONDITION: a[l:u] contains len(a[l:u]) integer values.
    
    POSTCONDITION: a[l:u] contains the same integer values originally in a[l:u], but sorted in ascending order."""
    
    if l < u:
        q = partition(a,l,u) #a[q] is the pivot element
        quicksortSlice(a,l,q)
        quicksortSlice(a,q+1,u)
    
def partition(a,l,u):
    x = a[u-1]
    i = l-1
    for j in range(l,u-1):
        pd([('l',l),('u',u),('i',i),('j',j),('a',a)])
        if a[j] <= x:
            # a[j] <= x so the size of the <= partition will increase
            i += 1
            swap(a,i,j)
        # Whether a[j] <= x and the size of the <= partition increases or whether
        # a[j] > x and the size of the > partition increases the upper limit of the
        # >= partition will shift one place to the right.
        pd([('l',l),('u',u),('i',i),('j',j),('a',a)])
    # After partitioning move pivot into it's correct position.
    swap(a,i+1,u-1)
    pd([('a',a)])
    return i+1
            
def swap(a,i,j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
            
def test(sortMethod,n=1000):
    a = random.sample(range(1000),n)
    print a
    sortMethod(a)
    print a
    
def pd(vars):
    for (varName,varContent) in vars:
        print varName+":"
        print varContent
