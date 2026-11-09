from algorithms.sorting.tools import lists

def bubble_sort(array):
    repeat = True
    while repeat:
        repeat = False
        for i in range (len(array)-1):
            if len(array)==i:
                pass
            elif array[i]>array[i+1]:
                array[i] , array[i+1] = array[i+1] , array[i]
                repeat = True
    return array


lists.random_list(1,10,20)

sorted = bubble_sort(list)

print(sorted)


#best case: O(n) - linear, every item must be checked against each neighbour once
#worst case: O(n^2) - quadratic, wpould perfrom n passes each requiring n comparisons

#space: O(1) - as the  size of data changes, the aditional memory space required does not change

