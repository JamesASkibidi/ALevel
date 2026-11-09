def traverse():
    CurrentPointer = start
    while CurrentPointer != None:
        CurrentNode = linked_list[CurrentPointer]['Data']
        print(CurrentNode)
        CurrentPointer = linked_list[CurrentPointer]['pointer']
    




def add_item(item , linked_list):

    global Next_Free
    print(item)

    if Next_Free != None:
        linked_list[Next_Free]['data'] = item                            #set the next free's data as the new item
        
        NewFree = linked_list[Next_Free]['pointer']                      #store the pointer to the new next free location
        
        CurrentPointer = start

        while CurrentPointer != None:                                    #loop though to find trhe final item
            PrevPointer = CurrentPointer                                 #store the pointer of the final item
            CurrentPointer = linked_list[CurrentPointer]['pointer']
        
        linked_list[PrevPointer]['pointer'] = Next_Free                  #point the final item to the new final item

        linked_list[Next_Free]['pointer'] = None                         #point the new final item to null                   

        Next_Free = NewFree                                              #set the next free location as the previous next frees pointer

        return linked_list


# def ()








linked_list = [
    {'Data' : 'ketchup', 'pointer' : 1},        #0
    {'Data' : 'condiments', 'pointer' : 2},     #1
    {'Data' : 'mountain', 'pointer' : 3},       #2
    {'Data' : 'texas', 'pointer' : 4},          #3
    {'Data' : 'sheep', 'pointer' : None},       #4
    {'Data' : '_', 'pointer' : 6},              #5
    {'Data' : '_', 'pointer' : 7},              #6
    {'Data' : '_', 'pointer' : 8},              #7
    {'Data' : '_', 'pointer' : 9},              #8
    {'Data' : '_', 'pointer' : None}            #9
]

start = 0

Next_Free = 5



print('Original')
print()
traverse()
print()
print(start)
print(Next_Free)

linked_list = add_item('altitude' , linked_list)
print()
print('appended')
print()
traverse()
print()
print(start)
print(Next_Free)