'''Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 
Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]'''

class Solution:
    def findClosestElements(self, arr, k, x):
        length=len(arr)
        
        if x<=arr[0]:
            return arr[:k]
        elif x>=arr[-1]:
            return arr[-k:]
        
        count_left=1
        count_right=1
        
        if x in arr:
            indexz=arr.index(x)
            n=1
            list1=[x]
        else:
            arr.append(x)
            arr.sort()
            length=len(arr)
            indexz=arr.index(x)
            n=0
            list1=[]
            
        
        while n<k:
            if indexz-count_left<0:
                list1.extend(arr[indexz+count_right:indexz+count_right+k-n])
                list1.sort()
                return list1
            elif indexz+count_right>length-1:
                list1.extend(arr[indexz-count_left-(k-n-1):indexz-count_left+1])
                list1.sort()
                return list1
            
            
            if abs(arr[indexz]-arr[indexz-count_left])<abs(arr[indexz]-arr[indexz+count_right]):
                list1.append(arr[indexz-count_left])
                count_left+=1
                n+=1
            elif abs(arr[indexz]-arr[indexz-count_left])>abs(arr[indexz]-arr[indexz+count_right]):
                list1.append(arr[indexz+count_right])
                count_right+=1
                n+=1
            else:
                if arr[indexz-count_left]<arr[indexz+count_right]:
                    list1.append(arr[indexz-count_left])
                    count_left+=1
                    n+=1
                elif arr[indexz-count_left]>arr[indexz+count_right]:
                    list1.append(arr[indexz+count_right])
                    count_right+=1
                    n+=1
              
        list1.sort()
        
        return list1
                    
