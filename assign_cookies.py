'''
Assign Cookies (GFG)
Assume you are an awesome parent of N children and want to give your children some cookies out of given M cookies. But, you should give each child atmost one cookie.
Each child i has a greed factor greed [ i ], which is the minimum size of cookie that the child will be content with; and each cookie j has a size sz [ j ]. If sz [ j ] >= greed [ i ],
we can assign the cookie j to the child ith, and the child i will be content.
Your goal is to maximize the number of your content children and return the maximum number.
Return number of maximum content children you can obtain with N cookies.

Example 1:

Input:
N = 3 
M = 2
greed [ ] = {1, 2, 3}
sz [ ] = {1, 1}
Output: 1
Explanation: 
You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to return 1.
'''

class Solution:
    def maxChildren(self, N, M, greed, sz):
        greed.sort()
        sz.sort()
        
        i,j=0,0
        
        count=0
        
        while i<N and j<M:
            if sz[j]>=greed[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
                
        return count
