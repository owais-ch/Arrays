'''
Find pairs with given relation (GFG)

Given an array of distinct integers, write a program to find if there exist two pairs (a, b) and (c, d) such that ab = cd, where a, b, c and d are distinct elements. If such pairs exists then print 1 else -1.

Example 1:

Input:
N=7
arr[] = {3, 4, 7, 1, 2, 9, 8} 
Output: 1
Explanation:
Product of 4 and 2 is 8 and also,
the product of 1 and 8 is 8.  
'''
class Solution:
    def findPairs(self,arr,n):
        dict1=dict()
        
        for i in range(n-1):
            for j in range(i+1,n):
                product=arr[i]*arr[j]
                if product not in dict1:
                    dict1[product]=1
                else:
                    return 1
                    
        return -1
