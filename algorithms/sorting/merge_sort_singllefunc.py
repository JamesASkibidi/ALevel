from tools import lists

def merge_sort(data):
    if len(data)<=1:
            return data #if element is size 1 already - retrun it 
    m= len(data)//2 #find midpoint of data
    l= data[:m]     #store each half of the data in a new array
    r= data[m:]


    left = merge_sort(l)  #recursively call merge sort on the new arrays
    right = merge_sort(r)

    sorted=[]
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:            #added the smallest of each's first item to the combined array
            sorted.append(left.pop(0))
        else:
            sorted.append(right.pop(0))

        sorted.extend(left)             #once one array is empty add the remaining elements of the other
        sorted.extend(right)

    return sorted




list = lists.random_list(1,100,10)

print(list)

sorted_list = merge_sort(list)

print(sorted_list)