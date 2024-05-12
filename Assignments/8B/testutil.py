"""test program for grid utility functions
hussein suleman
25 april 2014"""

# grid utility routines
import util

# run test
def run_test (test):
   if test == 0:
      grid = []    
      util.create_grid (grid)
      print (len (grid))
      print (len (grid[0]))
      print (len (grid[1]))
      print (len (grid[2]))
      print (len (grid[3]))
      print (grid[0][0])
      print (grid[1][2])
      print (grid[2][1])
      print (grid[3][3])
   elif test == 1:
      grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      util.print_grid (grid)
   elif test == 2:
      grid = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
      util.print_grid (grid)
   elif test == 3:
      grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      print (util.check_lost (grid))
   elif test == 4:
      grid = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
      print (util.check_lost (grid))
   elif test == 5:
      grid = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
      print (util.check_lost (grid))
   elif test == 6:
      grid = [[4,16,2,4],[2,4,16,2],[2,4,8,4],[4,8,4,2]]
      print (util.check_lost (grid))
   elif test == 7:
      grid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
      print (util.check_lost (grid))
   elif test == 8:
      grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      print (util.check_won (grid))
   elif test == 9:
      grid = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
      print (util.check_won (grid))
   elif test == 10:
      grid = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
      print (util.check_won (grid))
   elif test == 11:
      grid = [[4,16,2,4],[2,4,16,2],[2,4,8,4],[4,8,4,2]]
      print (util.check_won (grid))
   elif test == 12:
      grid = [[2,32,2,4],[4,2,16,2],[8,0,8,4],[2,0,4,2]]
      print (util.check_won (grid))
   elif test == 13:
      grid = [[2,2,8,0],[0,8,16,0],[16,32,8,8],[2,8,4,4]]
      print (util.check_won (grid))
   elif test == 14:
      grid = [[64,32,32,2],[8,4,2,0],[4,2,0,0],[2,0,0,0]]
      print (util.check_won (grid))
   elif test == 15:
      grid = [[64,32,32,2],[8,4,2,0],[4,2,0,0],[2,0,0,0]]
      print (util.check_won (grid))
   elif test == 16:
      grid = [[128,4,0,0],[8,4,2,0],[4,2,0,2],[2,0,0,0]]
      print (util.check_won (grid))
   elif test == 17:
      grid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
      test_grid = util.copy_grid (grid)
      print (grid[0][0],test_grid[0][0])
      print (grid[1][2],test_grid[1][2])
      print (grid[3][3],test_grid[3][3])
      grid[0][0] = 64
      grid[1][2] = 64
      grid[3][3] = 64
      print (grid[0][0],test_grid[0][0])
      print (grid[1][2],test_grid[1][2])
      print (grid[3][3],test_grid[3][3])
   elif test == 18:
      grid1 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
      grid2 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
      print (util.grid_equal (grid1, grid2))
   elif test == 19:
      grid1 = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
      grid2 = [[4,2,8,2],[2,8,16,4],[16,32,8,4],[4,8,4,2]]
      print (util.grid_equal (grid1, grid2))
   elif test == 20:
      grid1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      grid2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      print (util.grid_equal (grid1, grid2))
   elif test == 21:
      grid1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      grid2 = [[2,4,8,16],[32,64,128,256],[512,1024,2048,4096],[8192,16384,32768,65536]]
      print (util.grid_equal (grid1, grid2))
   elif test == 22:
      grid1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
      grid2 = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
      print (util.grid_equal (grid1, grid2))

def run_one_test ():
   test = int (input (""))
   run_test (test)

def run_all_tests ():
   for test in range (23):
      print ("Test",test)
      run_test (test)

run_one_test ()
