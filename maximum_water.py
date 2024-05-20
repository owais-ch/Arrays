'''
Maximum Water Between Two Buildings

Given an integer array representing the heights of N buildings, the task is to delete N-2 buildings such that the water that can be trapped between the remaining two building is maximum.
Note: The total water trapped between two buildings is gap between them (number of buildings removed) multiplied by height of the smaller building.

Example 1:

Input:
N = 6
height[] = {2,1,3,4,6,5}
Output: 8
Explanation: The heights are 2 1 3 4 6 5.
So we choose the following buildings
2,5  and remove others. Now gap between 
two buildings is equal to 4, and the
height of smaller one is 2. So answer is
2 * gap = 2*4 = 8. There is
no answer greater than this.
Example 2:
'''

class Solution:
    #Function to return the maximum water that can be stored.
    def maxWater(self, height, n): 
        i,j=0,n-1
        maximum=0
        
        while i<j:
            volume=min(height[i],height[j])*(j-i-1)
            if volume>maximum:
                maximum=volume
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
                
        return maximum
