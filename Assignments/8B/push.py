#Abdul-Kader Jainoodien
#JNDABD002
#Tool to push numbers in 2048 game

def merger(oneD, zeros="end"):#Takes a 1D slice of the grid to do moving and merging of anyvmovement
    def zerosHandler(): #This removes zeros of present, and adds zeros to the end if the length is incorrect.
        while 0 in oneD:
            oneD.remove(0)
        while len(oneD)<4:
            oneD.append(0)
    
    def mergerShifter(index, shift):
        if oneD[index]==oneD[index+shift]: #If the current number and next are the same (using index and our stating position)
            if index+shift==-1: #Prevents first and last item in the list from merging ilegally (negative positions)
                return
            oneD[index+shift]=oneD[index+shift]*2 #Double the vale.
            oneD[index]=0 #Removes the merged value from calculating further merges
            oneD.insert(index, 0)
            oneD.insert(index+shift, 0)


    zerosHandler()
    for count in range(3, -1, -1): #We shift our staring position to the right every loop, so we hav less to iterate over.
        if zeros=="start":
            for index in range(count, -1, -1):
                mergerShifter(index, -1)
        else: 
            for index in range(count):
                mergerShifter(index, 1)
                
    zerosHandler()
    if zeros=="start" and 0 in oneD:
        oneD=oneD[::-1]
        zerosHandler()
        oneD=oneD[::-1]
    
    

    return oneD

def push_up (grid):
    """merge grid values upwards"""
    for columIndex in range(4):
        oneD=list(oneD[columIndex] for oneD in grid) #Makes a list by taking the interested column from each row
        #Replace grid places from the list returned from merger()
        grid[0][columIndex], grid[1][columIndex], grid[2][columIndex], grid[3][columIndex]=merger(oneD)
    return grid
    
def push_down (grid):
    """merge grid values downwards"""
    for columIndex in range(4):
        oneD=list(oneD[columIndex] for oneD in grid) #Makes a list by taking the interested column from each row.
        #Replace grid places from the list returned from merger()
        grid[0][columIndex], grid[1][columIndex], grid[2][columIndex], grid[3][columIndex]=merger(oneD, zeros="start") #Reverses the list to correct from merger() reversal of input.
    return grid
    
def push_left (grid):
    """merge grid values left"""
    for rowIndex in range(4):
        oneD=grid[rowIndex] #Takes the row
      #Replace grid places from the list returned from merger()
        grid[rowIndex][0], grid[rowIndex][1], grid[rowIndex][2], grid[rowIndex][3]=merger(oneD)
    return grid

def push_right (grid):
    """merge grid values right"""
    for rowIndex in range(4):
        oneD=grid[rowIndex] #Takes the row
        #Replace grid places from the list returned from merger()
        grid[rowIndex][0], grid[rowIndex][1], grid[rowIndex][2], grid[rowIndex][3]=merger(oneD, zeros="start")
    return grid
