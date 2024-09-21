'''
Maximum no of 1's row (GFG)

Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s.

Example 1:

Input:
N = 3, M = 4
Mat[] = {{0 1 1 1},
         {0 0 1 1},
         {0 0 1 1}}
Output: 0
Explanation: Row 0 has 3 ones whereas
rows 1 and 2 have just 2 ones.
'''

class Solution:
    def maxOnes (self, arr, N, M):
        maximum=0
        row=-1
        
        for i in range(N):
            low,high=0,M-1
            count=0
            while low<=high:
                mid=(low+high)//2
                
                if arr[i][mid]==0:
                    if mid+1<M:
                        if arr[i][mid+1]==0:
                            low=mid+1
                        else:
                            if M-mid-1>maximum:
                                maximum=M-mid-1
                                row=i
                            break
                    else:
                        break
                elif arr[i][mid]==1:
                    if mid-1>=0:
                        if arr[i][mid-1]==1:
                            high=mid-1
                        else:
                            if M-mid>maximum:
                                maximum=M-mid
                                row=i
                            break
                    else:
                        if M-mid>maximum:
                            maximum=M-mid
                            row=i
                        break
                    
        return row
