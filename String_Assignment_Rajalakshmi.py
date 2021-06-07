
                        # String Assignment by Rajalakshmi B
#Qn    
#Declare a string and store it in a variable. 
#Check the type and print the id of the same.
#Solution
a = 'String Assignment By Rajalakshmi'
print("The value of string variable is :", a, "; \nIt's type is :", type(a), "; \nIt's ID is :", id(a))


#Qn  
#Which are valid/invalid strings
# 1. 'This is Python class' valid/invalid
# 2. "This is Python class" valid/invalid
# 3. '''This is Python class''' valid/invalid
# 4. """This is Python class"""valid/invalid

test_str1 = '\nThis is Python class'
print(test_str1, "-> is a valid string.") if type(test_str1) == str else print(test_str1,"-> is not a valid string.")

test_str2 = "\nThis is Python class"
print(test_str2, "-> is a valid string.") if type(test_str2) == str else print(test_str2, "-> is not a valid string.")

test_str3 = '''\nThis is Python class'''
print(test_str3, "-> is a valid string.") if type(test_str3) == str else print(test_str3, "-> is not a valid string.")

test_str4 = """\nThis is Python class"""
print(test_str4, "-> is a valid string.") if type(test_str4) == str else print(test_str4, "-> is not a valid string.")


# 5. 'This is Python's class' valid/invalid
# This string is not valid string as the main string is inside Single Quotation and the apostrophe in Python's 
# is taken as closing quotation. If the main string is inside "" then there won't be an error.

#6. "Learnbay provides "Java", "Python" classes" valid/invalid
# This string is not valid string as the main string is inside Double Quotation and the double quotation in Java & Python 
# is confused for the closing quotation. If the main string is inside '''''' then there won't be an error.

# 7. "Learnbay provides 'Java', 'Python' classes" valid/invalid
# 8. "This is Python's class" valid/invalid
# 9. """Learnbay provides "Java", "Python" classes""" valid/invalid
# 10. '''Learnbay provides "Java", "Python" classes''' valid/invalid   
# 11. '''Learnbay provides
# "Java", "Python" 
# classes'''
# valid/invalid

test_str7 = "\nLearnbay provides 'Java', 'Python' classes"
print(test_str7, "-> is a valid string.") if type(test_str7) == str else print(test_str7, "-> is not a valid string.")

test_str8 = "\nThis is Python's class"
print(test_str8, "-> is a valid string.") if type(test_str8) == str else print(test_str8, "-> is not a valid string.")

test_str9 = """\nLearnbay provides "Java", "Python" classes"""
print(test_str9, "-> is a valid string.") if type(test_str9) == str else print(test_str9, "-> is not a valid string.")

test_str10 = '''\nLearnbay provides "Java", "Python" classes'''
print(test_str10, "-> is a valid string.") if type(test_str10) == str else print(test_str10,
                                                                                 "-> is not a valid string.")
test_str11 = '''\nLearnbay provides
"Java", "Python" 
classes'''
print(test_str11, "-> is a valid string.") if type(test_str11) == str else print(test_str11,
                                                                                 "-> is not a valid string.")

# 12. 'This is
# Python 
# class'
# valid/invalid
# This string is not valid string as the main string is in the form of paragraph. 
#If the main string is inside '''''' then there won't be an error.


#Qn  
#Write the code to get the output mentioned below print statement
my_str = "Although that way may not be obvious at first unless you're Dutch."
my_str1 = "Although that way may not be obvious at first unless you're Dutch."

print("The length of my_str is", len(my_str)) 
#output:- The length of my_str is 66

print("Are IDs of my_str and my_str1 same? :", id(my_str) != id(my_str1))
#output:- id of my_str and my_str1 is same? - True

print("Type of my_str is:", type(my_str))
#output:- Type of my_str is: str


#Qn  
#Indexing
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
#Write the code to get the output,instructions are mentioned below print statement. use indexing

print("my_str is :",my_str)
print("The first character in my_str is:",my_str[0])
#output:- The first character in my_str is: A
#Note:- Use positive indexing

print("The first character in my_str is:",my_str[len(my_str)-1])
#output:- The first character in my_str is: h
#Note:- Use len() function.

print("The character at index 65 in my_str is:", my_str[65])
#output:- The character at index 10 in my_str is: c
#Note:- Use positive indexing

print("The last character in my_str is:",my_str[-1])
#output:- The last character in my_str is: h
#Note:- Use negative indexing.

print("The last character in my_str is:",my_str[len(my_str)-1])
#output:- The last character in my_str is: h
#Note:- Use len() function.

print("The character in my_str is:",my_str[my_str.index('8')])
#output:- The character in my_str is: 8
#Note:- Use positive index


#Qn  
# Slicing
my_str = "Although that way may not be obvious at first unless you're Dutch."
# Write the code to get the output,instructions are mentioned below print statement. use slicing
print("You have sliced:", my_str[::])
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.
# Without begin, end and step

print("You have sliced:", my_str[0:len(my_str):])
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.
# with begin as 0 end using len and without step

print("You have sliced:", my_str[::1])
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.
# without begin and end but using step

print("You have sliced:", my_str[0:len(my_str):1])
# output:- You have sliced: Although that way may not be obvious at first unless you're Dutch.
# With begin, end and step

print("You have sliced:", my_str[0:10:-1])
# output:- You have sliced:   .with using begin and end using postive values and step as negative values.
# Slicing command should print empty string.


print("You have sliced:", my_str[::2])
# output:- You have sliced: Atog htwymyntb biu tfrtuls o'eDth

print("You have sliced:", my_str[::3])
# output:- You have sliced: Ahgttam tebo  r lsorDc

print("You have sliced:", my_str[::-1])
# output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use only step

print("You have sliced:", my_str[len(my_str):None:-1])
# output:- You have sliced: .hctuD er'uoy sselnu tsrif ta suoivbo eb ton yam yaw taht hguohtlA. Use begin end and step.


print("You have sliced:", my_str[::-2])
# output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use only step

print("You have sliced:", my_str[len(my_str):None:-2])
# output:- You have sliced: .cu ruysen si asovoe o a a athuhl. use begin, end and step.


print(my_str[10:17:-1])
# What will be the output?
#Output will be empty as step is moving from RHS to LHS while start and stop index are 10,17
# which is moving from LHS to RHS. So there is a conflict.

print("You have sliced:", my_str[16:10:-1])
# output:- You have sliced: yaw ta, Using begin, end and step.

print("You have sliced:", my_str[my_str.index('ess'):56:1])
# output:- You have sliced: ess you. Using begin, end and step.


#Qn  
#Basic operation on string
str1 = 'Learnbay'
str2 = 'Python'

#Write the code to get the output,instructions are mentioned below.
#Output is: Learnbay Python
print("Concatenated string is:", str1 + str2)

# If a string is concatenated with integer  
# for eg: str3 = str1 + 10 , we get the below mentioned error
#Error: TypeError: can only concatenate str (not "int") to str

# If a string is concatenated with float number  
# for eg: str3 = str1 + 10.20 , we get the below mentioned error
#Error: TypeError: can only concatenate str (not "float") to str


#Find below Output
#Output is: LearnbayLearnbayLearnbay
print("String Repetition :", str1 * 3)

# If a string is multiplied with float to get a sequence 
# for eg: print(str1 * 3.5) , we get the below mentioned error
#Error: TypeError: can't multiply sequence by non-int of type 'float'

# If a string is multiplied with string to get a sequence 
# for eg: print(str1 * str2) , we get the below mentioned error
#Error: TypeError: can't multiply sequence by non-int of type 'str'


#Qn  
#Find below Output
str1 = 'Python'
str2 = 'Python'
str3 = 'Python$'
str4 = 'Python$'

print("str1 is", str1, "\t\tstr2 is", str2, "\nstr3 is", str3, "\tstr4 is", str4)

#print True by using identity operator between str1 and str2
print("\nAre str1 and str2 same? :", str1 is str2)

#print False by using identity operator between str1 and str3
print("Are str1 and str3 same? :", str1 is str3)

#print False by using identity operator between str4 and str3
print("Are str4 and str3 same? :", str4 is str3)

#Check if P is available in str1 and print True by using membership operator
#Solution
check_alphabet = 'P'
if str1.find(check_alphabet) != -1:
    print("\nIs", check_alphabet, "available in", str1, "?:", check_alphabet in str1)
else:
    print("Is", check_alphabet, "available in", str1, "?:", check_alphabet in str1)

    
#Check if $ is available in str3 and print True by using membership operator
#Solution
check_alphabet = '$'
if str3.find(check_alphabet) != -1:
    print("Is", check_alphabet, "available in", str3, "?:", check_alphabet in str3)
else:
    print("Is", check_alphabet, "available in", str3, "?:", check_alphabet in str3)

    
#Check if N is available in str3 and print False by using membership operator
#Solution
check_alphabet = 'N'
if str3.find(check_alphabet) != -1:
    print("Is", check_alphabet, "available in", str3, "?:", check_alphabet in str3)
else:
    print("Is", check_alphabet, "available in", str3, "?:", check_alphabet in str3)


#Qn  
str1 = 'This is Python class'

#write the code to replace 'Python' with 'Java' and you should get below error.
#Solution
print("Original String is:", str1)
print("New String is:", str1.replace('Python', 'Java'))


# String is an immutable object, the original string can't be changed 
# while replacing a part of it.
# Any attempt to replace the original string for eg:
# str1[str1.find('Python'):str1.find('class')] = 'Java'
# will raise TypeError: 'str' object does not support item assignment. 


#Qn  
str1 = 'A'
str2 = 'A'
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print False using comparison operator
#Solution
print(" Is", str1, "greater than", str2, "? : \t", bool(str1 > str2))
print(" Is", str1, "lesser than", str2, "? : \t", bool(str1 < str2))
print(" Is", str1, "greater than or equal to", str2, "? :", bool(str1 >= str2))
print(" Is", str1, "lesser than or equal to", str2, "? : ", bool(str1 <= str2))

#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Solution
print(" Is", str1, "equal to", str2, "? :\t", bool(str1 == str2))
print(" Is", str1, "not equal to", str2, "? :", bool(str2 != str1))


#Qn  
str1 = 'A'
str2 = 'a'
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print False using comparison operator
#Solution
print(" Is", str1, "greater than", str2, "? : \t", bool(str1 > str2))
print(" Is", str1, "lesser than", str2, "? : \t", bool(str1 < str2))
print(" Is", str1, "greater than or equal to", str2, "? :", bool(str1 >= str2))
print(" Is", str1, "lesser than or equal to", str2, "? : ", bool(str1 <= str2))

#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Solution
print(" Is", str1, "equal to", str2, "? :\t", bool(str1 == str2))
print(" Is", str1, "not equal to", str2, "? :", bool(str2 != str1))


#Qn  
str1 = 'A'
str2 = '65'

print(" Is", str1, "greater than", str2, "? : \t", bool(str1 > str2))
print(" Is", str1, "lesser than", str2, "? : \t", bool(str1 < str2))
print(" Is", str1, "greater than or equal to", str2, "? :", bool(str1 >= str2))
print(" Is", str1, "lesser than or equal to", str2, "? : ", bool(str1 <= str2))

#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Solution
print(" Is", str1, "equal to", str2, "? :\t", bool(str1 == str2))
print(" Is", str1, "not equal to", str2, "? :", bool(str2 != str1))


str1 = 'A'
str2 =  65

#Since 65 is declared within quotes in the previous variable, it becomes a string str2='65'. So comparison works.
#If str2=65 then comparison operator will not work and it will give the below error
#Error: TypeError: '>=' not supported between instances of 'str' and 'int'

#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Solution
print("\n Is", str1, "equal to", str2, "? :\t", bool(str1 == chr(str2)))
print(" Is", str1, "not equal to", str2, "? :", bool(chr(str2) != str1))


#Qn  
str1 = 'Python'
str2 = 'Python'
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print False using comparison operator
#Solution
print(" Is", str1, "greater than", str2, "? : \t", bool(str1 > str2))
print(" Is", str1, "lesser than", str2, "? : \t", bool(str1 < str2))
print(" Is", str1, "greater than or equal to", str2, "? :", bool(str1 >= str2))
print(" Is", str1, "lesser than or equal to", str2, "? : ", bool(str1 <= str2))

#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Solution
print(" Is", str1, "equal to", str2, "? :\t", bool(str1 == str2))
print(" Is", str1, "not equal to", str2, "? :", bool(str2 != str1))


#Qn  
str1 = 'Python'
str2 = 'python'
#Compare str1 and str2 and print True using comparison operator
#Compare str1 and str2 and print False using comparison operator
#Solution
print(" Is", str1, "greater than", str2, "? : \t", bool(str1 > str2))
print(" Is", str1, "lesser than", str2, "? : \t", bool(str1 < str2))
print(" Is", str1, "greater than or equal to", str2, "? :", bool(str1 >= str2))
print(" Is", str1, "lesser than or equal to", str2, "? : ", bool(str1 <= str2))

#Compare str1 and str2 and print True using equality operator
#Compare str1 and str2 and print False using equality operator
#Solution
print(" Is", str1, "equal to", str2, "? :\t", bool(str1 == str2))
print(" Is", str1, "not equal to", str2, "? :", bool(str2 != str1))




#Qn  
a = 'Python'
b = ''
#Apply logical opereators (and, or & not) on above string values 
#and observe the output.
print("\t---And operator---")
print("\t", a, " and", a, " |", a and a)
print("\t", a, " and", b, " |", a and b)
print("\t", b, " and", a, " |", b and a)
print("\t", b, " and", b, " |", b and b)

print("\n\t---Or operator---")
print("\t", a, " or", a, "  |", a or a)
print("\t", a, " or", b, "  |", a or b)
print("\t", b, " or", a, "  |", b or a)
print("\t", b, " or", b, "  |", b or b)

print("\n\t---Not operator---")
print("\tNot ", a, " |", not a)
print("\tNot ", b, " |", not b)

#Qn  
a = ''
b = ''
#Apply logical opereators (and, or & not) on above string values and 
#observe the output.

#Solution
print("\t---And operator---")
print("\t", a, " and", a, " |", a and a)
print("\t", a, " and", b, " |", a and b)
print("\t", b, " and", a, " |", b and a)
print("\t", b, " and", b, " |", b and b)

print("\n\t---Or operator---")
print("\t", a, " or", a, "  |", a or a)
print("\t", a, " or", b, "  |", a or b)
print("\t", b, " or", a, "  |", b or a)
print("\t", b, " or", b, "  |", b or b)

print("\n\t---Not operator---")
print("\tNot ", a, " |", not a)
print("\tNot ", b, " |", not b)


#Qn  
a = 'Python'
b = 'learnbay'
#Apply logical opereators (and, or & not) on above string values 
#and observe the output.

#Solution
print("\t---And operator---")
print("\t", a, " and", a, " |", a and a)
print("\t", a, " and", b, " |", a and b)
print("\t", b, " and", a, " |", b and a)
print("\t", b, " and", b, " |", b and b)

print("\n\t---Or operator---")
print("\t", a, " or", a, "  |", a or a)
print("\t", a, " or", b, "  |", a or b)
print("\t", b, " or", a, "  |", b or a)
print("\t", b, " or", b, "  |", b or b)

print("\n\t---Not operator---")
print("\tNot ", a, " |", not a)
print("\tNot ", b, " |", not b)


#Qn  
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"
# Write the code to get the total count of 't' in above string. 
#Use find() and index() method.

#Solution
lst = my_str.split()
i, count = 0, 0
for i in range(len(lst)):
    if lst[i].find('t') != -1:
        count += 1
        if lst[i].rindex('t') != lst[i].index('t'):
            count += 1
print("Count of 't' in ", my_str, "is:", count)

# Write the code to get the index of '8' in my_str. 
#Use find() and index() method.
#Solution
print("Substring '8' is found in the index ",my_str.find('8')," in the string")
print("The index of '8' in the string is",my_str.index('8'))

# What will be the output of below code?
print(my_str.find('the')) 
#Since the substring 'the' is not found in the string, find() function returns -1

# print(my_str.index('the'))
#Since the substring 'the' is not found in the string, index() function 
#raises ValueError

print(my_str.find('t', 9, 15))
#Since find() returns the first occurence of the given substring between 
#position 9 to 15, the value that is returned is 11.
#Because first occurence of 't' between position 9 and 15 is 11 

print(my_str.rfind('u'))
#rfind() method find the first occurence of 'u' from RHS in the string. 
#So the result is 63.

print(my_str.rindex('u'))
#rindex() method find the first occurence of 'u' from RHS in the string. 
#So the result is 63.


##Qn  
#W A P which applies strip() method if any string, which will be taken from 
#user, starts and ends with space, or applies 
#rrstrip() method if that string only ends with space or applies lstrip() 
#method if that string only starts with a space.

#For example:-
#input:- '    Python   '
#output:- 'Python'

#input:- '    Python'
#output:- 'Python'

#input:- 'Python   '
#output:- 'Python'

#Solution
my_str=input("Enter a string")
if my_str.startswith(' ') and my_str.endswith(' '):
    print(my_str.strip())
    print("Both Spaces striped off")
elif my_str.startswith(' '):
    print(my_str.lstrip())
    print("Left Spaces striped off")
elif my_str.endswith(' '):
    print(my_str.rstrip())
    print("Right Spaces striped off")
else:
    print(my_str)
    print("No spaces to strip off")


#Qn  
my_str = "Although 8 that way may not be obvious at first unless you're Dutch"

#Write the code to convert all alphabets in my_str into upper case.
#Solution
print(my_str.upper())

#Write the code to convert all alphabets in my_str into lower case.
#Solution
print(my_str.lower())

#Write the code to swap the cases of all alphabets in my_str.
#Solution
#(lower to upper and upper to lower)
print(my_str.swapcase())


#Qn  
#Write the code which takes one string from user and if it starts with 
#small case letter then convert it to corresponding 
#capital letter otherwise if starts with capital letters then convert 
#first character of every word in that string into capital.

#Solution
my_str=input("Enter a string")
while True:
    if my_str[0].islower():
        print(my_str.capitalize())
        break
    elif my_str[0].isupper():
        print(my_str.title())
        break
    else:
        print("Enter a string which starts with alphabet")
        my_str = input("Enter a string")


#Qn  
#Take a string from user and check if it is:-
#     1. alphanumeric
#     2. alphabets
#     3. digit
#     4. all letters are in lower case
#     5. all letters are in upper case
#     6. in title case
#     7. a space character
#     8. numeric
#     9. all number elements in string are decimal

#Solution
my_str=input("Enter a string")

print("Are all the values in string - alphanumeric? :",my_str.isalnum())
print("Are all the values in string - alphabet? :",my_str.isalpha())
print("Are all the values in string - digits? :",my_str.isdigit())
print("Are all letters in lower case? :",my_str.islower())
print("Are all letters in upper case? :",my_str.isupper())
print("Is string in title case? :",my_str.istitle())
print("Is string a space character? :",my_str.isspace())
print("Are all the values in string - numeric? :",my_str.isnumeric())
print("Are all number elements in string decimal? :",my_str.isdecimal())


#Qn  
#W A P which takes a string as an input and prints True if the string is 
#valid identifier else returns False.
#Sample Input:- 'abc', 'abc1', 'ab1c', '1abc', 'abc$', '_abc', 'if'

#Solution
my_str=input("Enter a string")
print("Is",my_str,"a valid identifier? :",my_str.isidentifier())


#Qn  
#What will be output of below code?
s = chr(65) + chr(97)
print(s.isprintable())
# Output is true as both the characters A and a are printable

s = chr(27) + chr(97)
print(s.isprintable())
# Output is false as chr(27) - Escape character is not printable

s = '\n'
print(s.isprintable())
# Output is false as \n is not printable but executable

s = ''
print(s.isprintable())
# Output is true as space is printable


#Qn  
#What will be output of below code?
my_string = '  '
print(my_string.isascii()) 
# Output is True 

my_string = 'Studytonight'
print(my_string.isascii())
# Output is True

my_string = 'Study tonight'
print(my_string.isascii())
# Output is True

my_string = 'Studytonight@123'
print(my_string.isascii())
# Output is True

my_string = '°'
print(my_string.isascii())
# Output is False as it is an Non ascii char

my_string = 'ö'
print(my_string.isascii())
# Output is False as it is an Non ascii char


#Qn  
#What will be the output of below code?
firstString = "der Fluß"
secondString = "der Fluss"

if firstString.casefold() == secondString.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')

#Solution
# Output is 'The strings are equal.' Casefold aggresively changes all the 
#characters into lower so both the output is equal.


#Qn  
#Write the code to get below output
#O/P 1:- python** (using ljust method)
#Solution
my_str = input("Enter a string")
print(my_str.ljust(len(my_str) + 2, '*'))

#Write the code to get below output
#O/P 1:- **python (using rjust method)
#Solution
print(my_str.rjust(len(my_str) + 2, '*'))

#Write the code to get below output
#O/P 1:- **python** (using rjust method)
#Solution
temp = my_str.ljust(len(my_str) + 2, '*')
print(temp.rjust(len(temp) + 2, '*'))



#Qn  
#Write a Python program to find the length of the my_str:-
#Input:- 'Write a Python program to find the length of the my_str'
#Output:- 55

#Solution
#Method 1
ip_str='Write a Python program to find the length of the my_str'
print("Length of the string is:",len(ip_str))

#Method 2
count = 0
for i in ip_str:
    count += 1
    
print("Length of the string is:",count)


#Qn  
#Write a Python program to find the total number of times letter 
#'p' is appeared in the below string:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 9

#Solution
my_str = "peter piper picked a peck of pickled peppers."
j, count_char = 0, 0

for i in my_str:
    if my_str[j] == 'p':
        count_char += 1
    j += 1

print("Count of 'p' in", my_str, "is :", count_char)


#Qn  
#Write a Python Program, to print all the indexes of all occurences of 
#letter 'p' appeared in the string:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 
# 0
# 6
# 8
# 12
# 21
# 29
# 37
# 39
# 40

#Solution
my_str = "peter piper picked a peck of pickled peppers."
j = 0
print("Letter 'p' appeared in following indices:")

for i in my_str:
    if my_str[j] == 'p':
        print(j)
    j += 1


#Qn  
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers.']

#Solution
my_str="peter piper picked a peck of pickled peppers."
print("Input is :",my_str)
print("Output is:",my_str.split())


#Qn  
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'peppers. pickled of peck a picked piper peter'

#Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is :",my_str)
lst = my_str.split()[::-1]
print(' '.join(lst))


#Qn  
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- '.sreppep delkcip fo kcep a dekcip repip retep'

#Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is :",my_str)
lst = my_str.split()
print(' '.join(lst)[::-1])


#Qn  
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'retep repip dekcip a kcep fo delkcip .sreppep'

#Solution
my_str = 'peter piper picked a peck of pickled peppers.'
print("Input is :", my_str)
lst = my_str.split()
new_str = ""

for ele in lst:
    new_str += ''.join(ele[::-1])
    new_str +=" "

print("Output is:", new_str)


#Qn  
#Write a python program to find below output:-
#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- 'Peter Piper Picked A Peck Of Pickled Peppers.'

#Solution
my_str="peter piper picked a peck of pickled peppers."
print("Input is :",my_str)
print("Output is:",my_str.title())


#Qn  
#Write a python program to find below output:-
#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.'
#Output:- 'Peter piper picked a peck of pickled peppers.'

#Solution
my_str="Peter Piper Picked A Peck Of Pickled Peppers."
print("Input is :",my_str)
print("Output is:",my_str.capitalize())


#Qn  
#Write a python program to implement index method. If sub_str is found in 
#my_str then it will print the index of first occurrence of first character 
#of matching string in my_str:-
#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', 
#sub_str = 'Pickl'
#Output:- 29

#Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
print("Main string is :",my_str)
print("The index of substring '",sub_str,"' in main string is", my_str.index(sub_str))


#Qn  
#Write a python program to implement replace method. If sub_str is found in
#my_str then it will replace the first occurrence of sub_str with new_str 
#else it will will print sub_str not found:-
#Input:- my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.', 
#sub_str = 'Peck', new_str = 'Pack'
#Output:- 'Peter Piper Picked A Pack Of Pickled Peppers.'

#Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'

print("Input is :\t\t",my_str)
print("Output after replacement is:",my_str.replace(sub_str,new_str))


#Qn  
#Write a python program to find below output (implements rjust and ljust):-
#Input:- 'Peter Piper Picked A Peck Of Pickled Peppers.', sub_str = 'Peck', 
#Output:- '*********************Peck********************'

#Solution
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'

print("Input  is",my_str)
temp = sub_str.rjust(my_str.index(sub_str)+len(sub_str), '*')
print("Output is",temp.ljust(len(my_str), '*'))







