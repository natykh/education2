# input
array = [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']]

DIMENSION = len(array)






# TASK #1
# print matrix elements right-to-left and down-to-up on even rows, and up-to-down on odd (snake-like traversing)

# order or printing
# [['25', '16', '15', '_6', '_5'],
#  ['24', '17', '14', '_7', '_4'],
#  ['23', '18', '13', '_8', '_3'],
#  ['22', '19', '12', '_9', '_2'],
#  ['21', '20', '11', '10', '_1']]

# expected output
# y t o j e d i n s x w r m h c b g l q v u p k f a

print("TASK #1")
for j in range(DIMENSION - 1, 0 - 1, -1):
    if j % 2 == 0:
        for i in range(DIMENSION - 1, 0 - 1, -1):
            print(array[i][j], end=' ')
    else:
        for i in range(0, DIMENSION):
            print(array[i][j], end=' ')






# TASK #2
# print from up-to-down row and
# 1) on even rows print elements from right-to-left and only elements on even positions
# 1) on odd rows print elements from left-to-right and only elements on odd positions

# order or printing
# [['_3', '__', '_2', '__', '_1'],
#  ['__', '_4', '__', '_5', '__'],
#  ['_8', '__', '_7', '__', '_6'],
#  ['__', '_9', '__', '10', '__'],
#  ['13', '__', '12', '__', '11']]

# expected output
# e c a g i o m k q s y w u

print("\n\nTASK #2")
for i in range(0, DIMENSION):
    if i % 2 == 0:
        for j in range(DIMENSION - 1, 0 - 1, -1):
            if j % 2 == 0:
                print(array[i][j], end=' ')
    else:
        for j in range(0, DIMENSION):
            if j % 2 == 1:
                print(array[i][j], end=' ')






# TASK #3
# print shown below quadrants

# order or printing
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['_1', '_3', '__', '__', '__'],
#  ['_2', '_4', '__', '__', '__']]

# order or printing
# [['__', '__', '_9', '_6', '_3'],
#  ['__', '__', '_8', '_5', '_2'],
#  ['__', '__', '_7', '_4', '_1'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__']]

# expected output
# p u q v
# o j e n i d m h c


print("\n\nTASK #3.1")
for j in range(0, DIMENSION):
    for i in range(0, DIMENSION):
        if i >= DIMENSION / 2 and j < int(DIMENSION / 2):
            print(array[i][j], end=' ')

print("\nTASK #3.2")
for j in range(DIMENSION - 1, int(DIMENSION / 2)-1, -1):    # note that we can not only check condition inside the loop
    for i in range(int(DIMENSION / 2), 0-1,  -1):           # but also play with loop boundaries. this solution
        print(array[i][j], end=' ')                         # is more efficient and should be preferred when possible

print()

# order or printing
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__']]
