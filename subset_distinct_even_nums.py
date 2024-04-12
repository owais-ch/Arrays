'''
Count subsets having distinct even numbers (GFG)

Given a set of n numbers. The task is to count all the subsets of the given set which only have even numbers and all are distinct.
Note: By the property of sets, if two subsets have the same set of elements then they are considered as one. For example: [2, 4, 8] and [4, 2, 8] are considered to be the same.
 
Example 1:

Input : 
n = 8
a[] = {4, 2, 1, 9, 2, 6, 5, 3}
Output : 
7
Explanation:
The subsets are:
[4], [2], [6], [4, 2],
[2, 6], [4, 6], [4, 2, 6]
'''

import math

def countSubsets(arr, n):
    set1=set()
    
    for i in range(n):
        if arr[i]%2==0:
            set1.add(arr[i])
            
    length=len(set1)
    
    total=0
    
    j=1
    
    for i in range(1,length+1):
        total+=math.factorial(length)//(math.factorial(i)*math.factorial(length-i))
    
    return total
    
