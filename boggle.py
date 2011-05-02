
import random


# list of letters on each cube
cube1 = ['A', 'A', 'C', 'I', 'O', 'T']
cube2 = ['D', 'E', 'N', 'O', 'S', 'W']
cube3 = ['A', 'B', 'I', 'L', 'T', 'Y']
cube4 = ['D', 'K', 'N', 'O', 'T', 'U']
cube5 = ['A', 'B', 'J', 'M', 'O', 'Qu']
cube6 = ['E', 'E', 'F', 'H', 'I', 'Y']
cube7 = ['A', 'C', 'D', 'E', 'M', 'P']
cube8 = ['E', 'G', 'I', 'N', 'T', 'V']
cube9 = ['A', 'C', 'E', 'L', 'S', 'R']
cube10 = ['E', 'G', 'K', 'L', 'U', 'Y']
cube11 = ['A', 'D', 'E', 'N', 'V', 'Z']
cube12 = ['E', 'H', 'I', 'N', 'P', 'S']
cube13 = ['A', 'H', 'M', 'O', 'R', 'S']
cube14 = ['E', 'L', 'P', 'S', 'T', 'U']
cube15 = ['B', 'F', 'I', 'O', 'R', 'X']
cube16 = ['G', 'I', 'L', 'R', 'U', 'W']

# list of available cubes
master_cube_list = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12, cube13, cube14, cube15, cube16]

current_cube_list = master_cube_list

# have a list of all available cubes
# as cubes are removed, pop that cube from the master list

remaining_cube_count = 16

for x in range(0, 16):
    # number of remaining cubes
    y = random.randint(0,remaining_cube_count-1)
    print str(remaining_cube_count) + ' cubes available \t ' + str(y) + ' chosen'
#    print 'list item '+str(y) + '\t ' + str(remaining_cube_count) + ' cubes remaining'
    print current_cube_list[y-1]
#    print current_cube_list
    current_cube_list.pop(y)
    remaining_cube_count = remaining_cube_count -1
    