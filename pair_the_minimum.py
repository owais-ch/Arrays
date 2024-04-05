'''
Pair the minimum (GFG)
Akshay loves to play with numbers and arrays. He took an array of size " 2n " where n is any positive integer chose by him. He tries to divide the array into n pairs, such that the pair sum minimizes the maximum sum of a pair.
For example, say we have an array with the given numbers [9, 6, 1, and 5]. The possible pairs are
( 1, 6 ) , ( 5 , 9 ) or ( 1 , 5 )  , ( 6 , 9 ) or  ( 1 , 9 ) , ( 5 , 6 ). The pair sums for these partitions are ( 7, 14 ) and ( 6, 15 ) and ( 10, 11 )  respectively.  The ideal or the selected pairs are (1, 9), (5, 6 )  because out of all the three cases or possibilities we only have (1, 9), (5, 6 )  where the sum of both pairs is a minimum of all the maximum sum of all three possibilities. 

 

Example 1:

â€‹Input : arr[ ] = {5, 8, 3, 9} and N = 2
Output : 13
Explanation:
Possible pairs: 
(8,9)(3,5) -->Case 1
Sum : (17)(8) --> maximum sum 17
(5,9)(3,8) -->Case 2
Sum : (14)(11) ----> maximum sum 14
(3,9)(5,8) -->Case 3
Sum : (12)(13)--> maximum sum 13
In case 3 , the maximum sum is minimum of 
all the other cases. Hence, the answer is 13.
'''

import math

class Solution:
    def Pair_minimum (self, arr, n) : 
        arr.sort()
        
        i,j=0,2*n-1
        maximum=-math.inf
        
        while i<j:
            if arr[i]+arr[j]>maximum:
                maximum=arr[i]+arr[j]
            i+=1
            j-=1
            
        return maximum
