#  Declare your age as integer variable

age = 28;

#  Declare your height as float variable

height = 5.4

# Declare a variable that stores complex number

complex = 1+1j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# b= input("Enter base: ")
# h= input("Enter height: ")
# print("The area of the triangle is", 0.5*int(b)*int(h))


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') > len('dragon')) #False

print('on' in 'python' and 'on' in 'dragon') #True

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon') #True

print(not('on' in 'python' and 'on' in 'dragon')) #False


# Find the length of the text python and convert the value to float and convert it to string
text = 'python'
length = len(text)
floater= float(length)
print(str(floater)) #'6.0'

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

# ------> Using the modulus operator we can check to see it there is a remainder if there is then it is not divisible by 2 else if there is no remainder we can say the number is divisible by 2

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print((7//3) == int(2.7)) #True

# Check if type of '10' is equal to type of 10

print(type('10') == type(10)) #False

# Check if int('9.8') is equal to 10

print(int('9.8') == 10)
# Generates error as 9.8 can only be type casted to a float
