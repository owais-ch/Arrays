'''
Pairs which are Divisible by 4 (GFG)

Given an array, if ‘n’ positive integers, count the number of pairs of integers in the array that have the sum divisible by 4.

Example 1:

Input : Arr[] = {2, 2, 1, 7, 5}
Output : 3
Explanation:
(2,2), (1,7) and(7,5) are the 3 pairs.

Time taken:0.47 sec   Time complexity: O(N)  Space complexity: O(1)
'''
class Solution:
    def count4Divisibiles(self, arr , n ): 
        num_zeros=0
        num_ones=0
        num_twos=0
        num_threes=0
        
        for i in range(n):
            if arr[i]%4==0:
                num_zeros+=1
            elif arr[i]%4==1:
                num_ones+=1
            elif arr[i]%4==2:
                num_twos+=1
            else:
                num_threes+=1
                
        zero_pair=(num_zeros*(num_zeros-1))//2
        one_three_pair=num_threes*num_ones
        two_pair=(num_twos*(num_twos-1))//2
        
        return zero_pair+one_three_pair+two_pair
