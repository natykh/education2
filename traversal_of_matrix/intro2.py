# input
array = [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']]

DIMENSION = len(array)

# TASK #1
# print matrix elements above main diagonal inclusively
# main diagonal is - https://www.mathdoubts.com/imgs/matrix/principal-diagonal.png

# order or printing
# [['_1', '_2', '_3', '_4', '_5'],
#  ['__', '_6', '_7', '_8', '_9'],
#  ['__', '__', '10', '11', '12'],
#  ['__', '__', '__', '13', '14'],
#  ['__', '__', '__', '__', '15']]

# expected output
# a b c d e g h i j m n o s t y

print("TASK #1")
for i in range(0, DIMENSION):
    for j in range(i, DIMENSION):
        print(array[i][j], end=' ')

# TASK #2
# print matrix elements above main diagonal exclusively

# order or printing
# [['__', '_1', '_2', '_3', '_4'],
#  ['__', '__', '_5', '_6', '_7'],
#  ['__', '__', '__', '_8', '_9'],
#  ['__', '__', '__', '__', '10'],
#  ['__', '__', '__', '__', '__']]

# expected output
# b c d e h i j n o t

print("\n\nTASK #2")
for i in range(0, DIMENSION):
    for j in range(i + 1, DIMENSION):
        print(array[i][j], end=' ')

# TASK #3
# print matrix main and secondary diagonal elements
# secondary diagonal - https://media.geeksforgeeks.org/wp-content/uploads/Secondary-Diagonal.jpg

# order or printing (main)
# [['_1', '__', '__', '__', '__'],
#  ['__', '_2', '__', '__', '__'],
#  ['__', '__', '_3', '__', '__'],
#  ['__', '__', '__', '_4', '__'],
#  ['__', '__', '__', '__', '_5']]

# order or printing (secondary)
# [['__', '__', '__', '__', '_5'],
#  ['__', '__', '__', '_4', '__'],
#  ['__', '__', '_3', '__', '__'],
#  ['__', '_2', '__', '__', '__'],
#  ['_1', '__', '__', '__', '__']]

# expected output
# a g m s y
# u q m i e

print("\n\nTASK #3 (main)")
for i in range(0, DIMENSION):
    print(array[i][i], end=' ')

print("\nTASK #3 (secondary)")
for i in range(DIMENSION-1, 0-1, -1):
    j = DIMENSION - 1 - i
    print(array[i][j], end=' ')


print()


# order or printing
# [['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__'],
#  ['__', '__', '__', '__', '__']]
