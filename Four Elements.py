'''
Given an array A of N integers. You have to find whether a combination of four elements in the array whose sum is equal to a given value X exists or not.
 
Example 1:

Input:
N = 6
A[] = {1, 5, 1, 0, 6, 0}
X = 7
Output:
1

Explantion:
1, 5, 1, 0 are the four elements which makes sum 7.
'''

def find4Numbers( A, n, X):
    A.sort()
    
    for i in range(n-3):
        for j in range(i+1,n-2):
            p=j+1;q=n-1
            
            while p<q:
                if A[i]+A[j]+A[p]+A[q]==X:
                    return 1
                elif A[i]+A[j]+A[p]+A[q]<X:
                    p+=1
                elif A[i]+A[j]+A[p]+A[q]>X:
                    q-=1
                    
    return 0
