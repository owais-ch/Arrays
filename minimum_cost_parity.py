'''
Given an arr[] of length N, the task is to make parity of arr[] the same by using the below-provided operation:

Select a subarray containing elements of the same parity.
Remove the subarray.
The cost to remove that subarray is (absolute adjacent difference of all elements present in sub-array)*(length of subarray). For a sub-array of length 1,
the cost will be the element present in that subarray.
Examples:

Input: N = 3, arr[] = {2, 4, 6}
Output: 0
Explanation: All the elements of given arr[] are even, Input arr[] has even parity already. Therefore, minimum cost is 0

Input: N = 4, arr[] = {22, 42, 64, 7}
Output: 7
'''

def minimum_cost(arr):
    length=len(arr)
    
    even_sum=0
    odd_sum=0
    even_count=0
    odd_count=0
    
    total_even=0
    total_odd=0
    
    for i in range(1,length):
        decider='Yes'
        if arr[i-1]%2==0 and arr[i]%2==0:
            even_sum+=abs(arr[i-1]-arr[i])
            even_count+=1
            decider='Yes'
        elif arr[i-1]%2!=0 and arr[i]%2!=0:
            odd_sum+=abs(arr[i-1]-arr[i])
            odd_count+=1
            decider='Yes'
        elif arr[i-1]%2==0 and arr[i]%2!=0:
            if even_count==0:
                even_count+=1
                even_sum+=arr[i-1]
                total_even+=even_sum
                even_sum=0
                even_count=0
            elif even_count>0:
                even_count+=1
                total_even=total_even+(even_count*even_sum)
                even_sum=0
                even_count=0
            if i==length-1:
                total_odd+=arr[i]
            
        elif arr[i-1]%2!=0 and arr[i]%2==0:
            if odd_count==0:
                odd_sum+=arr[i-1]
                total_odd+=odd_sum
                odd_count=0
                odd_sum=0
            elif odd_count>0:
                odd_count+=1
                total_odd=total_odd+(odd_count*odd_sum)
                odd_count=0
                odd_even=0
            
            if i==length-1:
                total_even+=arr[i]
              
    if even_sum>0 and even_count>0:
        even_count+=1
        total_even+=(even_sum*even_count)
    elif odd_sum>0 and odd_count>0:
        odd_count+=1
        total_odd+=(odd_sum*odd_count)

    
    return min(total_odd,total_even)
