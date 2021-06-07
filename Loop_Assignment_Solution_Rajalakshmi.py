                        # Python - Loop 

# Qn
# # W. A P. which takes one number from 0 to 9 from the user and prints
# it in the word. And if the word is not from 0 to 9 then
# it should print that number is outside of the range and program should
# exit.
# For example:-
# input = 1
# output = one

# Solution
while True:
    var3 = eval(input("Enter a number between 0 to 9"))
    if (var3 < 10) and (var3 > -1):
        if var3 == 0:
            print("Zero")
        elif var3 == 1:
            print("One")
        elif var3 == 2:
            print("Two")
        elif var3 == 3:
            print("Three")
        elif var3 == 4:
            print("Four")
        elif var3 == 5:
            print("Five")
        elif var3 == 6:
            print("Six")
        elif var3 == 7:
            print("Seven")
        elif var3 == 8:
            print("Eight")
        elif var3 == 9:
            print("Nine")
    else:
        print("Number is outside of the range")
        break

        

# Qn
# W. A P. to implement calculator but the operation to be done and two
# numbers will be taken as input from user:-
# Operation console should show below:-
# Please select any one operation from below:-
# * To add enter 1
# * to subtract enter 2
# * To multiply enter 3
# * To divide enter 4
# * To divide and find quotient enter 5
# * To divide and find remainder enter 6
# * To divide and find num1 to the power of num2 enter 7
# * To Come out of the program enter 8

# Solution
print('Welcome to Calculator App')
var1 = eval(input("Enter first integer number"))
var2 = eval(input("Enter second integer number"))

while True:
    print('''Select a number between [1-8] for operations
    Number -> Operation
    -------------------
        1 -> Addition
        2 -> Subtraction
        3 -> Multiplication
        4 -> Division
        5 -> To divide and find quotient
        6 -> To divide and find remainder
        7 -> To find num1 to the power of num2
        8 -> Exit''')
    var3 = eval(input("Enter a number between 1 to 8"))
    if (var3 < 9) and (var3 > 0):
        if var3 == 1:
            print("Addition of", var1, "and", var2, "is:", var1 + var2)
        elif var3 == 2:
            print("Subtraction of", var1, "and", var2, "is:", var1 - var2)
        elif var3 == 3:
            print("Multiplication of", var1, "and", var2, "is:", var1 * var2)
        elif var3 == 4:
            print("Division of", var1, "and", var2, "is:", var1 / var2)
        elif var3 == 5:
            print("Quotient after division is", var1, "and", var2, "is:", var1 // var2)
        elif var3 == 6:
            print("Remainder after division is", var1, "and", var2, "is:", var1 % var2)
        elif var3 == 7:
            print("To find num1 to the power of num2", var1, "and", var2, "is:", var1 ** var2)
        elif var3 == 8:
            print("Thank you for using the application")
            break
    else:
        print("Number Incorrect")

        

# Qn
# W A P to check whether a year entered by user is an leap year or not ?
# Check with below input:-
# leap year:- 2012 , 1968 , 2004 , 1200 , 1600 , 2400
# Non-lear year:- 1971 , 2006 , 1700 , 1800 , 1900

# Solution
year = int(input('Enter an year: '))
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print('Year is a leap Year')
else:
    print('Year is not a leap year')

    

# Qn
# W A P which takes one number from the user and checks whether it is
# an even or odd number?, If it even then prints number is
# even number else prints that number is odd number.

# Solution
num = int(input('Enter a number: '))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


    
    
# Qn
# W A P which takes two numbers from the user and prints below output:-
# 1 . num1 is greater than num2 if num1 is greater than num2
# 2 . num1 is smaller than num2 if num1 is smaller than num2
# 3 . num1 is equal to num2 if num1 and num2 are equal

# Solution
# Method 1 - if else
num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
print("num1 is:",num1,"\tnum2 is:",num2)
if num1 > num2:
    print("num1 is greater than num2")
elif num1 < num2:
    print("num1 is smaller than num2")
elif num1 == num2:
    print("num1 is equal to num2")
    
#Method 2 - Ternary operator
num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
print("num1 is:",num1,"\tnum2 is:",num2)
print("num1 is greater than num2") if num1 > num2 else print("num1 is smaller than num2") if(num1 < num2) else print("num1 is equal to num2")




# Qn
# W A P which takes three numbers from the user and prints below
# output:-
# 1 . num1 is greater than num2 and num3 if num1 is greater than num2
# and num3
# 2 . num2 is greater than num1 and num3 if num2 is greater than num1
# and num3
# 3 . num3 is greater than num1 and num2 if num3 is greater than num1
# and num2
# Note:- 1 . Do this problem using if - elif - else
# 2 . Do this using ternary operator
# a = a if a>b else b

# Solution
# Method 1 - if else
num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
num3 = eval(input('Enter third number: '))
print("num1 is:",num1,"\tnum2 is:",num2,"\tnum3 is:",num3)
if (num1 > num2) & (num1>num3):
    print("num1 is greater than num2 and num3")
elif (num2 > num1) & (num2>num3):
    print("num2 is greater than num1 and num3")
elif (num3 > num2) & (num3>num1):
    print("num3 is greater than num1 and num2")
    
# Method 2 Ternary Operator    
num1 = eval(input('Enter first number: '))
num2 = eval(input('Enter second number: '))
num3 = eval(input('Enter third number: '))
print("num1 is:",num1,"\tnum2 is:",num2,"\tnum3 is:",num3)

print("num1 is greater than num2 and num3") if ((num1 > num2) & (num1>num3)) else print("num2 is greater than num1 and num3") if ((num2 > num1) & (num2>num3)) else print("num3 is greater than num1 and num2")



# Qn
# Write a Python program to find the length of the my_str using loop:-
# Input:- 'Write a Python program to find the length of the my_str'
# Output:- 55

# Solution
ip_str='Write a Python program to find the length of the my_str'
print("Input String is:",ip_str)
length_of_string = 0
for i in ip_str:
    length_of_string += 1

print("Length of the string is:", length_of_string)



# Qn
# Write a Python program to find the total number of times letter 'p'
# is appeared in the below string using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.\n'
# Output:- 9

# Solution
my_str = "peter piper picked a peck of pickled peppers.\n"
j, count_char = 0, 0

for i in my_str:
    if my_str[j] == 'p':
        count_char += 1
    j += 1

print("Count of 'p' in string is :", count_char)




# Qn
# Write a Python Program, to print all the indexes of all occurences of
# letter 'p' appeared in the string using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:-
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40

# Solution
my_str = "peter piper picked a peck of pickled peppers."
j = 0
print("Letter 'p' appeared in following indices:")

for i in my_str:
    if my_str[j] == 'p':
        print(j)
    j += 1

    
    
# Qn
# Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- [ 'peter' , 'piper' , 'picked' , 'a' , 'peck' , 'of' , 'pickled' ,
# 'peppers' ]

# Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is:",my_str)
word = ""
lst = [10, 20]
lst.clear()
for w in my_str:
    if w != ' ':
        word += w
    else:
        lst.append(word)
        word = ""

print("Output is:",lst)




# Qn
# Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'peppers pickled of peck a picked piper peter'

# Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is :",my_str)
lst = my_str.split()[::-1]
new_str = ''
for ele in lst:
    new_str +=ele
    new_str +=' '

print("Output is:", new_str)




# Qn
# Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- '.sreppep delkcip fo kcep a dekcip repip retep'

# Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is:",my_str)

rev_index=-1
new_str,word = '',''

for w in my_str[::-1]:
    if w != ' ':
        word += w
    else:
        new_str += word
        new_str += " "
        word = ""

print("Output is:", new_str)



# Qn
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'

# Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is :", my_str)
lst = my_str.split()
new_str = ""

for ele in lst:
    new_str += ''.join(ele[::-1])
    new_str +=" "

print("Output is:", new_str)



# Qn
# Write a python program to find below output using loop:-
# Input:- 'peter piper picked a peck of pickled peppers.'
# Output:- 'Peter Piper Picked A Peck Of Pickled Peppers'

# Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is :",my_str)
lst = my_str.split()
new_str = ''
for ele in lst:
    new_str +=ele.capitalize()
    new_str +=' '

print("Output is:", new_str)



# Qn
# Write a python program to find below output using loop:-
# Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
# Output:- 'Peter piper picked a peck of pickled peppers'

# Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print("Input is :", my_str)
lst = my_str.split()
new_str = ''
for ele in lst:
    if ele == lst[0]:
        new_str += ele.capitalize()
        new_str += ' '
    else:
        new_str += ele.lower()
        new_str += ' '
print("Output is:", new_str)



# Qn
# Write a python program to implement index method using loop. If
# sub_str is found in my_str then it will print the index
# of first occurrence of first character of matching string in my_str:-
# Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.' ,
# sub_str = 'Pickl'
# Output:- 29

# Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print("Input is :", my_str)
sub_str = 'Pickl'

lst = my_str.split()
str_index = 0
new_str = ''
if(my_str.find(sub_str)!=-1):
    for ele in lst:
        if ele.find(sub_str) != -1:
            # print(str_index)
            # print(ele)
            str_index += ele.find(sub_str)
            # print(str_index)
            break
        else:
            # print(ele,len(ele))
            str_index += len(ele)+1
            # print(str_index)
    print("Index of '", sub_str, "' in", my_str, "is", str_index)
else:
    print("Substring not found")


    
# Qn
# Write a python program to implement replace method using loop. If
# sub_str is found in my_str then it will replace the first
# occurrence of sub_str with new_str else it will will print sub_str not
# found:-
# Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.' ,
# sub_str = 'Peck' , new_str = 'Pack'
# Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'

# Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print("Input is :", my_str)
sub_str = 'Peck'
new_sub_str = 'Pack'

lst = my_str.split()
str_index = 0
new_str = ''
if my_str.find(sub_str) != -1:
    for ele in lst:
        if ele.find(sub_str) != -1:
            i, j = 0, 0
            word = ''
            while i < len(ele):
                if ele[i] == sub_str[j]:
                    k = i
                    for j in range(len(sub_str)):
                        if ele[k] == sub_str[j]:
                            word += new_sub_str[j]
                            k += 1
                    i = k - 1
                else:
                    word += ele[i]

                i += 1

            lst[str_index] = word
            str_index += 1

        else:
            str_index += 1

    new_str = ' '.join(lst)
    print("Output is:", new_str)
else:
    print("Substring not found")

    

# Qn
# Write a python program to find below output (implements rjust and
# ljust) using loop:-
# Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.' , sub_str =
# 'Peck' ,
# Output:- '*********************Peck********************'

# Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
print("Input is :", my_str)
sub_str = 'Peck'
sub_str_index = 0
new_str = ''

if my_str.find(sub_str) != -1:
    sub_str_index = my_str.index(sub_str)
    i = 0
    # ljust using loop
    for i in range(0, sub_str_index):
        new_str += '*'

    new_str += sub_str

    # rjust using loop
    for i in range(len(new_str), len(my_str)):
        new_str += '*'

    print("Output is:", new_str)
else:
    print("Substring not found")

    

# Qn
# Write a python program to find below output using loop:-
# Input:- 'This is Python class' , sep = ' is' ,
# Output:- [ 'This' , 'is' , 'Python class' ]

# Solution
my_str = 'This is Python class'
print("Input is :", my_str)
sep = 'is'
lst = my_str.split()
op_lst = []
temp_lst = []
word = ''
if sep in lst:
    for ele in lst[:lst.index(sep)]:
        temp_lst.append(ele)

    if lst.index(sep) != 0:
        word = ' '.join(temp_lst)
        op_lst.append(word)
    op_lst.append(sep)

    temp_lst.clear()
    word = ''
    for ele in lst[lst.index(sep) + 1:len(lst)]:
        temp_lst.append(ele)

    if lst.index(sep) != len(lst) - 1:
        word = ' '.join(temp_lst)
        op_lst.append(word)

    print(op_lst)
else:
    print("Separator not found")







