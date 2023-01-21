'''
Given an array Arr[] of size N. Find the number of subarrays whose sum is an even number.

N = 6
Arr[] = {1, 2, 2, 3, 4, 1}
Output: 9
'''

class Solution:
    def countEvenSum(self, arr, n):
        even=0
        odd=0
        
        sum1=0
        
        for i in range(n):
            sum1+=arr[i]
            
            if sum1%2==0:
                even+=1
            else:
                odd+=1
                
        count1=(odd*(odd-1))//2+(even*(even-1))//2+even
        
        return count1
