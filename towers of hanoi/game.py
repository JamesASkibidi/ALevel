def create_towers(towerNo , diskNo):

    for i in range (towerNo):
        towers.append([])
        for j in range (diskNo):
            towers[i].append(0)

    for i in range (diskNo):
        towers[0][i] = (diskNo - i)

def display_towers():
    print()



diskNo= 5

towerNo = 3

towers = []

create_towers(towerNo , diskNo)



















print(towers)
