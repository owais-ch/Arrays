'''
Chocolate Station (GFG)
Geek has an array Arr, where Arr[i] (1-based indexing) denotes the number of chocolates corresponding to each station. When he moves from station i to station i+1 he gets A[i] A[i+1] chocolates for free, 
if this number is negative, he looses that many chocolates also.
He can only move from station i to station i+1, if he has non-negative number of chocolates with him.
Given the cost of one chocolate Rs. P. Find the minimum cost incurred in reaching last station from the first station (station 1).
Note: Initially Geek has 0 chocolates.

Example 1:

Input:
N=3, price=10
arr[] = { 1, 2, 3 }
Output:  30
Explanation: 
To reach the first station from the starting
point, we need to buy 1 chocolate,To reach 
station 2 form station 1, we get A[1]  A[2]
= -1 chocolates i.e. we lose 1 chocolate. 
Hence, we need to buy 1 chocolate.Similarly, 
we need to buy 1 chocolate to reach station 3
from station 2.
Hence, total cost incurred = (1+1+1)*10 = 30
'''

def getChocolateCost(arr,chocolateMRP):
    total=arr[0]
    total_bought=total*chocolateMRP
    balance=0
    
    for i in range(1,n):
        balance=balance+arr[i-1]-arr[i]
        if balance<0:
            total_bought+=(-balance*chocolateMRP)
            balance=0
            
    return total_bought
