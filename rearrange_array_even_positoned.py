'''
Rearrange array such that even positioned are greater than odd (GFG)

Given an array A of n elements, rearrange the array according to the following relations :
A[i] >= A[i-1], if i is even.
A[i] <= A[i-1], if i is odd.[Considering 1-indexed array]
Return the resultant array.

Example:

Input 1:
A[] = {1, 2, 2, 1}
Output:
1 2 1 2
Explanation:
Both 2 are at even positions and 1 at odd satisfying 
given condition 
'''
class Solution:
    def assign (self, arr,  n) : 
        arr.sort()
        
        if n%2==0:
            mid=n//2
        else:
            mid=n//2+1
            
        start=1
        index=mid
        for i in range(1,mid):
            arr[start],arr[index]=arr[index],arr[start]
            start+=2
            index+=1
        
        return arr
