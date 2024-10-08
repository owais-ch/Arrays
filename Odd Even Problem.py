'''
Odd Even Problem (GFG)

Given a string s of lowercase English characters, determine whether the summation of x and y is EVEN or ODD.
where:

x is the count of distinct characters that occupy even positions in the English alphabet and have even frequency. 
y is the count of distinct characters that occupy odd positions in the English alphabet and have odd frequency.
Ex: string = "ab" here 'a' has an odd(1) position in the English alphabet & has an odd(1) frequency in the string so a is odd but b has an even(2) position in
the English alphabet & has odd(1) frequency so it doesn't count(since string doesn't have 2 b's) so the final answer x + y = 1+0 = 1(odd) would be "ODD".

Note:

Return "EVEN" if the sum of x & y is even otherwise return "ODD".
You need to find index of characters in the english alphabet "abcdefghijklmnopqrstuvwxyz".
Examples :

Input: s = "abbbcc"
Output: ODD
Explanation: x = 0 and y = 1 so (x + y) is ODD. 'a' occupies 1st place(odd) in english alphabets and its frequency is odd(1), 'b' occupies 2nd place(even) but 
its frequency is odd(3) so it doesn't get counted and 'c' occupies 3rd place(odd) but its frequency is even(2) so it also doesn't get counted.
'''

from collections import Counter

class Solution:
    def oddEven(self, s : str) -> str:
        dict1=Counter(s)
        
        x,y=0,0
        
        for i in dict1:
            if (98-ord(i))%2==0 and dict1[i]%2==0:
                x+=1
            elif (98-ord(i))%2!=0 and dict1[i]%2!=0:
                y+=1
        
        if (x+y)%2==0:
            return "EVEN"
            
        return "ODD"
