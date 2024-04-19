'''
Equivalent subarrays (GFG)
Given an array arr[] of n integers. Count the total number of sub-array having total distinct elements same as that of total distinct elements of the original array.

Example 1:

Input:
N=5
arr[] = {2, 1, 3, 2, 3} 
Output: 5
Explanation:
Total distinct elements in array is 3
Total sub-arrays that satisfy the condition
are:
Subarray from index 0 to 2
Subarray from index 0 to 3
Subarray from index 0 to 4
Subarray from index 1 to 3
Subarray from index 1 to 4
'''
class Solution:
    def countDistinctSubarray(self,arr, n): 
        set1=set(arr)
        
        num_distinct=len(set1)
        
        dict1=dict()
        
        i,j=0,0
        
        total=0
        count=0
        
        while i<n-num_distinct+1:
            if count==num_distinct:
                total+=(n-j+1)
            else:
                while j<n:
                    if arr[j] not in dict1:
                        dict1[arr[j]]=1
                        count+=1
                        if count==num_distinct:
                            total+=(n-j)
                            j+=1
                            break
                    else:
                        dict1[arr[j]]+=1

                    j+=1
            
            dict1[arr[i]]-=1
            if dict1[arr[i]]==0:
                dict1.pop(arr[i])
                count-=1
            
            i+=1
        
        return total
