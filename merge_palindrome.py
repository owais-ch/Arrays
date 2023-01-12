'''Given a list of non-negative integers, find the minimum number of merge operations to make it a palindrome. A merge operation can only be performed on two adjacent
elements. The result of a merge operation is that the two adjacent elements are replaced with their sum.
Input:  [6, 1, 3, 7]
 
Output: 1
 
Explanation: [6, 1, 3, 7] —> Merge 6 and 1 —> [7, 3, 7]
 
 
Input:  [6, 1, 4, 3, 1, 7]
 
Output: 2
 
Explanation: [6, 1, 4, 3, 1, 7] —> Merge 6 and 1 —> [7, 4, 3, 1, 7] —> Merge 3 and 1 —> [7, 4, 4, 7]

'''

def pal_min(arr):
    length=len(arr)
    i,j=0,length-1
    
    count=0
    
    sum1=None
    sum2=None
    
    while i<j:
        if sum1==None and sum2==None:
            sum1=arr[i]
            sum2=arr[j]
        elif sum1==sum2:
            i+=1
            j-=1
            if i>=j:
                break
            sum1=arr[i]
            sum2=arr[j]
        elif sum1<sum2:
            i+=1
            if i>=j:
                break
            sum1+=arr[i]
            count+=1
        elif sum1>sum2:
            j-=1
            if i>=j:
                break
                
            sum2+=arr[j]
            count+=1
                    
    return count
