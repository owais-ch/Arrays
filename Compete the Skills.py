'''
Comepete the Skills (GFG)

A and B are good friends and programmers. They decide to judge the best among them by competing. They do so by comparing their three skills as per their values.

Skills of A are arr1= [a1, a2, a3]
Skills of B are arr2= [b1, b2, b3]

Compare ith skill of A with ith skill of B whichever has a higher skill value gets 1 point

Example :

Input: arr1[] = [4, 2, 7], arr2[] = [5, 6, 3]
Output: [1, 2]
Explanation: 4<5, 2<6 and 7>3
Input: arr1[] = [4, 2, 7], arr2[] = [5, 2, 8]
Output: [0, 2]
Explanation: 4<5, 2=2 and 7<8
'''

class Solution:
    #Function to return a list containing the intersection of two arrays.
    def scores(self, arr1, arr2):
        n=len(arr1)
        score1,score2=0,0
        
        for i in range(n):
            if arr1[i]>arr2[i]:
                score1+=1
            elif arr2[i]>arr1[i]:
                score2+=1
        return score1,score2

