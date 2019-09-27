# input
array = [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']]

DIMENSION = len(array)





# TASK #1
# print matrix elements below main diagonal inclusively from up-to-down and left-to-right

# order or printing
# [['_1', '__', '__', '__', '__'],
#  ['_2', '_6', '__', '__', '__'],
#  ['_3', '_7', '10', '__', '__'],
#  ['_4', '_8', '11', '13', '__'],
#  ['_5', '_9', '12', '14', '15']]

# expected output
# a f k p u g l q v m r w s x y

# SOLUTION GOES HERE





# TASK #2
# print matrix elements below main diagonal exclusively from right-to-left and down-to-up

# order or printing
# [['__', '__', '__', '__', '__'],
#  ['10', '__', '__', '__', '__'],
#  ['_9', '_8', '__', '__', '__'],
#  ['_7', '_6', '_5', '__', '__'],
#  ['_4', '_3', '_2', '_1', '__']]

# expected output
# x w v u r q p l k f

# SOLUTION GOES HERE





# TASK #3
# print main diagonal from both sides simultaneously


# order or printing
# [['_1', '__', '__', '__', '__'],
#  ['__', '_3', '__', '__', '__'],
#  ['__', '__', '_5', '__', '__'],
#  ['__', '__', '__', '_4', '__'],
#  ['__', '__', '__', '__', '_2']]


# expected output
# a y g s m

# SOLUTION GOES HERE






# TASK #4
# print cross


# order or printing
# [['_1', '__', '__', '__', '_9'],
#  ['__', '_3', '__', '_7', '__'],
#  ['__', '__', '_5', '__', '__'],
#  ['__', '_4', '__', '__6, '__'],
#  ['_2', '__', '__', '__', '_8']]


# expected output
# a u g q m s i y e

# SOLUTION GOES HERE


print()


# order or printing
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__']]
