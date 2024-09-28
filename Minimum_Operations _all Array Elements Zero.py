'''
Minimum no. of operations required to make all Array Elements Zero (GFG)

Last Updated : 02 Sep, 2022
Given an array of N elements and each element is either 1 or 0. You need to make all the elements of the array equal to 0 by performing the below operations:

If an element is 1, You can change it’s value equal to 0 then, 
if the next consecutive element is 1, it will automatically get converted to 0.
if the next consecutive element is already 0, nothing will happen.
Now, the task is to find the minimum number of operations required to make all elements equal to 0.

Examples:  

Input : arr[] = {1, 1, 0, 0, 1, 1, 1, 0, 0, 1} 
Output : Minimum changes: 3 

Input : arr[] = {1, 1, 1, 1}
Output : Minimum changes: 1 
'''

class Solution:
    def make_arr_zero(self,arr,n):
        count=0
        for i in range(n):
            if arr[i]==1 and (i==0 or arr[i-1]==0):
                count+=1


        return count
