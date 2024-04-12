'''
Count_number (GFG)
Given an array arr consisting of integers of size n and 2 additional integers k and x, you need to find the number of subsets of this array of size k, where Absolute difference between the Maximum and Minimum number of the subset is at most x.

Note: As this number that you need to find can be rather large, print it Modulo 109+7

Example 1:

Input:
n = 5, k = 3, x = 5
arr[] = {1, 2, 3, 4, 5}
Output:
10
Explanation :
Possible subsets of size 3 are :-
{1,2,3} {1,2,4} {1,2,5} {1,3,4}
{1,3,5} {1,4,5} {2,3,4} {2,3,5}
{2,4,5} {3,4,5} having difference
of maximum and minimum
element less than equal to 5.
'''

import math
def getAnswer( arr, n, k, x):
    arr.sort()
    
    j=0
    total=0
    i=0
    lastj=0
    while i<n-k+1:
        while j<n:
            if arr[j]-arr[i]<=x:
                j+=1
            else:
                break
        
        if i==0:
            count2=0
            lastj=j
        else:
            count2=lastj-i
            
        count=j-i
        
        if count2>=k:
            extra=math.factorial(count2)//(math.factorial(k)*math.factorial(count2-k))
        else:
            extra=0
        
        if count>=k:
            total+=(math.factorial(count)//(math.factorial(k)*math.factorial(count-k))-extra)
        
        lastj=j
        
        i+=1
        
    return total%(10**9+7)
