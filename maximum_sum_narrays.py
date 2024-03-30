'''
Maximum sum of increasing order elements from n arrays (GFG)

Given n arrays of size m each. Find maximum sum obtained by selecting a number from each array such that the element selected from the i-th array is more than the element 
selected from (i-1)-th array. If maximum sum cannot be obtained then return 0.

Example 1:

â€‹Input : arr[ ] = {{1,7,4,3}, {4,2,5,1}, {9,5,1,8}}
Output : 18
Explanation:
We can select 4 from the first array,
5 from second array and 9 from the third array.
'''
def maximumSum (n, m, arr) : 
    arr=list(map(lambda x:sorted(x),arr))
    
    total=0
    for i in range(n-1,-1,-1):
        if i==n-1:
            total+=arr[i][-1]
            maximum=arr[i][-1]
        else:
            for j in range(m-1,-1,-1):
                if arr[i][j]<maximum:
                    maximum=arr[i][j]
                    total+=maximum
                    break
            else:
                return 0
        
    return total
