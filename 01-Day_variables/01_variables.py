# Day 1: 30 Days of python programming
import math
# Variable Declaration

first_name = "Brian"
last_name = "Lusigi"
full_name = "Brian Lusigi"
country = "Kenya"
city ="Nairobi"
age = 28
year = 2008
is_married = True
is_true = True
is_light_on = False


# Multiline variable
item_name, item_price, item_quantity = "Laptop", 25, 30

# Our Types
print(type(first_name)) #str
print(type(last_name)) #str
print(type(full_name)) #str
print(type(country)) #str
print(type(city)) #str
print(type(age)) #int
print(type(year)) #int
print(type(is_married)) #bool
print(type(is_true)) #bool
print(type(is_light_on)) #bool

# Built in len()
print(len(first_name)) #5

#Comparison operator
print(len(first_name) == len(last_name)) #False

#Arithmetic ops

num_one = 5
num_two = 4


total = num_one + num_two #9
diff = num_one - num_two #1
product = num_one * num_two #20
division = num_one / num_two #1
remainder = print(num_one % num_two) #1
exp = print(num_one**num_two) #625
floor_division = print(math.floor(num_one/num_two)) #1

#Radius is 30m
area_of_circle = 3.14 * 30 *30
print(area_of_circle) #2826.0

circum_of_circle = 2*3.14*30
print(circum_of_circle)#188.4

# radius = input("What is the radius? :")
# area = 3.14 * int(radius)**2
# print(area)




