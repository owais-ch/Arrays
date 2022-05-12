'''Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the 
first k characters and leave the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length=len(s)
        
        if length<k:
            return s[::-1]
        else:
            count=0
            list1=list(s)
            start=0
            for i in range(0,length,k):
                if count%2==0:
                    list1[start:start+k]=list1[start:start+k][::-1]
                count+=1
                start+=k
                
            return ''.join(list1)
