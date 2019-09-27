# how ranges work
# https://pynative.com/python-range-function/

# nested arrays (lists)
# https://snakify.org/en/lessons/two_dimensional_lists_arrays/


# input
array = [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']]

DIMENSION = len(array)

# TASK #1
# print matrix elements left-to-right and up-to-down
# (every element of the first row left to right, then next row that's below current row)

# order or printing
# [['_1', '_2', '_3', '_4', '_5'],
#  ['_6', '_7', '_8', '_9', '10'],
#  ['11', '12', '13', '14', '15'],
#  ['16', '17', '18', '19', '20'],
#  ['21', '22', '23', '24', '25']]


# expected output
# a b c d e f g h i j k l m n o p q r s t u v w x y

print("TASK #1")
for i in range(0, DIMENSION):
    for j in range(0, DIMENSION):
        print(array[i][j], end=' ')

# TASK #2
# print matrix elements up-to-down and left-to-right and

# order or printing
# [['_1', '_6', '11', '16', '21'],
#  ['_2', '_7', '12', '17', '22'],
#  ['_3', '_8', '13', '18', '23'],
#  ['_4', '_9', '14', '19', '24'],
#  ['_5', '10', '15', '20', '25']]


# expected
# a f k p u b g l q v c h m r w d i n s x e j o t y

print("\n\nTASK #2")
for j in range(0, DIMENSION):  # note  that i and j loops switched places
    for i in range(0, DIMENSION):
        print(array[i][j], end=' ')

print("\nTASK #2 (2nd solution)")
for i in range(0, DIMENSION):
    for j in range(0, DIMENSION):
        print(array[j][i], end=' ')  # now loops are in the same order, but indices switched order

# TASK #3
# print matrix elements right-to-left and down-to-up

# order or printing
# [['25', '24', '23', '22', '21'],
#  ['20', '19', '18', '17', '16'],
#  ['15', '14', '13', '12', '11'],
#  ['10', '_9', '_8', '_7', '_6'],
#  ['_5', '_4', '_3', '_2', '_1']]


# expected
# y x w v u t s r q p o n m l k j i h g f e d c b a

print("\n\nTASK #3")
for i in range(DIMENSION - 1, 0 - 1, -1):
    for j in range(DIMENSION - 1, 0 - 1, -1):
        print(array[i][j], end=' ')

# TASK #4
# print matrix elements down-to-up and right-to-left

# order or printing
# [['25', '20', '15', '10', '_5'],
#  ['24', '19', '14', '_9', '_4'],
#  ['23', '18', '13', '_8', '_3'],
#  ['22', '17', '12', '_7', '_2'],
#  ['21', '16', '11', '_6', '_1']]


# expected
# y t o j e x s n i d w r m h c v q l g b u p k f a

print("\n\nTASK #4")
for j in range(DIMENSION - 1, 0 - 1, -1):  # note  that i and j loops switched places
    for i in range(DIMENSION - 1, 0 - 1, -1):
        print(array[i][j], end=' ')

print("\nTASK #4 (2nd solution)")
for i in range(DIMENSION - 1, 0 - 1, -1):
    for j in range(DIMENSION - 1, 0 - 1, -1):
        print(array[j][i], end=' ')    # now loops are in the same order, but indices switched order

print()


