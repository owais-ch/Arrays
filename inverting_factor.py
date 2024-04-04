'''
The Inverting Factor (GFG)
Ishaan being curious as always was playing with numbers when he started to reverse the numbers. He invented something called the "inverting factor" of two numbers.
The inverting Factor of 2 integers is defined as the absolute difference between the reverse of the 2 integers.
Ishaan has an array A of N integers. He wants to find out the smallest possible Inverting Factor among all pairs of his integers. Help him find that.
Note : Trailing zeros in a number of ignored while reversing, i.e. 1200 becomes 21 when reversed.

Example 1:

â€‹Input : arr[ ] = {56, 20, 47, 93, 45}
Output : 9
Explanation:
The minimum inverting factor is 9, of the pair (56,47)
Reverse 56 -> 65 and 47 -> 74
difference between them is 9.
'''

import math

def findMinimumInvertingFactor (arr, n) : 
    minimum=math.inf
    list1=[]
    for i in range(n):
        arr[i]=int(str(arr[i])[::-1])
       
    arr.sort()
    
    for i in range(1,n):
        minimum=min(minimum,arr[i]-arr[i-1])
    
    return minimum
