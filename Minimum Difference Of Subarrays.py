'''Minimum Difference Of Subarrays
You are given an array of length 'n'. Your task is to split array into two nonempty subarrays such that th absolute difference between their sum is minimum

'''
def minimumDifference(n, arr):
    total_right=sum(arr)
    
    minimum=999999999
    
    total_left=0
    for i in range(n):
        total_left+=arr[i]
        total_right=total_right-arr[i]
        
        if abs(total_left-total_right)<minimum:
            minimum=abs(total_left-total_right)
            
    return  minimum

