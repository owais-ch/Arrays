'''
Max and Min Products (GFG)

Given a set, we need to find the maximum and minimum possible product among all subsets of the set.

Example 1:

Input : 
arr[] = {1, 2, 3};
Output : 
Maximum product = 6
Minimum product = 1
Explanation :
Maximum product is obtained by multiplying
2, 3
Minimum product is obtained by multiplying
1
'''
import math

class Solution:
    def getMaxandMinProduct(self, arr, n): 
        if n==1:
            return arr[0],arr[0]
        num_neg=0;
        num_zeros=0;
        num_pos=0;
        
        minimum=math.inf
        maximum=-math.inf
        
        pos_product=1
        neg_product=1
        highest_neg=-math.inf
        lowest_pos=math.inf
        
        for i in range(n):
            if arr[i]==0:
                num_zeros+=1
            elif arr[i]>0:
                if arr[i]<lowest_pos:
                    lowest_pos=arr[i]
                pos_product*=arr[i]
                num_pos+=1
            else:
                if arr[i]>highest_neg:
                    highest_neg=arr[i]
                    
                neg_product*=arr[i]
                
                num_neg+=1
            if arr[i]>maximum:
                maximum=arr[i]
            if arr[i]<minimum:
                minimum=arr[i]
        
        #print(num_pos,num_neg,num_zeros)
        if num_neg>0 and num_pos>0 and num_zeros>0:
            if num_neg%2==0:
                maximum_product=pos_product*neg_product
                minimum_product=(pos_product*neg_product)//highest_neg
            else:
                maximum_product=(pos_product*neg_product)//highest_neg
                minimum_product=pos_product*neg_product
        elif num_neg==0 and num_pos>0 and num_zeros>0:
            maximum_product=pos_product
            minimum_product=0
        elif num_neg>0 and num_pos==0 and num_zeros>0:
            if num_neg%2==0:
                maximum_product=neg_product
                minimum_product=min(0,neg_product//highest_neg)
            else:
                if num_neg==1:
                    maximum_product=0
                else:
                    maximum_product=neg_product//highest_neg
                minimum_product=neg_product
        elif num_neg>0 and num_pos>0 and num_zeros==0:
            if num_neg%2==0:
                maximum_product=pos_product*neg_product
                minimum_product=(pos_product*neg_product)//highest_neg
            else:
                maximum_product=(pos_product*neg_product)//highest_neg
                minimum_product=pos_product*neg_product
        elif num_neg>0:
            if num_neg%2==0:
                maximum_product=neg_product
                minimum_product=neg_product//highest_neg
            else:
                maximum_product=neg_product//highest_neg
                minimum_product=neg_product
        elif num_pos>0:
            maximum_product=pos_product
            minimum_product=lowest_pos
        elif num_zeros>0:
            maximum_product=0
            minimum_product=0
        
            
        return minimum_product,maximum_product
