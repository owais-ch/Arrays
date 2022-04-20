'''Problem Description
 
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.

Input Format
First and only argument is an integer array A.

Output Format
Return 1 if any such integer p is found else return -1.

Example Input
Input 1:

 A = [3, 2, 1, 3]
Input 2:

 A = [1, 1, 3, 3]


Example Output
Output 1:

 1
Output 2:

 -1'''

from  collections import Counter

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        total=len(A)
        
        dict1=Counter(A)

        list1=list(zip(dict1.keys(),dict1.values()))
        list1.sort(key=lambda x:x[0])

        for i in list1:
            if total-i[1]==i[0]:
                
                return 1
            total-=i[1]

        return -1
