'''
Maximum point you can obtain from cards

There are several cards arranged in a row, and each has an associated number of points. The points are given in the integer array cardPoints of size N.
In one step, you can take one card from beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints, and its size N and the integer k, return the maximum score you can obtain.

Example 1:

Input:
N = 7
k = 3
cardPoints[ ] = {1, 2, 3, 4, 5, 6, 1}
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the cards on the right, giving a final score of 1 + 6 + 5 = 12.
'''

class Solution:
    def maxScore(self, cardPoints, N, k):
        maximum=sum(cardPoints[:k])
        total=maximum
        
        j=0
        
        for i in range(-1,-k-1,-1):
            total=total-cardPoints[k-1-j]+cardPoints[i]
            maximum=max(maximum,total)
            j+=1
        return maximum
