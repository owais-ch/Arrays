'''Find the minimum number of moves required for converting an array of zeroes to a given array of non-negative integers using only increment and double operations. 
The increment operation increases the value of an array element by 1 and the double operation doubles the value of each array element.'''

from math import ceil

def minimum_moves(arr):
    length=len(arr)
    
    minimum=min(arr)
    
    total=0
    
    for i in range(length):
        total+=arr[i]-minimum
    
    #print(total)
    while minimum>1:
        if minimum%2==0:
            minimum=minimum//2
            total+=1
        else:
            minimum=minimum-1
            total+=length
    
        print(minimum)
    total+=length
    
    return total
