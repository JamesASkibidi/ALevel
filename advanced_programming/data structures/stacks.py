def stackInitialise(stackSize):
    stack = []
    for i in range (stackSize):
        stack.append(None)

    return stack

def stackPush(item):

    global top
    global mystack
    global stackSize
    
    if top+1 != stackSize:
        top = top+1
       
        mystack[top] = item

        print(item , ' was pushed to the stack')
        print()
    else:
        print('Stack Full: ' , item , ' could not be added')
        print()
        stackfull = True

    return mystack 

def stackPop():
    global top

    if top > -1:
        popped = mystack[top]
        top -=1
    else:
        print('Stack is empty')
    
    return popped

stackfull = False

stackSize = 8

mystack = stackInitialise(stackSize)

top = -1


while stackfull == False:

    item = input('Add an item: ')

    stackPush(item)

popped = stackPop()




