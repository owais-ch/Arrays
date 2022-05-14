'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        length=len(s)
        
        if length%2==0:
            count=0
        else:
            count=1
            
        i=0
        j=length-1
        
        while i<j:
            if s[i]!=s[j]:
                if (s[:i]+s[i+1:]==(s[:i]+s[i+1:])[::-1]) or  (s[:j]+s[j+1:]==(s[:j]+s[j+1:])[::-1]):
                    return True
                else:
                    return False
                
            i+=1
            j-=1
            
        return True
