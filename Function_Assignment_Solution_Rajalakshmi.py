                # Python programs - Function

#Qn
# Define a function calls addNumber(x, y) that takes in two number 
#and returns the sum of the two numbers.

#Solution

#Function definition of function that returns the sum of the two numbers
def addNumber(num1,num2):
    return (num1+num2)

# Getting two numbers from user
x=int(input("Enter a number"))
y=int(input("Enter a number"))

#Computing sum of numbers using addNumber function
print("Sum of numbers is:",addNumber(x,y))



# Qn
# Define a function calls subtractNumber(x, y) that takes in two numbers and
# returns the difference of the two numbers.

# Solution

# Function definition of function that returns the difference of the two numbers.
def subNumber(num1, num2):
    return (num1 - num2)


# Getting two numbers from user
x = int(input("Enter a number"))
y = int(input("Enter a number"))

# Computing difference of numbers using subNumber function
print("Difference of numbers is:", subNumber(x, y))



# Qn
# Write a function getBiggerNumber(x, y) that takes in two numbers as arguments
# and returns the bigger number.

# Solution
# Function definition of function that returns the bigger number.
def get_bigger_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Getting two numbers from user
x = int(input("Enter a number"))
y = int(input("Enter a number"))

# Computing bigger numbers using getBiggerNumber function
print("Bigger numbers is:", get_bigger_number(x, y))



# Qn
# Python provides many built-in modules with many useful functions.
# One such module is the math module. The math module provides many
# useful functions such as sqrt(x), pow(x, y), ceil(x), floor(x) etc.
# You will need to do a "import math" before you are allowed to use
# the functions within the math module.


import math
# Calculate the square root of 16 and stores it in the variable a
a = math.sqrt(16)
print("Square root of 16 is", a)

# Calculate 3 to the power of 5 and stores it in the variable b
b = math.pow(3, 5)
print("3 to the power of 5 is", b)

# Calculate area of circle with radius = 3.0 by making use of the math.pi
# constant and store it in the variable c
radius = 3.0
c = math.pi * radius * radius
print("Area of circle is", c)



# Qn
# Write a function to convert temperature from Celsius to Fahrenheit scale.
# oC to oF Conversion: Multiply by 9, then divide by 5, then add 32.

# Note: Return a string of 2 decimal places.
# In - Cel2Fah(28.0)
# Out - '82.40'
# In - Cel2Fah(0.00)
# Out - '32.00'

#Function to convert Celsius to Fahrenheit
def cel2fah(ip_temp):
    fah_temp = (ip_temp * (9 / 5)) + 32
    return round(fah_temp, 2)


# Getting temperature from user
temperature = int(input("Enter a celsius temperature"))

# Converting temperature from Celsius to Fahrenheit scale
print("Celsius temperature is:",temperature,"equivalent Fahrenheit scale is:", cel2fah(temperature))



#Qn
# Write a function to compute the BMI of a person.
#     BMI = weight(kg)  /  ( height(m)*height(m) )
# Note: Return a string of 1 decimal place.
# In - BMI(63, 1.7)
# Out - '21.8'
# In - BMI(110, 2)
# Out - '27.5'

#Solution
#function to compute the BMI of a person.
def computeBMI(weight,height):
    return round(weight/(height*height),1)

# Getting weight and height from user
x = eval(input("Enter the weight in kg"))
y = eval(input("Enter the height in metre"))

# Computing BMI using computeBMI function
print("BMI is:", computeBMI(x, y))



#Qn
# Write a function percent(value, total) that takes in two numbers as arguments,
# and returns the percentage value as an integer.
# In - percent(46, 90)
# Out - 51
# In - percent(51, 51)
# Out - 100
# In - percent(63, 12)
# Out - 525


#Solution

import math
#function to compute the percentage value as an integer
def compute_percentage(value,total):
    return math.trunc((value * 100)/total)

# Getting weight and height from user
num1 = eval(input("Enter the value"))
num2 = eval(input("Enter the total"))

# Computing percentage value using compute_percentage function
print("Percentage is:", compute_percentage(num1, num2))



#Qn
# Write a function to compute the hypotenuse given sides a and b of the triangle.
# Hint: You can use math.sqrt(x) to compute the square root of x.
# In - hypotenuse(3, 4)
# Out - 5
# In - hypotenuse(5, 12)
# Out - 13

# #Solution

import math
#function to compute the hypotenuse given sides a and b of the triangle
def compute_hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)

# Getting sides from user
num1 = eval(input("Enter length of one side of triangle"))
num2 = eval(input("Enter length of another side"))

# Computing hypotenuse value using compute_hypotenuse function
print("Hypotenuse is:", compute_hypotenuse(num1, num2))


# Qn
# Write a function getSumOfLastDigits() that takes in a list of positive numbers and
# returns the sum of all the last digits in the list.
# getSumOfLastDigits([2, 3, 4])
# 9
# getSumOfLastDigits([1, 23, 456])
# 10

# Solution
# Function to return sum of all the last digits in the list.
def getSumOfLastDigits(lst):
    result = 0
    for i in lst:
        result += int(i % 10)

    return result


# Getting list from user
my_lst = eval(input("Enter a list of numbers"))

# Function call to compute sum of last digits of number in list using getSumOfLastDigits function
print("Sum of last digits of number is:", getSumOfLastDigits(my_lst))



#Qn
# Write a function that uses a default value.
# In - introduce('Lim', 20)
# Out - 'My name is Lim. I am 20 years old.'
# In - introduce('Ahmad')
# Out - 'My name is Ahmad. My age is secret.'

#Solution
def introduce(name,age=". My age is secret."):
    if str(age).isnumeric():
        print("My name is",name,"I am",age,"years old")
    else:
        print("My name is", name,age)


introduce('Lim', 20)
introduce('Ahmad')


# Qn
# Write a function isEquilateral(x, y, z) that accepts the 3 sides of a triangle as arguments. 
# The program should return True if it is an equilateral triangle.
# In - isEquilateral(2, 4, 3)
# False - False
# In - isEquilateral(3, 3, 3)
# Out - True
# In - isEquilateral(-3, -3, -3)
# Out - False

#function to check whether it is equilateral triangle
def check_equilateral(x, y, z):
    # check whether it is a valid triangle
    if (x + y <= z) or (x + z <= y) or (y + z <= x):
        return False
    else:
        if x == y == z:
            return True
        else:
            return False


# Getting sides from user
num1 = eval(input("Enter length of one side of triangle"))
num2 = eval(input("Enter length of second side"))
num3 = eval(input("Enter length of third side"))

#check whether it is equilateral triangle using check_equilateral function
print("Are these sides of an equilateral triangle?:", check_equilateral(num1, num2, num3))



#Qn
# For a quadratic equation in the form of ax2+bx+c, the discriminant, D is b2-4ac. Write a function to
#compute the discriminant, D.
# In - quadratic(1, 2, 3)
# Out - 'The discriminant is -8.'
# In - quadratic(1, 3, 2)
# Out - 'The discriminant is 1.'
# In - quadratic(1, 4, 4)
# Out - 'The discriminant is 0.'

#Solution

import math

# function for finding roots
def compute_discriminant(a, b, c):

    discriminant = b * b - 4 * a * c
    return discriminant



# Getting coefficient from user
num1 = eval(input("In the quadriatic eq ax2+bx+c, Enter value of a"))
num2 = eval(input("Enter value of b"))
num3 = eval(input("Enter value of c"))

# If a is 0, then incorrect equation
if num1 == 0:
    print("Input incorrect for quadratic equation")

else:
    #Computing discriminant using compute_discriminant function
    print("The discriminant is",compute_discriminant(num1,num2,num3))



#Qn
# Define a function calls addFirstAndLast(x) that takes in a list of numbers and
# returns the sum of the first and last numbers.
# In - addFirstAndLast([])
# Out - 0
# In - addFirstAndLast([2, 7, 3])
# Out - 5
# In - addFirstAndLast([10])
# Out - 10

# Function to compute sum of first and last number
def addFirstAndLast(lst):
    if not lst:
        print("0")
    elif len(lst) == 1:
        print(lst[0])
    else:
        print(lst[0] + lst[-1])

#Getting list from user
my_lst = eval(input("Enter a list of numbers"))

# Function call to compute sum of first and last number using addFirstAndLast function
addFirstAndLast(my_lst)


#Qn
# Complete the 'lambda' expression so that it returns True if the 
#argument is an even number, and False otherwise.

#Solution
(lambda num: "True" if num % 2 == 0 else "False")(6)


#Qn
# Get the documentation of below function

#Solution
"""Student final score calculator

This script computes the final score of each of the student and prints it.
First the script gets the student information which includes the student name 
and marks in five subjects.It then computes then final score

This script contains the following functions:

    * getScore - computes then final score of each of the student and prints it.
    * main - the main function of the script"""


def getScore(ip_dict):
    """getScore is a function that computes and returns the final score.

    Parameters
    ----------
    ip_dict : dict
        Dictionary containing student name and marks in 5 subjects(English , Hindi , Maths , Science and Social) """

    for key, inner_dict in ip_dict.items():
        final_score = 0
        for inner_key, values in inner_dict.items():
            final_score += int(values)

        print(key, "'s final score is:", final_score)


def main():
    print("This script computes the final score of each of the student and prints it using getScore() function")
    print("Documentation Using __doc__:")
    print(getScore.__doc__)

    print("Using help:")
    help(getScore)
    main_dict = {}
    lst = []

    no_of_entry = eval(input("Enter number of students' information that you wish to add"))
    # Creating dictionary using user input
    for i in range(no_of_entry):
        key = input("Enter the name of student")
        values = input("Enter marks in English, Hindi, Maths,Science and Social separated by comma ','")
        lst = values.split(',')
        inner_dict = {'English': lst[0], 'Hindi': lst[1], 'Maths': lst[2], 'Science': lst[3], 'Social': lst[4]}
        main_dict[key] = inner_dict
        lst.clear()

    print(main_dict)

    getScore(main_dict)


main()


# Qn
# In Python, it is possible to pass a function as a argument to another function.
# Write a function useFunction(func, num) that takes in a function and a number as arguments.
# The useFunction should produce the output shown in the examples given below.
# def addOne(x):
#   return x + 1
# useFunction(addOne, 4)
# 25
# useFunction(addOne, 9)
# 100
# useFunction(addOne, 0)
# 1

#Solution
#Function to add one to the number
def addOne(x):
    return x + 1


#Function which calls addOne along with number as argument
def useFunction(addOne, num):
    return addOne(num)


#Getting input from user
num1=int(input("Enter a number"))

#Getting result by calling useFunction function
print("Result is:",useFunction(addOne, num1))


# Qn
# Write a function find_max that accepts three numbers as
# arguments and returns the largest number among three.
# Write another function main, in main() function accept
# three numbers from user and call find_max.

# Solution
# Function for finding maximum of three numbers
def find_max(a, b, c):
    if (a > b) & (a > c):
        return a
    elif (b > a) & (b > c):
        return b
    else:
        return c


# Outer main function
def main():
    # Inner main function
    def main():
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))
        num3 = int(input("Enter third number"))
        
        # Getting biggest number and printing it
        print("Biggest number is", find_max(num1, num2, num3))

    # Calling inner main
    main()


# Calling outer main
main()


#Qn
# Write a function, is_vowel that returns the value true if a given character is a vowel,
# and otherwise returns false.
# Write another function main, in main() function accept a string from user and count number
# of vowels in that string.

#Solution
# Function for finding whether character is vowel
def is_vowel(ip_char):
    vowel_lst=['a','e','i','o','u']

    if ip_char.lower() in vowel_lst:
        return True
    else:
        return False



#Outer main function
def main():
    # Inner main function
    def main():
        #Getting input from user
        inp_char = str(input("Enter a character"))

       # Checking if character is vowel and printing it
        print(f"Is '{inp_char}' a vowel?:",is_vowel(inp_char) )

    # Calling inner main
    main()


# Calling outer main
main()


# Qn
# Write a function named is_prime, which takes an integer as an argument and returns true
# if the argument is a prime number, or false otherwise.
# Also, write the main function that displays prime numbers between 1 to 500.

# #Solution
# Function for finding whether number is prime
def is_prime(ip_num):
    if ip_num > 1:
        for i in range(2, ip_num - 1):
            if (ip_num % i) == 0:
                return False

        else:
            return True

    else:
        return False


# The main function
def main():
    # Getting input from user
    inp_val = int(input("Enter a number"))
    # Checking if number is prime and printing it
    print(f"Is '{inp_val}' a prime number?:", is_prime(inp_val))

    # Printing prime numbers from 1 to 500
    print("Prime numbers from 1 to 500 are:")
    print(1)
    for j in range(2, 500):
        for i in range(2, j - 1):
            if (j % i) == 0:
                break
        else:
            print(j)


# Calling the main function
main()


#Qn
# Write a function in python to find the sum of the cube of elements in a list.
# The list is received as an argument to the function, in turn, the function must return the sum.
# Write the main function which invokes the above function.

# #Solution
# Function for finding sum of cube of elements
def sum_of_cube_of_nums(ip_lst):
    sum =0
    for i in ip_lst:
        sum +=(i ** 3)

    return sum

# The main function
def main():
    # Getting input from user
    inp_val = eval(input("Enter a list of numbers"))

    # Getting Sum of cube of elements using sum_of_cube_of_nums fn
    print("Sum of cube of elements is:", sum_of_cube_of_nums(inp_val))

# Calling the main function
main()


#Qn
# Write the definition of a function zero_ending(scores) to add all those values in the list of scores,
# which are ending with zero and display the sum.
# For example: If the scores contain [200, 456, 300, 100, 234, 678] The sum should be displayed as 600


# #Solution
# Function to add all those values in the list of scores which are ending with zero
def zero_ending(ip_lst):
    sum =0
    for i in ip_lst:
        if(i % 10==0):
            sum +=(i)

    return sum

# The main function
def main():
    # Getting input from user
    inp_val = eval(input("Enter a list of scores (Integer numbers)"))

    # Getting to add all those values in the list of scores which are ending with zero
    print("Sum of all those values in the list of scores which are ending with zero is:", zero_ending(inp_val))

# Calling the main function
main()


# Qn
# Write a definition of a method count_now(places) to find and display those place names,
# in which there are more than 5 characters.

# For example :
# If the list places contains
# ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]
# The following should get displayed :
# LONDON
# NEW YORK

#Function to print places that are more than 5 chars
def count_now(ip_lst):
    for i in ip_lst:
        if len(i) > 5:
            print(i)


# The main function
def main():
    # Getting input from user
    inp_val = eval(input("Enter a list of places"))

    # Getting to print places that are more than 5 chars with count_now function
    print("Places that have more than 5 characters are:")
    count_now(inp_val)


# Calling the main function
main()


#Qn
# Write a method in python to display the elements of list thrice if it is a number and display
# the element terminated with ‘#’ if it is not a number.

# For example, if the content of list is as follows :
# ThisList=[‘41’,‘DROND’,‘GIRIRAJ’, ‘13’,‘ZARA’]
# The output should be
# 414141
# DROND#
# GIRIRAJ#
# 131313
# ZARA#

#Solution
#Function to alter the list
def alter_str(ip_lst):
    for i in ip_lst:
        if i.isnumeric():
            print(i*3)
        else:
            i +='#'
            print(i)


#lst=['41','DROND','GIRIRAJ', '13','ZARA']

# Getting input from user
inp_val = eval(input("Enter a list"))

print("Altered list is:")
alter_str(inp_val)


# Qn
# For a given list of values in descending order, write a method in python to search
# for a value with the help of Binary Search method.
# The method should return position of the value and should return -1 if the value not present in the list.

# Solution
def binary_search(ip_lst, search_num):
    low = 0
    high = len(ip_lst) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If search_num is greater, ignore left half
        if ip_lst[mid] < search_num:
            low = mid + 1

        # If search_num is smaller, ignore right half
        elif ip_lst[mid] > search_num:
            high = mid - 1

        # means search_num is present at mid
        else:
            return mid

    # If element is not present then return -1
    return -1


inp_val = [5000, 200, 30, 24, 10, 4]
print("Original list is", inp_val)
print("Sorted list is", sorted(inp_val))

# Getting input from user
search_num = int(input("Enter a number to search in the list"))

# Function call
result = binary_search(sorted(inp_val), search_num)

if result != -1:
    print(f"Element '{search_num}' is present at index", str(result))
else:
    print(f"Element '{search_num}' is not present in array")


# Qn
# Write a function half_and_half that takes in a list and change the list
# such that the elements of the second half are now in the first half.
# For example, if the size of list is even and content of list is as follows :
# my_liist = [10,20,30,40,50,60]
# The output should be
# [40,50,60,10,20,30]
# if the size of list is odd and content of list is as follows :
# my_liist = [10,20,30,40,50,60,70]
# The output should be
# [50,60,70,40,10,20,30]

# Solution
import math

#function half_and_half to swap first and second half of list
def half_and_half(my_list):
    new_list = [0] * (len(my_list) - 1)
    half_length = math.ceil(len(my_list) / 2)

    new_list[:half_length] = my_list[half_length:]

    if len(my_list) % 2 != 0:
        new_list[half_length - 1] = my_list[half_length - 1]
        new_list[half_length:] = my_list[:half_length - 1]
    else:
        new_list[half_length:] = my_list[:half_length]

    print("Altered list is",new_list)


# Getting input from user
inp_val = eval(input("Enter a list of numbers"))

#Calling function half_and_half to swap first and second half of list
half_and_half(inp_val)


# Qn
# Write a function that accepts a dictionary as an argument. If the dictionary contains replicate values,
# return an empty dictionary, otherwise, return a new dictionary whose values are now the keys and whose
# keys are the values.

#Solution
def alter_dict(ip_dict):
    new_dict = {}

    val_lst = list(ip_dict.values())

    for i in range(len(val_lst)):
        if val_lst[i] in val_lst[i + 1:]:
            print("Dictionary contains duplicate values")
            return new_dict

    for old_key, old_value in ip_dict.items():
        new_value = old_key
        new_key = old_value
        if new_key not in new_dict.keys():
            a = new_dict.setdefault(new_key, list(new_value))
        else:
            new_dict[new_key].append(new_value)

    return new_dict


# Getting input from user
inp_val = eval(input("Enter a dictionary"))
#
# Calling alter_dict function
print("New dictionary is", alter_dict(inp_val))




