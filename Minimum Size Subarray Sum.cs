/*
Minimum Size Subarray Sum (LeetCode)
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
*/

public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int total = 0;
        int min_length = int.MaxValue;
        int length = nums.Count();

        int i = 0;
        int j = 0;
        
        while ( i < length && total < target )
        {
            total += nums[i];
            i++;
        }

        if ( total >= target )
        {
            min_length = i;
        }

        while (i < length && j < length)
        {
            total += nums[i];

            while ( j < i && total >= target )
            {
                total -= nums[j];
                
                if ( total >= target && i-j < min_length)
                {
                    min_length = i-j;
                }
                j++;
            }
            i++;
        }

        while ( j < length )
        {
            total -= nums[j];
            j++;
            if (total>=target && i-j <min_length)
            {
                min_length = i-j;
            }
            
        }

        if ( min_length == int.MaxValue )
        {
            return 0;
        }

        return min_length;
    }
}
