'''
Balance with respect to an array (GFG)

As a programmer, it is very necessary to maintain balance in the life.
Here is task for you to maintain a balance. Your task is to find whether a given number x is balanced with respect to a given array a[ ] which is sorted in non-decreasing order.
Given a sorted array a[ ], the ceiling of x is the smallest element in the array greater than or equal to x, and the floor of x is the greatest element smaller than or equal to x. 
The number 'x' is said to be balanced if the absolute difference between floor of x and x is equal to the absolute difference between ceil of x and x i.e. if absolute(x - floor(x, a[])) = absolute(ceil(x, a[]) - x).
If one of floor or ceil does not exist assume 'x' to be balanced.

Example 1:

Input:
N = 7  
x = 5
a[] = {1, 2, 8, 10, 10, 12, 19} 
Output: 
Balanced
Explanation: Here 2 is the floor value and 
8 is the ceil value and (5 - 2) = (8 - 5). 
'''

class Solution:
    def isBalanced(self,arr,n,x):
        low=0
        high=n-1
        count=0
        if x>arr[-1]:
            return "Balanced"
        elif x<arr[0]:
            return "Balanced"
        while low<=high:
            mid=(low+high)//2
            
            if arr[mid]==x or (mid+1<n and arr[mid+1]==x) or (mid-1>=0 and arr[mid-1]==x):
                return "Balanced"
            elif x>arr[mid] and mid+1<n and x>arr[mid+1]:
                low=mid+1
            elif x<arr[mid] and mid-1>=0 and x<arr[mid-1]:
                high=mid-1
            else:
                if mid+1<n and arr[mid]<x<arr[mid+1]:
                    if x-arr[mid]==arr[mid+1]-x:
                       return "Balanced"
                    else:
                        return "Not Balanced"
                elif mid-1>=0 and arr[mid-1]<x<arr[mid]:
                    if x-arr[mid-1]==arr[mid]-x:
                        return "Balanced"
                    else:
                        return "Not Balanced"
                elif arr[mid]==x:
                    return "Balanced"
                else:
                    return "Not Balanced"
           
        return "Not Balanced"
