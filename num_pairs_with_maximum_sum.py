'''
Number of pairs with maximum sum
Given an array arr[], count number of pairs arr[i], arr[j] such that arr[i] + arr[j] is maximum and i < j.

Example 1:

Input : Arr[] = {1, 1, 1, 2, 2, 2}
Output : 3
Explanation:
We have an array [1, 1, 1, 2, 2, 2]
The maximum possible pair
sum where i is less than j is  4, which 
is given by 3 pairs, so the answer is 3
the pairs are (2, 2), (2, 2) and (2, 2).

'''
import math

class Solution:
    # Function to find the number 
    # of maximum pair sums 
    def MaximumSum(self, a, n): 
        maximum=-math.inf
        second_maximum=-math.inf
        
        for i in range(n):
            if arr[i]>maximum:
                second_maximum=maximum
                maximum=arr[i]
            elif arr[i]<maximum and arr[i]>=second_maximum:
                second_maximum=arr[i]
        
        #print(maximum,second_maximum)
        count_max=0
        count_second_max=0
        
        for i in range(n):
            if arr[i]==maximum:
                count_max+=1
            elif arr[i]==second_maximum:
                count_second_max+=1
                
        if count_max>1:
            return (count_max*(count_max-1))//2
        else:
            return count_max*count_second_max
