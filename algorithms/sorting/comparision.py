import time
from tools import lists
import merge_sort

def insertion_sort(data):
    for pos in range(1 , len(data)):
        item = data[pos]
        while pos>0 and data[pos-1]>item:
            data[pos] = data[pos-1]
            pos=pos-1
        data[pos] = item
    return data

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

def merge(data):
    return merge_sort.sort(data)

list = lists.random_list(1,100,50)
print(list)


bubble_start = time.perf_counter()
print(bubble_sort(list.copy()))
bubble_end = time.perf_counter()
bubble_time = (bubble_end-bubble_start)*100000
print(list)

insert_start = time.perf_counter()
print(insertion_sort(list.copy()))
insert_end = time.perf_counter()
insert_time = (insert_end-insert_start)*100000
print(list)



merge_start = time.perf_counter()
print(merge(list.copy()))
merge_end = time.perf_counter()
merge_time = (merge_end-merge_start)*1000
print(list)

print("Bubble: " , bubble_time , " Insertion: " , insert_time , " Merge: " , merge_time)