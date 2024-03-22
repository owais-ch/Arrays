'''
Jumping Caterpillars
Given N leaves numbered from 1 to N . A caterpillar at leaf 1, jumps from leaf to leaf in multiples of Aj (Aj, 2Aj, 3Aj).
j is specific to the caterpillar. Whenever a caterpillar reaches a leaf, it eats it a little bit.. You have to find out how many leaves, from 1 to N, are left uneaten after all K caterpillars have reached the end.
Each caterpillar has its own jump factor denoted by Aj, and each caterpillar starts at leaf number 1.

Example 1:

Input:
N=10 K=3
arr[] = {2, 3, 5} 
Output: 2
Explanation: The leaves eaten by the first 
caterpillar are (2, 4, 6, 8, 10). The leaves 
eaten by the second caterpilllar are (3, 6, 9).
The leaves eaten by the third caterpilllar 
are (5, 10). Ultimately, the uneaten leaves are 
1, 7 and their number is 2.
'''

def uneatenLeaves(arr,n,k):
    set1={i for i in range(1,n+1)}
    arr=list(set(arr))
    length=len(arr)
    for i in range(length):
        start=arr[i]
        
        while start<n+1:
            if start in set1:
                set1.remove(start)
            start+=arr[i]
            
    return len(set1)
