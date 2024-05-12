"""2048 game
hussein suleman
25 april 2014"""

# random number generator
import random
# grid utility routines
import util
# grid value merging routines
import push

def add_block (grid):
    """add a random number to a random location on the grid"""
    # set distributon of number possibilities
    options = [2,2,2,2,2,4]
    # get random number
    chosen = options[random.randint(0,len(options)-1)]
    found = False
    while (not found):
        # get random location
        x = random.randint (0, 3)
        y = random.randint (0, 3)
        # check and insert number
        if (grid[x][y] == 0):
            grid[x][y] = chosen
            found = True

def play ():
    """generate grid and play game interactively"""
    # create grid
    grid = []
    util.create_grid (grid)
    # add 2 starting random numbers
    add_block (grid)
    add_block (grid)
    won_message = False
    while (True):
        util.print_grid (grid)
        key = input ("Enter a direction:\n")
        if (key in ['x', 'u', 'd', 'l', 'r']):
            # make a copy of the grid
            saved_grid = util.copy_grid (grid)
            if (key == 'x'):
                # quit the game
                return
            # manipulate the grid depending on input
            elif (key == 'u'):
                push.push_up (grid)
            elif (key == 'd'):
                push.push_down (grid)
            elif (key == 'r'):
                push.push_right (grid)
            elif (key == 'l'):
                push.push_left (grid)
            # check for a grid with no more gaps or legal moves
            if util.check_lost (grid):
                print ("Game Over!")
                return
            # check for a grid with the final number
            elif util.check_won (grid) and not won_message:
                print ("Won!")
                won_message = True
            # finally add a random block if the grid has changed    
            if not util.grid_equal (saved_grid, grid):
                add_block (grid)

# initialize the random number generator to a fixed sequence
random.seed (12)
# play the game
play ()
