values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def binary_search(list, target):
    L = 0
    R = (len(list))-1
    while L <= R:
        M = (L+R)//2
        if target>list[M]:
            L=M+1           
        elif target<list[M]:
            R=M-1
        else:
            return True , M
    return False , -1

            
    




found, location = binary_search(values, 13)

print(found, location )