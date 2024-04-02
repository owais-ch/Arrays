'''
The Tiny Miny (GFG)
Find the smallest number that can be framed using the series created by the digits obtained by raising the given number  (  "a"  ) to the power from 1 to  n  i.e.  a^1 , a^2 , a^3 .......a^n . We get  b1,b2 , b3 , ........... bn . 
Using all the digits  ( including repeating ones )  that appear inb1 ,b2 , b3 .... bn . Frame a number that contains all the digits ( including repeating ones )  and find out the combination of digits that make the smallest number of all possible combinations. Excluding or neglecting zeroes  ( " 0 " )  . 

Example 1:

Input : A = 9 and N = 4
Output : 1125667899
Explanation:
9^1 = 9
9^2 = 81
9^3 = 729
9^4  = 6561 
9 81 729 6561
We get  9817296561 .
Using 9817296561 number we need to find 
the smallest possible number that can be 
framed using other combinations of the 
samenumber .
1298796561
8799265611
2186561997
.
.
.
1125667899
The smallest possible number that can be 
framed is1125667899 . 
'''
class Solution:
    def tiny_miny (self, a, n) : 
        string=''
        
        for i in range(1,n+1):
            string+=str(a**i)
          
        return int(''.join(sorted(string)))
