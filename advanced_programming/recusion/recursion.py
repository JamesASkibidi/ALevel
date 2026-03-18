# import sys
# print(sys.getrecursionlimit())


# sys.setrecursionlimit(1500)


# def callme(n,pn):
#     print(n)
#     tmp = pn
#     pn = n
#     n = n + tmp
#     if n <100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
#         callme(n,pn)

# callme(1,0)



# def sumTo(n):
#     if n==1:
#         return 1
#     else:
#         return n + sumTo(n-1)
    
# def sum2(n):
#     total = 0
#     for i in range(n+1):
#         total += i
#         print(i)

#     return total


# print(sum2(4))



# def countGreater(arr, index, threshold):
#     if index == len(arr):
#         return 0
#     else:
#         if arr[index] > threshold:
#             return 1 + countGreater(arr, index+1, threshold)
#         else:
#             return countGreater(arr, index+1, threshold)
    
def sum_row(row):
    total = 0
    for collumn in row:
        total += collumn
    if total == 15:
        return True
    return False

def sum_collumn(count):
    total = 0
    count = count + 2
    for row in grid:
        for collumn in row:
            count +=1
            if count %3 == 0:
                total += collumn  
    if total == 15:
        return True
    return False 
     

              


         

def sum_all(grid):
    correct = 0
    for row in grid:
        
        valid = sum_row(row)
        if valid:
            correct+=1
            
    for i in range(3):
        valid = sum_collumn(i)
        if valid:
            correct +=1
    
    return correct

        


        


                
                
                    
grid = [
    [5,5,5],
    [5,5,5],
    [5,5,5],
]

print(sum_all(grid))
