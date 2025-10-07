import os, time

def create_towers(towerNo , diskNo, tops):

    for i in range (towerNo):
        towers.append([])
        tops.append(-1)
        for j in range (diskNo):
            towers[i].append(0)
    tops[0] = diskNo - 1 
    
    
    for i in range (diskNo):
        towers[0][i] = (diskNo - i)
    return tops


def display_towers():
    for i in range(diskNo-1, -1, -1): # found a way of printing in reverse order
        for j in range(towerNo):
            print(towers[j][i], end='   ')
        print()
    
def pop_disk(towerpop,):
    global tops , towers
    if tops[towerpop] == -1:
        return -1
    else:
        disk = towers[towerpop][tops[towerpop]]
        towers[towerpop][tops[towerpop]] = 0
        tops[towerpop] -= 1
        return disk
    
def push_disk(towerpush, disk):
    global tops , towers , diskNo
    if tops[towerpush] < diskNo -1 and ( tops[towerpush] ==-1 or towers[towerpush][tops[towerpush]] > disk):
        tops[towerpush]+=1
        towers[towerpush][tops[towerpush]] = disk
        return True
    else:
        return False

def tower_checker():
    global diskNo , towerNo, tops
    for i in range (towerNo):
        if tops[i+1] == diskNo:
            return True

        else:
            return False

def processing():
    for i in range (2):
        print('loading.')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('loading..')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('loading...')
        time.sleep(0.25)
        os.system('cls' if os.name == 'nt' else 'clear')

diskNo= 5

towerNo = 3

towers = []

tops = []

tops = create_towers(towerNo , diskNo, tops ,)

win = False

display_towers()

while win == False:

    valid = False

    while valid == False:

        towerpop = int(input('Pick a tower to remove from (1-3): '))-1
        if towerpop >-1 and towerpop <3:
            valid = True
        else:
            print('Invalid Input')


    print()

    disk = pop_disk(towerpop)

    if disk == -1:
        print('Invalid Move')
    
    else:

        valid = False
        while valid == False:

            towerpush = int(input('Pick a tower to drop the disk onto (1-3): '))-1
            if towerpush >-1 and towerpush <3:
                valid = True
            else:
                print('Invalid Input')


        print()

        dropped = push_disk(towerpush , disk)

        if dropped == False:
            towerpush = towerpop
            dropped = push_disk(towerpush , disk)
            print('Invalid Move')

    processing()

    display_towers()

    win = tower_checker()
    if win == True:
        break


print('You won!')




















print(towers)
