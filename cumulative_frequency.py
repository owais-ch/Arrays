'''
Cumulative frequency of count of each element in an unsorted array

Given an array of elements. The task is to calculate the cumulative frequency of each element of the array.

Note :- Cumulative frequency should be taken according to the sorted order of elements.

Example 1:

Input : Arr[] = {1, 2, 2, 1, 3, 4}
Output : 2 4 5 6
Explanation:
Here we have an array arr[] = [1, 3, 2, 
                               1, 2, 4]
Output :1->2
        2->4
        3->5
        4->6
So, the return array will have [2, 4, 5, 6] 
as an output.
'''

class Solution:
    def countFreq(self, a, n):
        a.sort()
        
        start=1
        j=0
        
        for i in range(1,n):
            if a[i]==a[i-1]:
                start+=1
            else:
                a[j]=start
                start+=1
                j+=1
        a[j]=start
        j+=1
        return a[:j]
