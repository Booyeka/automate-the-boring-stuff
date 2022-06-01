


#rotate the picture grid clockwise 90 degrees




grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.'],
]



#displaying grid in console properly
def to_display(value):

#  for i in value:
#      print(i, end ='\n')
    
    for list in value:
        for place in list:
            print(place, end='')
        
        print('')


def to_90cw_rotate(array):
    
    rotated_grid = []

    for list in range(len(array[0])):
        rotated_grid.append([])

        for char in range(len(array)):
            rotated_grid[list].insert(0,array[char][list])

    return rotated_grid

def to_180cw_rotate(array):
    return to_90cw_rotate(to_90cw_rotate(array))
    

def to_270cw_rotate(array):
    return to_90cw_rotate(to_180cw_rotate(array))

def to_360cw_rotate(array):
    return to_90cw_rotate(to_270cw_rotate(array))



to_display(grid)


print('How many degrees would you like me to rotate this clockwise? (90/180/270/360)')
num = int(input())

if num == 90:
    rotate = to_90cw_rotate(grid)
elif num == 180:
    rotate = to_180cw_rotate(grid)
elif num == 270:
    rotate = to_270cw_rotate(grid)
else:
    rotate = to_360cw_rotate(grid)

#for i in range(int(num)):
#    if i == 0:
#        val = to_cw_rotate(grid)
#    else:
#        val = to_cw_rotate(val)

#print(f'Let me rotate that for you {num} times')        

to_display(rotate)