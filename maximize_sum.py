'''
Maximize the sum of selected numbers from a sorted array to make it empty (GFG)

Given a array of N numbers, we need to maximize the sum of selected numbers. At each step, you need to select a number Ai, delete one occurrence of Ai-1 (if exists), and Ai each from the array.
Repeat these steps until the array gets empty. The problem is to maximize the sum of the selected numbers.

Note: Numbers need to be selected from maximum to minimum.

Example 1:

Input : arr[ ] = {1, 2, 2, 2, 3, 4}
Output : 10
Explanation:
We select 4, so 4 and 3 are deleted leaving us with {1,2,2,2}.
Then we select 2, so 2 & 1 are deleted. We are left with{2,2}.
We select 2 in next two steps, thus the sum is 4+2+2+2=10.
'''

from collections import Counter

class Solution:
    
    def maximizeSum (self,arr, n) : 
        arr.sort(key=lambda x:-x)
        
        dict1=Counter(arr)
        dict2=dict1.copy()
        
        start=arr[0]
        total=0
        
        i=0
        count=0
        
        while i<n:
            if start-1 in dict1:
                if dict1[arr[i]]>=dict1[arr[i]-1]:
                    total+=dict1[arr[i]]*arr[i]
                    i=i+dict1[arr[i]]+dict1[arr[i]-1]
                    if i<n:
                        start=arr[i]
                else:
                    total+=(dict1[arr[i]]*arr[i])
                    dict1[arr[i]-1]=dict1[arr[i]-1]-dict1[arr[i]]
                    i=i+2*dict1[arr[i]]
                    if i<n:
                        start=arr[i]
            else:
                total+=(dict1[arr[i]]*arr[i])
                i=i+dict1[arr[i]]
                if i<n:
                    start=arr[i]
            
        return total
                    
