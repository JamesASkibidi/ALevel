from tools import lists

def sort(data): #Divide
    if len(data)<=1:
        return data #if element is size 1 already - retrun it 
    m= len(data)//2 #find midpoint of data
    l= data[:m]     #store each half of the data in a new array
    r= data[m:]

    
    sort_left = sort(l)  #recursively call merge sort on the new arrays
    sort_right = sort(r)   #store these in a new array

    return merge(sort_right, sort_left) #call a new function to combine and sort these arrays


def merge(left, right): #Conquer
    i=j=0
    sorted = []
    while i<len(left) and j<len(right): #while there are still data items within the arrays
        if left[i]<right[j]:            #added the smallest of each's first item to the combined array
            sorted.append(left[i])      
            i+=1
        else:
            sorted.append(right[j])
            j+=1

    sorted.extend(left[i:])             #once one array is empty add the remaining elements of the other
    sorted.extend(right[j:])

    return sorted                       #return this back the the previous call to be comnbined with the next array up

list = lists.random_list(-100,100,10)

sorted_list = sort(list)

print(sorted_list)






"""
merge sort: Divide and conquer
It breaks down the problem into its smallest easiest to solve parts
The smaller parts are then recombined into larger solved parts until the whole probleem is solved
D&C Algorithms are recursive

During DIVIDE merge sort will recursively split the data until we have size 1 sorted arrays

Durin MERGE the smaller sub-arrays / left & right arrays are combined by
-Comparing the first item in both arrays
-The smaller is added to a new larger array
-This continues until one of the arrays is empty- then the remaning items from the other are added

The new larger array is retrurned to the previous function call where it is combined with another array
The process repeats until the initial call merges the final two arrays
"""

