'''
You are given two arrays A and B of unique elements of size N. Check if array B is a stack permutation of the array A or not.
Stack permutation means that array B can be created from array A using a stack and stack operations.

Example 1:

Input:
N = 3
A = {1,2,3}
B = {2,1,3}
Output:
1
Explanation:
1. push 1 from A to stack
2. push 2 from A to stack
3. pop 2 from stack to B
4. pop 1 from stack to B
5. push 3 from A to stack
6. pop 3 from stack to B
'''
class Solution:
    def isStackPermutation(self, N, A, B):
        stack=[]
        j=0
        rem_list=[]
        for i in range(N):
            if A[i]==B[j]:
                j+=1
            else:
                #print(stack)
                if stack!=[] and B[j]==stack[-1]:
                    stack.pop()
                    j+=1
                else:
                    stack.append(A[i])
                    
        if stack!=[] and j<N:
            p=j
            while p<N and stack!=[]:
                if stack[-1]==B[p]:
                    stack.pop()
                    p+=1
                else:
                    rem_list.append(B[p])
                    p+=1
                  
        if stack==[]: 
            return 1
            
        return 0
