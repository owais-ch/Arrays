'''

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        n=len(s)
        
        dict1={'a':0,'e':1,'i':1,'o':1,'u':1,'A':0,'E':1,'I':1,'O':1,'U':1}
        list1=list(s)
        
        i=0
        j=n-1
        
        
        while i<j:
            if list1[i] in dict1 and list1[j] in dict1:
                list1[i],list1[j]=list1[j],list1[i]
                i+=1
                j-=1
            elif list1[i] in dict1 and list1[j] not in dict1:
                j-=1
            elif list1[i] not in dict1 and list1[j] in dict1:
                i+=1
            else:
                i+=1
                j-=1
                
        return ''.join(list1)
