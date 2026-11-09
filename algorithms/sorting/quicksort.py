from tools import lists

def quick_sort(data):
    #If base case has not been reached
    #base case: data contains more than one item
    if len(data)<=1:
            return data
        
    p = data(len(data) - 1)    #set pivot point (last item)

        #partition
        #move all smaller items to left
        #move all larger items to right

        #recursion
        #call on data to left of pivot
        #call on data to right of pivot
    pass







list = lists.random_list(1,50,10)

print(list)