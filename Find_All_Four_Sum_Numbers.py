'''
Find ALL Four Sum Numbers (GFG)
Given an array A of integers and another number K. Find all the unique quadruple from the given array that sums up to K.

Also note that all the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.

Example 1:

Input:
N = 5, K = 3
A[] = {0,0,2,1,1}
Output: 0 0 1 2 
Explanation: Sum of 0, 0, 1, 2 is equal
to K.
'''
class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        
        result_arr=[]
        set1=set()
        for i in range(n-3):
            for j in range(i+1,n-2):
                p=j+1;q=n-1
                if arr[i]+arr[j] +arr[p]+arr[p+1] > k:
                    break
                
                while p<q:
                    if arr[i]+arr[j]+arr[p]+arr[q]==k:
                        if (arr[i],arr[j],arr[p],arr[q]) not in set1:
                            set1.add((arr[i],arr[j],arr[p],arr[q]))
                            result_arr.append([arr[i],arr[j],arr[p],arr[q]])
                        p+=1
                        q-=1
                    elif arr[i]+arr[j]+arr[p]+arr[q] > k:
                        q-=1
                    else:
                        p+=1
                        
        return result_arr
