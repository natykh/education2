# input
array = [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']]

DIMENSION = len(array)





# TASK #1
# print matrix elements right-to-left and up-to-down

# order or printing
# [['_5', '_4', '_3', '_2', '_1'],
#  ['10', '_9', '_8', '_7', '_6'],
#  ['15', '14', '13', '12', '11'],
#  ['20', '19', '18', '17', '16'],
#  ['25', '24', '23', '22', '21']]

# expected output
# e d c b a j i h g f o n m l k t s r q p y x w v u

print("TASK #1")
for i in range(0, DIMENSION):
    for j in range(DIMENSION-1, 0-1, -1):
        print(array[i][j], end=' ')







# TASK #2
# print matrix elements down-to-up and left-to-right and

# order or printing
# [['_5', '10', '15', '20', '25'],
#  ['_4', '_9', '14', '19', '24'],
#  ['_3', '_8', '13', '18', '23'],
#  ['_2', '_7', '12', '17', '22'],
#  ['_1', '_6', '11', '16', '21']]

# expected
# u p k f a v q l g b w r m h c x s n i d y t o j e

print("\n\nTASK #2")
for j in range(0, DIMENSION):
    for i in range(DIMENSION-1, 0-1, -1):
        print(array[i][j], end=' ')




# TASK #3
# print matrix elements up-to-down and right-to-left

# order or printing
# [['21', '16', '11', '_6', '_1'],
#  ['22', '17', '12', '_7', '_2'],
#  ['23', '18', '13', '_8', '_3'],
#  ['24', '19', '14', '_9', '_4'],
#  ['25', '20', '15', '10', '_5']]

# expected
# e j o t y d i n s x c h m r w b g l q v a f k p u

print("\n\nTASK #3")
for j in range(DIMENSION-1, 0-1, -1):
    for i in range(0, DIMENSION):
        print(array[i][j], end=' ')

print()


