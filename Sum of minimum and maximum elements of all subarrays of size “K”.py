'''Sum of minimum and maximum elements of all subarrays of size “K”'''

def sumOfMaxAndMin(nums, n, k):
    minimum=min(nums[:k])
    index_min=nums[:k].index(minimum)
    
    maximum=max(nums[:k])
    index_max=nums[:k].index(maximum)
    
    total=minimum+maximum
    
    for i in range(1,n-k+1):
        if nums[i+k-1]<minimum:
            minimum=nums[i+k-1]
            index_min=i+k-1
        elif nums[i+k-1]>maximum:
            maximum=nums[i+k-1]
            index_max=i+k-1

        if index_min<i:
           minimum=min(nums[i:i+k])
           index_min=index_min+1+nums[i:i+k].index(minimum)
        if index_max<i: 
            maximum=max(nums[i:i+k])
            index_max=index_max+1+nums[i:i+k].index(maximum)
    
        total+=minimum+maximum
    return total
