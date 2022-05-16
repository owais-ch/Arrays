'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length1=len(s)
        length2=len(t)
        if length2==0 and length1!=0:
            return False
        if length1<=length2:
            i,j=0,0
            count=0
            while i<length1 and j<length2:
                if s[i]==t[j]:
                    i+=1
                    j+=1
                    count+=1
                else:
                    j+=1
                    
            if count==length1:
                return True
            
        else:
            i,j=0,0
            count=0
            while i<length1 and j<length2:
                if t[i]==s[j]:
                    i+=1
                    j+=1
                    count+=1
                else:
                    i+=1
                    
            if count==length2:
                return True
            
        return False
