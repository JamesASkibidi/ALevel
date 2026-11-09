"""
##Works on the principle of "splitting" the Data into two abritrary parts: unsorted and worted

#e.g to being with 
3¦,7,2,1,5,7,9,23,5
it then works by taking each item in turn in the unsorted side and placing it in the correct position in the "sorted side"
#Once all "unsorted" items are placed the data is sorted


"""
def insertion_sort(data):
    ###for each item except the first
        #store the item being placed
        #store the start position of the current item i.e. i
        ##while there are items to the left AND the item to the left is larger than the item being placed
        #   overwrite the value at the current position (pos) with the value to its left
        #   take one away from the curret position
        #once this is completed we know the position to store the data
        #update the value of the current position to the copy of the data we took

    for pos in range(1 , len(data)):
        item = data[pos]
        while pos>0 and data[pos-1]>item:
            data[pos] = data[pos-1]
            pos=pos-1
        data[pos] = item
    return data



list = [3,7,2,1,5,7,9,23,5]


len(list)
print(insertion_sort(list))
            

"""
BIG O
Time best case- O(n)
Time Worst Case- O(n^2)
Space- O(1)
"""




