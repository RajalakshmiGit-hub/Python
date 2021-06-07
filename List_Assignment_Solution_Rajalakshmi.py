                        # Python - List Assignment

# Qn
#Write a Python program to find the sum of all elements in a list using loop.
#Input:- [10,20,30,40]
#Output:- 100

# Solution
ip_lst = eval(input("Enter the list of numbers"))
result = 0
x: int
for x in ip_lst:
    result += x

print("Sum of all items in the list :", result)


# Qn
#Write a Python program to find the multiplication of all elements 
#in a list using loop.
#Input:- [10,20,30,40]
#Output:- 240000

# Solution
ip_lst = eval(input("Enter the list of numbers"))
result = 1
x: int
for x in ip_lst:
    result = result * x

print("Multiplying all items in the list :", result)



# Qn
#Write a Python program to find the largest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 2321

# Solution
ip_lst = eval(input("Enter the list of numbers"))

result = ip_lst[0]
for x in ip_lst:
    if result < x:
        result = x

print("Largest number in the list :", result)



# Qn
#Write a Python program to find the smallest number from a list using loop.
#Input:- [10,100,2321, 1,200,2]
#Output:- 1

# Solution
ip_lst = eval(input("Enter the list of numbers"))

result = ip_lst[0]
for x in ip_lst:
    if result > x:
        result = x
        
print("Smallest number in the list :", result)



# Qn
#Write a Python program to count the number of strings having length more 
#than 2 and are palindrome in a list using loop.
#Input:- ['ab', 'abc', 'aba', 'xyz', '1991']
#Output:- 2

# Solution
ip_lst = eval(input("Enter a list"))

result = 0

for x in ip_lst:
    if (len(x) >2) & (x == x[::-1]):
        result +=1

print("Number of strings having length more than 2 and are palindrome in a list are:", result)



# Qn
#Write a Python program to sort a list in ascending order using loop.
#Input:- [100,10,1,298,65,483,49876,2,80,9,9213]
#Output:- [1,2,9,10,65,80,100,298,483,9213,49876]

# Solution
ip_lst = eval(input("Enter the list of numbers"))

for i in range (len(ip_lst)):
    for j in range(i + 1, len(ip_lst)):
        if(ip_lst[i] > ip_lst[j]):
            temp = ip_lst[i]
            ip_lst[i] = ip_lst[j]
            ip_lst[j] = temp

print("Sorted List ( Ascending Order ) is : ", ip_lst)



# Qn
#Write a Python program to get a sorted list in increasing order of last 
#element in each tuple in a given list using loop.
#Input:- [(5,4),(9,1),(2,3),(5,9),(7,6),(5,5)]
#output:- [(9,1),(2,3),(5,4),(5,5),(7,6),(5,9)]

# Solution
ip_tuple = eval(input("Enter the list of tuple of numbers e.g [(5,4),(9,1)]"))

for i in range (len(ip_tuple)):
    for j in range(i + 1, len(ip_tuple)):
        if ip_tuple[i][1] > ip_tuple[j][1]:
            temp = ip_tuple[i]
            ip_tuple[i] = ip_tuple[j]
            ip_tuple[j] = temp

print("After sorting using second element ( Ascending Order ) is: ", ip_tuple)



# Qn
#Write a Python program to remove duplicate element from a list using loop.
#Input:- [10,1,11,1,29,876,768,10,11,1,92,29,876]
#Output:- [10,1,11,29,876,768,92]

# Solution
ip_lst = eval(input("Enter the list of numbers"))

op_lst=[]

for i in ip_lst:
    if i not in op_lst:
        op_lst.append(i)

print("List after removing duplicates is",op_lst)



# Qn
#Write a Python program to check a list is empty or not?
#Input:- []
#Output:- List is empty
#Input:- [10,20,30]
#Output:- List is not empty

# Solution
ip_lst = eval(input("Enter a list"))

print("List :",ip_lst," is empty") if ((not ip_lst) == True) else print("List :",ip_lst," is not empty")



# Qn
#Write a Python program to copy a list using loop.
#inp_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]
#out_lst = [10,10.20,10+20j, 'Python', [10,20], (10,20)]

# Solution
ip_lst = eval(input("Enter a list to copy"))

op_lst=[]

for i in ip_lst:
    op_lst.append(i)

print("Output List:",op_lst)



# Qn
#Write a Python program to find the list of words that are longer than 
#or equal to 4 from a given string.
#Input:'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
#Output:- ['much', 'wood', 'would', 'woodchuck', 'chuck', 'could']
#Note:- Duplicate should be avoided.

# Solution
ip_str='How much wood would a woodchuck chuck if a woodchuck could chuck wood'
print("Input is : ",ip_str)
ip_lst = ip_str.split()
op_lst =[]

for i in ip_lst:
    if ( i not in op_lst)&(len(i)>=4):
        op_lst.append(i)

print("The list of words that are longer than or equal to 4 from a given string are: \n",op_lst)



# Qn
#Write a Python program which takes two list as input and returns True 
#if they have at least 3 common elements.
#inp_lst1 = [10,20,'Python', 10.20, 10+20j, [10,20,30], (10,20,30)]
#inp_lst2 = [(10,20,30),1,20+3j,100.2, 10+20j, [10,20,30],'Python']
#Output:- True

# Solution
ip_lst1 = eval(input("Enter the first list"))
ip_lst2 = eval(input("Enter the second list"))
count = 0
print("List 1 is:",ip_lst1)
print("List 2 is:",ip_lst2)

for i in ip_lst1:
    for j in ip_lst2:
        if i == j:
            count += 1

print("Are there 3 or more common element between the two lists? :", count>3)



# Qn
#Write a Python program to create a 4X4 2D matrix with below elements using
#loop and list comprehension both.
#Output:- [[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]

# Solution
op_lst = [[i*j for j in range(0,4)] for i in range(0,4)]
print(op_lst)



# Qn
#Write a Python program to create a 3X4X6 3D matrix with
#below elements using loop
#Output:- 
# [
#     [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
#     [[0,0,0,0,0,0],[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3]],
#     [[0,0,0,0,0,0],[2,2,2,2,2,2],[4,4,4,4,4,4],[6,6,6,6,6,6]]
# ]


# Solution
op_lst = []

for i in range(3):
    print_lst = []
    for j in range(4):
        temp_lst = []
        for k in range(6):
            temp_lst.append(i * j)
        op_lst.append(temp_lst)
        print_lst.append(temp_lst)

    print(print_lst)

    
    

# Qn
#Write a Python program which takes a list of numbers as input and prints 
#a new list after removing even numbers from it.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [21,87,45,33,1]

# Solution
ip_lst = eval(input("Enter the list of numbers"))
op_lst = []

for i in ip_lst:
    if int(i) % 2 != 0:
        op_lst.append(i)

print("Output is", op_lst)



# Qn
#Write a Python program which takes a list from the user and prints it 
#after reshuffling the elements of the list.
#Input:- [10,21,22,98,87,45,33,1,2,100]
#Output:- [1,87,21,10,33,2,100,45,98,22] (It may be any randon 
#list but with same elements)

# Solution
import random
ip_lst = eval(input("Enter the list of numbers"))

#Method 1
op_lst = random.sample(ip_lst, len(ip_lst))
print("The shuffled list1 is : ",op_lst)

#Method2
random.shuffle(ip_lst)
print("The shuffled list2 is : ",ip_lst)







