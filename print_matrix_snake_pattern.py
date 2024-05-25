'''
Print Matrix in snake Pattern (GFG)

Given a matrix of size N x N. Print the elements of the matrix in the snake like pattern depicted below.


Example 1:

Input:
N = 3 
matrix[][] = {{45, 48, 54},
             {21, 89, 87}
             {70, 78, 15}}
Output: 
45 48 54 87 89 21 70 78 15 
Explanation:
Matrix is as below:
45 48 54
21 89 87
70 78 15
Printing it in snake pattern will lead to 
the output as 45 48 54 87 89 21 70 78 15.
'''

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
        num_rows=len(matrix)
        num_cols=len(matrix[0])
        
        i,j=0,0
        right=True
        left=False
        
        list1=[0 for i in range(num_cols) for j in range(num_rows)]
        k=0
        while i<num_rows and j<num_cols and j>-1:
            #print(matrix[i][j])
            list1[k]=matrix[i][j]
            k+=1
            if left==False and j==num_cols-1:
                i+=1
                if i<num_rows:
                    #print(matrix[i][j])
                    list1[k]=matrix[i][j]
                    k+=1
                right=False
                left=True
            elif right==False and j==0:
                i+=1
                if i<num_rows:
                    #print(matrix[i][j])
                    list1[k]=matrix[i][j]
                    k+=1
                left=False
                right=True
                
            if right==True and j<n-1:
                j+=1
            elif left==True and j>0:
                j-=1
                
            
            if i>=num_rows:
                break
        return list1
