# # + Using personal examples differentiate between tuple and a list
# # # In a list, you can modify, add, or remove items. for instance, if you decide to add "zain" to your
# # # network list, you can do so with network_list.append("zain").
# # lists are indexed and are written with square brackets.
# # #  List Example
# # # network_list=["mtn","airtel","glo","etisalat"]
# # # print(network_list)
# # Tuple are immutable, meaning you can't change their contents. Once you've created a tuple, 
# # # you can't add, remove, or modify elements.
# # Tuple are written with round brackets 
# # # Tuple Example
# # # grocery_tuple=("millet","beans","garri","rice")
# # # print(grocery_tuple)
# # Using examples explain string formatting
# # String formatting is way to combine string and numbers by using the format () method. The format () method takes the passed arguments formats them and places them in the string whe 
# # re the place holders {} are 
# # Example
# # Using % operator/ modulus
# name='Vivian'
# age=23
# Details='hello, %s' % name
# print(Details)
# print("%s is %d years old." %(name, age))
# # #  Using Format()method
# # print("Beauty {} in the {} of the  {} .".format('is', 'eyes', 'beholder'))
# idiom=("Not {} that {} are {}.".format('all', 'glitters', 'gold'))
# print(idiom)
# # Q3.Using X and y as variable use the following operators +*/
# # x=24
# # y=33
# # sum=(x+y)
# # print(sum)
# # x=66
# # y=22
# # div=(x/y)
# # print(div)
# # x=16
# # y=17
# # print(x*y)
# write a code to calculate the division of two numbers and round it up to the nearest whole number.
# import math

# def divide_and_round_up(num1, num2):
#     result = num1 / num2
#     rounded_up = math.ceil(result)
#     return rounded_up
# num1 = 10
# num2 = 3
# result = divide_and_round_up(num1, num2)

# print(f"The result of {num1} divided by {num2} rounded up is: {result}")