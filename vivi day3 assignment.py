# Use the following in a set of code created by you if else statement, nested dictionary, while loop, for loop in both list and tuple,
# while count, while true. explain it using comment and give an example of each.
# IF ELSE STATEMENT
# If else statement is a programming construct used to make decisions based on certain conditions.
# it allows the program to execute different blocks of code based on whether a condition is true or false.
# example:

# age= 16
# age= input(" please, Enter your age:")
# age= int(age)
# if age>=16:
#     print("you are eligible to vote:")
# else:
#     print("you are not eligible to vote:")
# In this example, the program checks whether the 'age' variable is greater than or equal to 16. If it is,
# it will print "You are eligible to vote." Otherwise, it will print "You are not eligible to vote."

# NESTED DICTIONARY
# A nested is a dictionary that has another dictionary as its value. This means that values of the outer
# dictionary can be accessed using two keys.

# my_dict={
#     "Chef1":{
#         "name":"Vivian",
#         "age":12,
#         "city":"akure"
#     },
#     "Chef2":{
#         "name":"hussaini",
#         "age":29,
#         "city":"Jos"
#     }
# }
# # Accessing values in the nested dictionary
# print(my_dict["Chef1"]["name"])
# print(my_dict["Chef2"]["name"])

# WHILE LOOP
# While loop allow you to repeatedly execute a block of code as long as a given condition is true.

# count=1
# while count<=5:
#     print(count)
#     count+=1

# FOR LOOP IN BOTH LIST AND TUPLE
# For loop can be used to iterate over both lists and tuples
# For loop with a List
# my_list=[44,2,38,4,23]
# for item in my_list:
#     print(item)
# For loop with a Tuple
# my_tuple=(9,7,8,23,59)
# for item in my_tuple:
#     print(item)

# WHILE COUNT
# This counts the occurence of a specific element in a list
# my_list=[1,2,3,4,1,1,2,3,4,5]
# count the occurence of a specific element
# count=my_list.count(1)
# print(f"The count of 1 in the list is:{count}")

# WHILE TRUE
# While True is a looping construct in the Python programming language that allows a block of code to be repeated 
# indefinitely. It is often used in conjunction with a break statement, which allows the loop to be exited 
# under certain conditions

# counter = 0
# while True:
#     print("Vivian is a good girl!")
#     counter += 1
#     if counter == 10:
#         break