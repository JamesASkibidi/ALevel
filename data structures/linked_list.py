def traverse():
    CurrentPointer = start
    while CurrentPointer != None:
        CurrentNode = linked_list[CurrentPointer]['Data']
        print(CurrentNode)
        CurrentPointer = linked_list[CurrentPointer]['pointer']
    



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

traverse()

