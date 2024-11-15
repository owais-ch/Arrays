'''
Professor and Parties (GFG)

A professor attended a party and classified it into two categories based on the colors of the robes. If all party members are wearing different colored robes, represented by positive integers in the array arr[],
then it is a girl's only party. If there is at least one duplicate color, it is a boy's party. Determine the type of party by returning “true” if it’s a boy’s party, otherwise, return “false”.

Examples:

Input: arr[] = [1, 2, 3, 4, 7]
Output: false
Explanation: All the colors are unique so it's a GIRLS party.
Input: arr[] = [1, 3, 2, 4, 5, 1]
Output: true
Explanation: There are two colors 1. So it's a BOYS party.
'''

class Solution:
    def PartyType(self, arr):
        n=len(arr)
        m=len(set(arr))
        
        if n==m:
            return "false"
            
        return "true"
