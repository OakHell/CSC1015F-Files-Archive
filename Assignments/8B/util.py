#Abdul-KAder Jainoodien
#JNDAABD002
#14 April 2024
#Varius utilities for the game 2048

def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0,0,0,0])

def print_grid (grid):
    """Prints a board for any 2 dimensional grid assuming all rows have consistent columns"""
    #Prints the boarder
    print(f"+{'-'*len(grid[0])*5}+")
    for row in grid: #For every row, each column is mapped to a function that left aligns text to 5 spaces, and prints an empty string if 0.
        print("|"+"".join(map(lambda val: "{:<5}".format(str(str(val) if val != 0 else '')),row))+"|")
    print(f"+{'-'*len(grid[0])*5}+")

def check_lost (grid):
    """return True if there are no 0 values and there are
    adjacent values that are equal; otherwise False"""
    if str(grid).find("0")==-1:
        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[rowIndex])):
                if rowIndex==len(grid) and colIndex==len(grid[0]):
                    return False
                if len(grid[0]) != colIndex+1:
                    if grid[rowIndex][colIndex]==grid[rowIndex][colIndex+1]:
                        return False
                if len(grid) != rowIndex+1:
                    if grid[rowIndex][colIndex]==grid[rowIndex+1][colIndex]:
                        return False
        return True
    else: return False

def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise
    False"""
    #Converts to a one dimensional list and removes the square bracket
    grid=str(grid).replace("[","").replace("]","").split(",")
    #maps each vale to int to convert to integers
    grid=list(map(int, grid))
    maxNum=max(grid)
    return maxNum>=32

def copy_grid (grid):
    """return a copy of the given grid"""
    gridNew=[]
    for rowIndex in range(len(grid)):
        gridNew.append(grid[rowIndex][:])
    return gridNew

def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""
    return grid1==grid2
