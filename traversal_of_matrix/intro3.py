# input
array = [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']]

DIMENSION = len(array)

# TASK #1
# print matrix elements left-to-right on even rows, and right-to-left on odd (snake-like traversing)

# order or printing
# [['_1', '_2', '_3', '_4', '_5'],
#  ['_9', '_8', '_8', '_7', '_6'],
#  ['10', '11', '12', '13', '14'],
#  ['19', '18', '17', '16', '15'],
#  ['20', '21', '22', '23', '24']]

# expected output
# a b c d e j i h g f k l m n o t s r q p u v w x y

print("TASK #1")
for i in range(0, DIMENSION):
    if i % 2 == 0:
        for j in range(0, DIMENSION):
            print(array[i][j], end=' ')
    else:
        for j in range(DIMENSION - 1, 0 - 1, -1):
            print(array[i][j], end=' ')

# TASK #2
# print only columns with odd indices (0,2,4,...) from down-to-up

# order or printing
# [['_5', '__', '10', '__', '15'],
#  ['_4', '__', '_9', '__', '14'],
#  ['_3', '__', '_8', '__', '13'],
#  ['_2', '__', '_7', '__', '12'],
#  ['_1', '__', '_6', '__', '11']]

# expected output
# u p k f a w r m h c y t o j e

print("\n\nTASK #2")
for j in range(0, DIMENSION):
    if j % 2 == 0:
        for i in range(DIMENSION - 1, 0 - 1, -1):
            print(array[i][j], end=' ')

# TASK #3
# print right-bottom quadrant exclusively and inclusively (left-to-right, up-to-down)

# order or printing (exclusively)
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '_1', '_2'],
#  ['__', '__', '__', '_3', '_4']]

# order or printing (inclusively)
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '_1', '_2', '_3'],
#  ['__', '__', '_4', '_5', '_6'],
#  ['__', '__', '_7', '_8', '_9']]

# expected output
# s t x y
# m n o r s t w x y


print("\n\nTASK #3 (exclusively)")
for i in range(0, DIMENSION):
    for j in range(0, DIMENSION):
        if i >= DIMENSION / 2 and j >= DIMENSION / 2:
            print(array[i][j], end=' ')

print("\nTASK #3 (inclusively)")
for i in range(0, DIMENSION):
    for j in range(0, DIMENSION):
        if i >= int(DIMENSION / 2) and j >= int(DIMENSION / 2):
            print(array[i][j], end=' ')

print()

# order or printing
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__']]
