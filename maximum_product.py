'''
Maximum product (GFG)

Given an array arr[] of N integers, the task is to find a subsequence of size K whose product is maximum among all possible K sized subsequences of a given array.

Example 1:

Input: N = 4, K = 2
arr[] = {1, 2, 0, 3} 
Output: 6
Explanation: Subsequence containing 
elements {2, 3} gives maximum product: 
2*3 = 6
'''

class Solution:
    def maxProductSubarrayOfSizeK(self,arr, n, k):
        zero_count=arr.count(0)
        for i in range(zero_count):
            arr.remove(0)
        
        n=len(arr)
        if k>n:
            return 0
        arr.sort()
        #print(arr)
        
        count=0
        
        if arr[0]>k:
            for i in range(-1,-k-1,-1):
                if i==-1:
                    product=arr[i]
                else:
                    product*=arr[i]
            return product
        
        product=1
        
        i=-1
        count=0
        
        while count<k:
            product*=arr[i]
            count+=1
            i-=1
        
        max_product=product  
        
        start=-k
        count=0
        j=0
        
        while count<k:
            product=(product*arr[j])//arr[start]
            count+=1
            start+=1
            j+=1
            max_product=max(max_product,product)
        
        if max_product<0 and zero_count>0:
            return 0
        return max_product
