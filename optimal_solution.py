''''
The optimal solution

Ishaan is given N integers in the form of an array A. He is asked to select all of these integers in any order. For selecting every integer he gets some points. He needs to maximize those points.
For every integer he selects, he gets points equal to the value of :
the selected integer * number of integers selected before the current integer (Refer example for explanation)
Help him find the maximum points he can get provided he can select every integer exactly 1 time.

 

Example 1:

â€‹Input : arr[ ] = {1, 2, 2, 4, 9}
Output : 
Explanation:
First he selects 1
Points : 1 * 0 (no integer selected before 
this), Total Points = 0

Then he selects 2
Points : 2 * 1 (1 selected before this)
Total Points = 2

Then he selects 2
Points : 2 * 2 (1,2 selected before this)
Total Points = 6

Then he selects 4
Points : 4 * 3 (1,2,2 selected before this)
Total Points = 18

Then he selects 9
Points : 9 * 4 (1,2,2,4 selected before this)
Total Points = 54
'''
def selection (arr, n) : 
    arr.sort()
    
    total=0
    
    for i in range(n):
        total+=(i*arr[i])
        
    return total
