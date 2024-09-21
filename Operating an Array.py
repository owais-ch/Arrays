'''
Operating an Array (GFG)

Given an array arr, complete the following three functions:
searchEle: This function searches for an element x in the array arr. It should return a boolean value - true if the element is found, and false otherwise.
insertEle: This function inserts an element y at index yi in the array. true will be printed if the insertion is done correctly, and false otherwise.
deleteEle: This function deletes the first occurrence of an element z in the array. true will be printed if the deletion is done correctly, and false otherwise.
'''

class Solution:
    def searchEle(self,arr, x):
        if arr.count(x)==0:
            return False
        return True
    
    # insert element if you have inserted properly 1 will be printed else 0
    def insertEle(self,arr, y, yi):
        arr.insert(yi,y)
    
    # delete element if you have deleted properly 1 will be printed else 0
    def deleteEle(self,arr, z):
        if arr.count(z)>0:
            arr.remove(z)
