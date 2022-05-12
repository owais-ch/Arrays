'''Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n=len(s)
        
        i=0
        j=n-1
        
        list1=list(s)
        
        while i<j:
            if list1[i].isalpha() and list1[j].isalpha():
                list1[i],list1[j]=list1[j],list1[i]
                i+=1
                j-=1
            elif list1[i].isalpha()==True and list1[j].isalpha()==False:
                j-=1
            elif list1[i].isalpha()==False and list1[j].isalpha()==True:
                i+=1
            else:
                i+=1
                j-=1
                
        return ''.join(list1)
