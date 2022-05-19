'''Given an array/list 'ARR' of integers and a position ‘M’. You have to reverse the array after that position.

Sample Input 1:
2
6 3
1 2 3 4 5 6
5 2
10 9 8 7 6
Sample Output 1:
1 2 3 4 6 5
10 9 8 6 7'''

def reverseArray(arr, m):
	start=m+1
	end=len(arr)-1
	
	while start<end:
		arr[start],arr[end]=arr[end],arr[start]
		start+=1
		end-=1
		
	return arr
