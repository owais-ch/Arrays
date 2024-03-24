'''
String Manipulation(GFG)

Tom is a string freak. He has got sequences of  n words to manipulate. If in a sequence, two same words 
come together then hell destroy each other. He wants to know the number of words left in the sequence after this pairwise destruction.
 
Example 1:

Input:
5
v[] = {"ab", "aa", "aa", "bcd", "ab"}
Output:
3
Explanation:
ab aa aa bcd ab
After the first iteration, we'll have: ab bcd ab
We can't further destroy more strings and
hence we stop and the result is 3. 
'''
class Solution:
    def removeAdj(self,v,n):
        stack=[]
        
        for i in range(n):
            if stack==[]:
                stack.append(v[i])
            else:
                if stack!=[] and stack[-1]==v[i]:
                    stack.pop()
                else:
                    stack.append(v[i])
                    
        return len(stack)
