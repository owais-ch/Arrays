'''You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "xbdef", b = "xecab"
Output: false'''

class Solution:
    def checkPalindromeFormation(self, a, b):
        n=len(a)
        
        i,j=0,n-1
        
        while i<j:
            if a[i]==b[j]:
                
                i+=1
                j-=1
            else:
                break
                
        num_char=n-i*2
        
        if a[i:i+num_char]==a[i:i+num_char][::-1] or b[j-num_char+1:j+1]==b[j-num_char+1:j+1][::-1]:
            return True
        
        i,j=0,n-1
        
        while i<j:
            if b[i]==a[j]:
                
                i+=1
                j-=1
            else:
                break
                
        num_char=n-i*2
        
        if b[i:i+num_char]==b[i:i+num_char][::-1] or a[j-num_char+1:j+1]==a[j-num_char+1:j+1][::-1]:
            return True
