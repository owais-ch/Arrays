'''
You and your books
You have N stacks of books. Each stack of books has some non zero height Hi equal to the number of books on that stack ( considering all the books are identical and each book has a height of 1 unit ).
In one move, you can select any number of consecutive stacks of books such that the height of each selected stack of books Hi <= K . Once such a sequence of stacks is chosen , You can collect any number of books from the chosen sequence of stacks .
What is the maximum number of books that you can collect this way ?
'''
class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, a):
        count=0
        maximum=0
        total=0
        
        for i in range(n):
            if a[i]<=k:
                total+=a[i]
            else:
                maximum=max(maximum,total)
                total=0
        maximum=max(maximum,total)
        return maximum
