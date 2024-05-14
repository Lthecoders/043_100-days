my2DList = [["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"]]

# print(my2DList[2][0])
"""
it works like we are tilling to print the the 2 list with a specific instricuction.

1. we are telling to that choose list number 1 in my2Dlist in order to do further operations
2. the further we hare spcificy the index in the list in order to achieve a specific element from the 2D list.

example 
IMP remeber that in 2 D list it start from 0 both vertically and horizontally

                          INDEX
                        0 1 2 3 4

list number 0          [L I S T 0]      
list number 1          [L I S T 1]
list number 2          [L I S T 2]

SO In order to print a specific element from a 2D list we have to first specify the number of list 
in that perticular 2D list with repect of starting from 0
then we have to specify the index where in the list that perticulare element is there.

it's like we are telling print from list number 2 where the index is 1
print(2Dlist[2][1])
where [2] is the number of list in the the 2D list and [1] is the index of the element which is present over there.
"""
"""
we can define 2D list as 2 or more list in a single list.
we can compare it by excle list.
"""
# for a,b,c in my2DList:
#   print(a,b)
"this for 2D loop will print the list in proper was"

my2DList = [["Johnny", 21, "Mac"], ["Sian", 19, "PC"], ["Gethin", 17, "PC"]]

# print(my2DList[0][0])
# This code outputs 'Johnny'. It's Johnny's name from list 0 (first square bracket), item 0 (second square bracket)

# print(my2DList[1][2])
# This code outputs 'PC'. It's Sian's computing preferene from list 1 (first square bracket), item 2 (second square bracket)



# following is the way we edit the 2D list
student_data=[
              ["name", "rollno", "marks"],      #list no 0
              ["nikhil",   23  ,   89.23],      #list no 1
              ['rahul' ,   24  ,   87.12],      #list no 2
              ['honey' ,   28  ,   78.23]       #list no 3
]

# (student_data[2][0])='nikhil' #first spcify the number of list in 2Dlist and then the index of the element in the list
# (student_data[1][0])='rahul'
# print(student_data[1])
# print(student_data[2])


my2DList = [ ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"] ]

# print(my2DList[0][2])


my2DList = [
             ["Johnny", 21, "Mac"],
             ["Sian", 19, "PC"],
             ["Gethin", 17, "PC"],
          ]

# print(my2DList[0][1])
"when ever you see like this print(my2DList[0][1])"
""" you always shall remeber that first it is 0 that means list number 0
then it is showing [1] that means print the element which is print at index 1 of list number 0

in simple languagae we are telling
select list number 0 that means the first list and print the index 1 element from the list

"""

my2DList =  [ ["Johnny", 21, "Mac"], # No opening square bracket
             ["Sian", 19, "PC"], # Missing , between Sian and 19. Also missing , after the square bracket for this sub-list.
             ["Gethin", 17, "PC"] ] #Extra , after this sub list - the last sub-list doesn't have a comma after it.

# print(my2DList[0][1])
