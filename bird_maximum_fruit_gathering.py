'''
There are N trees in a circle. Each tree has a fruit value associated with it. A bird has to sit on a tree for 0.5 sec to gather all the fruits present on the tree and then the bird can move to a neighboring tree. 
It takes the bird 0.5 seconds to move from one tree to another. Once all the fruits are picked from a particular tree, she can’t pick any more fruits from that tree. The maximum number of fruits she can gather is infinite.

Given N and M (the total number of seconds the bird has), and the fruit values of the trees. Maximize the total fruit value that the bird can gather. The bird can start from any tree.

Example 1:

Input:
N=7 M=3
arr[] = { 2 ,1 ,3 ,5 ,0 ,1 ,4 }
Output: 9
Explanation: 
She can start from tree 1 and move
to tree2 and then to tree 3.
Hence, total number of gathered fruits
= 1 + 3 + 5 = 9.
'''

class Solution:
    def maxFruits(self,arr,n,m):
        total=sum(arr[:m])
        maximum=total
        
        for i in range(1,n-m+1):
            total=total-arr[i-1]+arr[i+m-1]
            if total>maximum:
                maximum=total
            
        left=1
        right=n-m+1
        left_total=arr[0]
        right_total=sum(arr[right:])
        
        while left<m:
            maximum=max(maximum,left_total+right_total)
            left_total=left_total+arr[left]
            right_total=right_total-arr[right]
            left+=1
            right+=1
        return maximum
