'''
Hungry Pizza Lovers(GFG)

Dominos Pizza has hungry customers waiting in the queue. Each unique order is placed by a customer at time x[i], and the order takes y[i] units of time to complete.
You have information on all n orders, Find the order in which all customers will receive their pizza and return it. If two or more orders are completed at the same time then sort them by non-decreasing order number.

Example 1:

Input : arr[ ] = {{4,1}, {6,2}, {7,6}, 
                       {8,1}, {1,3}}
Output : 5 1 2 4 3
Explanation:
Here an array can be transform to 
{5, 8, 13, 9, 4}. Here 5th index order 
received first then 1st order, 2nd order...
return {5, 1, 2, 4, 3}
'''
class Solution:
    def permute(self,arr,n):
        arr=sorted(enumerate([i[0]+i[1] for i in arr]),key=lambda x:x[1])
        
        return list(map(lambda x:x[0]+1,arr))

