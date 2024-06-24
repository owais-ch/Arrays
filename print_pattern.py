'''
Print Pattern (GFG)

Print a sequence of numbers starting with nn, without using a loop. Replace nn with n−5n - 5n−5 until n≤0n \leq 0n≤0. Then, replace n with n+5n + 5n+5 until nn regains its initial value.
Complete the function pattern(n) which takes n as input and returns a list containing the pattern.

Examples

Input: n = 16
Output: 16 11 6 1 -4 1 6 11 16
Explanation: The value decreases until it is greater than 0. After that it increases and stops when it becomes 16 again.
Input: n = 10
'''

import sys
sys.setrecursionlimit(18020);

class Solution:
    def __init__(self):
        self.arr=[]
        self.amount=None
        self.zero_flag=False
    def pattern(self, N):
        if self.amount==None:
            if N<=0:
                self.arr.append(N)
                return self.arr
            self.amount=N
            self.arr.append(self.amount)
            N-=5
        elif N<self.amount and N>0 and self.zero_flag==False:
            self.arr.append(N)
            N-=5
            if N<=0:
                self.zero_flag=True
                
        elif N<self.amount and N>0 and self.zero_flag==True:
            xx=self.arr[:-1][::-1]
            self.arr.extend(xx)
            
            return self.arr
            self.arr.append(N)
            N+=5
            
        elif N<self.amount and N<=0:
            self.arr.append(N)
            xx=self.arr[:-1][::-1]
            self.arr.extend(xx)
            
            return self.arr
            N+=5
            
            self.zero_flag==True
        elif self.amount>=N:
            self.arr.append(N)
            return 
            
        self.pattern(N);
       
        return self.arr
