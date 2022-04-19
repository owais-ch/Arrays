'''Problem Description

You are given an integer array A.

You have to find the number of occurences of each number.

Return an array containing only the occurences with the smallest value's occurence first.

For example, A = [4, 3, 3], you have to return an array [2, 1], where 2 is the number of occurences for element 3, 
and 1 is the number of occurences for element 4. But, 2 comes first because 3 is smaller than 4.



Problem Constraints
1 <= |A| <= 105
1 <= Ai <= 109


Input Format
The first argument is the integer array A.


Output Format
Return an integer array denoting the occurences of each number.


Example Input
Input 1:
A = [1, 2, 3]
Input 2:

A = [4, 3, 3]

Example Output
Output 1:
[1, 1, 1]
Output 2:

[2, 1]'''

from collections import OrderedDict,Counter

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        dict1=Counter(A)
        list2=list(zip(dict1.keys(),dict1.values()))

        list2.sort(key=lambda x:x[0])
        list1=[]

        for i in list2:
            list1.append(i[1])

        return list1
