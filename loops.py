# for i in range(5):
#     if i == 3:
#         break
#     else:
#         print "i=" + str(i)


#i = 0

#while i < 10:

    #print "a"
   # print "b"
  #  if i % 2 == 0:
 #    print "c"

#print "hello"
    # if i == 3:
    #     break
    # else:
    #     print "i=" + str(i)
    # i = i + 1
#
#
# x = raw_input("Say your name: ")
# print "Hello " + x

# EXCERCISE 1

a = 10

# s = "aSDasdas"
# C = 'ADadfasdf'
# print chr(50)
#
# if a > 5 and a < 20:
#         if a != 7 and a != 13:
#                print "hello"
#
#
# if a > 5 and a < 20 and a != 7 and a != 13:
#     print "Hello"
#
#
# if a in range(5, 11) and a != 7 and a != 13:la
#     print "ZZZ"

#
# # EXCERCISE 2
#
#
# color = "red"
# a = 1
# is_allowed = True
#
# if color == "red" and a > 5 and is_allowed:
#          print "Hello Jane"
#
#
# # EXCERCISE 3
#
# a = 2
# color = "pink"
#
# if a > 0 and color == "pink":
#     print "Hello mum"
# elif a < 0 and color != "green":
#     print "Hello Dad"
# elif a == 0 and color == "":
#     print "Hello everyone"
#
# # EXCERCISE 4
#
# color = "brown"
#
# if color == ("brown" or "violet" or "yellow"):
#     print "Hello Daniel"
#
# # EXCERCISE 5
#
# if not False:
#     print "hello didus"
#
#
# #Excercise 6
#
# x = 11
#
# if x %2 == 0:
#     color = "Dark"
# else:
#     color = "Light"
# if color == "Dark":
#     print "Its nighttime"
# else:
#     print "Its daytime"

#EXCERCISES - ARRAYS/LISTS

# Excercise 1
#
# list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
# for x in list:
#     if x % 4 == 0:
#         print "Number is divisible by 4"
#

# Excercise 2
#
# list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
# for x in list:
#     if x != 0:
#         if 30 % x == 0:
#             print "Divisor of 30"
#     else:
#          print "Action not allowed"

#Excercise 3

list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
for x in list:
    if x >= 0:
        print x
    else:
        break

print "________________________"

# #Excercise 4
#
# list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
# for x in list:
#     while x >0:
#         print x

print "________________________"

#Excersice 5

list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
N = 4
for x in list:
    print [x] * 4


print "________________________"

#Excercise 6

list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
list.reverse()
print list

print "________________________"

#Excercise 7

list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
print list [::2]


list = [2, 44, 15, 84, 3, -1, 0, 10, 15]
print list [::3]

