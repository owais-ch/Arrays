'''
Sachin's love for runs

Sachin always wanted to score more and more runs for his team. Sometimes he succeeds in doing that and sometimes he fails. He also has a habit of noting down the runs he scored after every match in his diary.
After N  matches he always looks for his scores. In i-th match, he scores A[i] runs. Now he wanted to know the length of the maximum non-decreasing sub-segment in sequence A. As he wants to go for another match, help him in doing this task.

Example 1:

Input:                  
N = 6                       
A[] = {2, 2, 1, 3, 4, 1}
Output:
3
Explanation:
The maximum non-decreasing sub-segment is
the segment with numbers from the third to
the fifth one.
'''

class Solution:
    def compute(self, arr, n):
        maximum=1
        
        total=1
        
        for i in range(1,n):
            if arr[i]>=arr[i-1]:
                total+=1
            else:
                maximum=max(maximum,total)
                total=1
                
        maximum=max(maximum,total)
        
        return maximum

