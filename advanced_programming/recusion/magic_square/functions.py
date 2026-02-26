def print_grid(grid):
    for row in grid:
        print()
        for collumn in row:
           print(collumn , end = '')

def sum_row(row):
    total = 0
    for collumn in row:
        total += collumn
    if total == 15:
        return True
    return False

def sum_collumn(count , grid):
    count = count + 2
    total = 0
    for row in grid:
        for collumn in row:
            count +=1
            if count %3 == 0:
                total += collumn  
    if total == 15:
        return True
    return False 

def sum_diagonal1(row_no, grid):
    total = 0
    coordinate =0
    
    for i in range(row_no):
        total = total + grid[coordinate][coordinate]
        coordinate +=1
    if total == 15:
        return True
    return False

def sum_diagonal2(row_no , grid):
    total = 0 
    coord_x = row_no-1
    coord_y = 0

    for i in range(row_no):
        total = total + grid[coord_x][coord_y]
        coord_y += 1
        coord_x -= 1
    if total ==15:
        return True
    return False
 
def sum_all(grid , row_no):
    correct = 0
    for row in grid:
        
        valid = sum_row(row)
        if valid:
            correct+=1
            
    for i in range(row_no):
        valid = sum_collumn(i, grid)
        if valid:
            correct +=1
    
    valid = sum_diagonal1(row_no , grid)
    if valid:
        correct+=1
    valid = sum_diagonal2(row_no , grid)
    if valid:
        correct += 1
       
    return correct