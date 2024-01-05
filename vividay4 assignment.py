# Explain the for statement and give 3 examples using the for statement
# For statement is a control flow statement that is used to repeatedly execute a block of code 
# based on a specified condition. It allows iterating over a sequence, such as a list or a range of numbers, and 
# can also be used to iterate over the characters in a string.
# EXAMPLES
# Iterating over a list:
fruits=["strawberry","mango","apple"]

for fruit in fruits:
    print(fruits)
# # Iterating over a range of numbers:
# for num in range(1,6):
#     print(num)
# # Iterating over a string:
# string="Hello, Vivian!"
# for char in string:
#     print(char)
# # 2: Create 3 different set of codes using the def and lambda function each (make each one with string, integers/floats, list respectively).

# # In the examples below, the def keyword is used to define a function with a name, while the lambda is used to define an anonymous function. 

# # Similarities btw def and lambda:
# # Both def and lambda functions can take argurments and return a result. 

# # Difference btw def and lambda
# # The main difference btw the two functions is that, "lambda" functions are limited to a single expression and cannnot include statements, 
# # While "def" functions can include multiple lines of code and statements.

# # Set 1: Working with Strings

# 1. Using def function:

# def advent_strings(str1, str2):
#     return str1 + str2

# print(advent_strings("Hello, Class! ", "Good Morning, and welcome to today's presentation."))

# # # # 2. Using lambda function:
    
# advent_strings = lambda str1, str2: str1 + str2
# print(advent_strings("Hello, Class! ", "Good Morning, and welcome to today's presentation."))

# # # Set2: Working with Integers/Floats

# # # 1. Using def function:

# def multiply_numbers(num1, num2):
#     return num1 * num2

# print(multiply_numbers(6, 9))

# # # # # 2. Using lambda function:
    
# multiply_numbers = lambda num1, num2: num1 * num2

# print(multiply_numbers(6, 9))

# # # # Set3: Working with Lists

# # # # 1. Using def function:

# def add_figures(set, figures):
#     set.append(figures)
#     return set

# print(add_figures([1, 2, 3, 4], 5))

# # # # # 2. Using lambda function:
    
# add_figures = lambda set, figures: set + [figures]

# print(add_figures([1, 2, 3, 4], 5))



