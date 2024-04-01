'''
Rop Cutting (GFG)
You are given N ropes. A cut operation is performed on ropes such that all of them are reduced by the length of the smallest rope. Display the number of ropes left after every cut operation until the length of each rope is zero.

Example 1:

Input : arr[ ] = {5, 1, 1, 2, 3, 5} 
Output : 4 3 2 
Explanation: In the first operation, the 
minimum ropes are 1 So, we reduce length 1 
from all of them after reducing we left with 
4 ropes and we do the same for rest.
'''

class Solution:
    def RopeCutting (self, arr, n) : 
        arr.sort()
        j=0
        total=n-1
        for i in range(1,n):
            if arr[i]!=arr[i-1]:
                arr[j]=n-i
                j+=1
                
        return arr[:j]
