                        # Python - Dictionary programs

# Qn
# Initialize a dictionary "emp_info" with below details
# In - emp_info['Tom']
# Out - {'email':'tom_latham019@gmail.com', 
#'Phone': +1987654321, 'City': 'California'}

# In - emp_info['Kathy']
# Out - {'email':'kathy_abram897@gmail.com', 
#'Phone': +1887654321, 'City': 'New York'}

main_dict={}
lst=[]

no_of_entry=eval(input("Enter number of employees' information that you wish to add"))
#Creating dictionary using user input
for i in range(no_of_entry):
    key = input("Enter the name of employee")
    values=input("Enter emailID,ph no, city separated by comma ','")
    lst=values.split(',')
    inner_dict={'email':lst[0],'Phone': lst[1], 'City': lst[2]}
    main_dict[key]=inner_dict
    lst.clear()

print(main_dict)

#Searching dictionary and printing corresponding user details
user_key =input("Enter name of employee whose detail you wish to see")
if user_key in main_dict.keys():
    print("Employee Info is:",main_dict[key])
else:
    print("Employee Info is not found")


# Qn
# Create a dictionary out of below inputs
# lst1 = ['emp1', 'emp2', 'emp3']
# emp_key = ['e_name', 'e_id', 'e_sal']
# emp1_val = ['John', 'SG101', '$10,000']
# emp2_val = ['Smith', 'SG102', '$9,000']
# emp3_val = ['Peter', 'SG103', '$9,500']

# Expected Output:-{'emp1':{'e_name':'John', 'e_id':'SG101', 'e_sal':$10,000}, 
#                   'emp2':{'e_name':'Smith', 'e_id':'SG102', 'e_sal':$9,000}, 
#                   'emp3':{'e_name':'Peter', 'e_id':'SG103', 'e_sal':$9,500}}

lst1 = ['emp1', 'emp2', 'emp3']
emp_key = ['e_name', 'e_id', 'e_sal']
emp1_val = ['John', 'SG101', '$10,000']
emp2_val = ['Smith', 'SG102', '$9,000']
emp3_val = ['Peter', 'SG103', '$9,500']

lst2=[emp1_val,emp2_val,emp3_val]
emp_info={}

#Creating dictionary with given inputs
for i in range(len(lst1)):
    emp_info[lst1[i]]=dict(zip(emp_key,lst2[i]))
    # print(list(emp_info.items())[i])

print(emp_info)


# Qn
# Acess the value of key 'history'

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

#Method 1 to access the value of key 'history'
print("History mark is:",sampleDict["class"]["student"]["marks"]["history"])

#Method 2 to access the value of key 'history'
print("History mark is:",sampleDict.get("class",{}).get("student",{}).get("marks",{}).get("history"))


# Qn
# Initialize dictionary with default values. Inputs are:-
# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}

#Expected output:- 
# {'Kelly': {'designation': 'Application Developer', 'salary': 8000}, 
#  'Emma': {'designation': 'Application Developer', 'salary': 8000}, 
#  'John': {'designation': 'Application Developer', 'salary': 8000}}

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

emp_info = dict.fromkeys(employees, defaults)
print(emp_info)


# Qn
# In gene expression, mRNA is transcribed from a DNA template. 
# The 4 nucleotide bases of A, T, C, G corresponds to the U, A, G, C bases 
# of the mRNA. 
# Write a function that returns the mRNA transcript given the sequence of 
# a DNA strand.

# Use a dictionary to provide the mapping of DNA to RNA bases.


# Function definition of function that returns the mRNA transcript 
# given the sequence of a DNA strand.

def mRNAtranscription(dna_template):
    dna2rna = {}
    mrna = ' '
    for i in dna_template:
        dna2rna = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
        if i in dna2rna.keys():
            mrna += (dna2rna.get(i))
        else:
            print("Invalid input. DNA strand should be sequence of A, T, C, G")
            ip_dna_template = input("Enter a valid sequence of DNA strand:")
            mrna = mRNAtranscription(str(ip_dna_template))
            return mrna
        
    return mrna


# Getting input DNA template from user
ip_dna_template = input("Enter the sequence of DNA strand:")

# Function call for mRNAtranscription
mRNA_transcript = mRNAtranscription(str(ip_dna_template))

print("RNA transcription is:", mRNA_transcript)




# Qn
# Write a function which takes a word as input and returns a dictionary with 
# letters as key and no of time letters are repeated as value.
# In - count_letter('google.com')
# Out - {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

#  Function definition of function which takes a word as input and returns 
# a dictionary 
#  with letters as key and no of times each letter is repeated as value.
def count_letter(ip_str):
    counter_dict = {}
    for i in ip_str:
        if i not in counter_dict.keys():
            counter_dict[i] = ip_str.count(i)

    return counter_dict

# Getting input string from user
input_string = eval(input("Enter a string"))

#Function call for count_letter
my_dict=count_letter(input_string)

#Printing the output
print(my_dict)


# Qn
# A DNA strand consisting of the 4 nucleotide bases is usually represented
# with a string of letters: A,T, C, G. 
# Write a function that computes the base composition of a given DNA sequence.

# In - baseComposition("CTATCGGCACCCTTTCAGCA")
# Out - {'A': 4, 'C': 8, 'T': 5,  'G': 3 }
    
# In - baseComposition("AGT")
# Out - {'A': 1, 'C': 0, 'T': 1,  'G': 1 }


#Solution:
#Function definition of function that computes the base composition 
# of a given DNA sequence

def baseComposition(dna_seq):
    nucleotide_base_key = ['A', 'C', 'T', 'G']
    base_comp_dict = {}
    for i in nucleotide_base_key:
        base_comp_dict[i] = dna_seq.count(i)

    print(base_comp_dict)



# Getting DNA sequence from user
input_string = input("Enter a DNA sequence")

# Function call for baseComposition function
baseComposition(input_string)


# Qn
# [MCQ] Suppose "d" is an empty dictionary, which statement does not
# assign "d" with {"Name":"Tom"}? 
# 1. d = {"Name": "Tom" }
# 2. d["Name"] = "Tom"
# 3. d.update({"Name": "Tom" })
# 4. d.setdefault("Name", "Tom")
# 5. None of the above.

# Solution
# All the above statements assign "d" with {"Name":"Tom"}
# So answer is 5. None of the above


# Qn
# [MCQ] d = {"a":1, "b":2}. Which of the statements returns [1,2]? 
# 1. d.keys()
# 2. d.values()
# 3. d.items()
# 4. d.popitem()
# 5. None of the above.

d = {"a":1, "b":2}
print(d.values())

#So option 2. d.values()  gives the values of the key in the dictionary


# Qn
# [MCQ] Which of the following declarations is not valid for 'dict' type?
# 1. d = {"Name": "Tom" }
# 2. d = { (1,3,4): 4.5 }
# 3. d = { ["First", "Last"]: (1,3) }
# 4. d = { 1: 0.4 }
# 5. None of the above

# Solution
# Answer is 3. d = { ["First", "Last"]: (1,3) } as list can't be used 
# as dictionary key as list is mutable and not hashable


# Qn
# Write a function reverseLookup(dictionary, value) that takes in a dictionary 
# and a value as arguments and returns a sorted list of all keys that 
# contains the value. 
# The function will return an empty list if no match is found.

# In - reverseLookup({'a':1, 'b':2, 'c':2}, 1)
# Out - ['a']
# In - reverseLookup({'a':1, 'b':2, 'c':2}, 2)
# Out - ['b', 'c']
# In - reverseLookup({'a':1, 'b':2, 'c':2}, 3)
# Out - []

# Function that returns a sorted list of all keys that contains the value.
# The function will return an empty list if no match is found.
def reverseLookup(dictionary, ip_value):
    out_list = []
    for key, dict_value in dictionary.items():
        if ip_value == dict_value:
            out_list.append(key)

    return sorted(out_list)


# Getting dictionary and value from user
ip_dict=eval(input("Enter a dictionary"))
inp_value=eval(input("Enter a value to search in dictionary"))

# Function call for reverseLookup function
output_list = reverseLookup(ip_dict, inp_value)
print(output_list)


# Qn
# Write a function invertDictionary(d) that takes in a dictionary as argument
# and return a dictionary that inverts the keys and the values of the 
# original dictionary.
# In - invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})
# Out - {1: ['a'], 2: ['b', 'd'], 3: ['c']}
# In - invertDictionary({'a':3, 'b':3, 'c':3})
# Out - {3: ['a', 'c', 'b']}
# In - invertDictionary({'a':2, 'b':1, 'c':2, 'd':1})
# Out - {1: ['b', 'd'], 2: ['a', 'c']}

# Function definition of function that inverts the keys and the values of 
# the original dictionary
def invertDictionary(dictionary):
    new_dict = {}
    for old_key, old_value in dictionary.items():
        new_value = old_key
        new_key = old_value
        if new_key not in new_dict.keys():
            a = new_dict.setdefault(new_key, list(new_value))
        else:
            new_dict[new_key].append(new_value)

    return new_dict


# Getting dictionary from user
ip_dict = eval(input("Enter a dictionary"))

# Function call for invertDictionary function
output_dict = invertDictionary(ip_dict)
print(output_dict)


# Qn
# Write a function that converts a sparse vector into a dictionary 
# as described above.
# In - convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])
# Out - {0: 1, 3: 2, 7: 3, 12: 4}
# In - convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0])
# Out - {0: 1, 2: 1, 4: 2, 6: 1, 9: 1}
# In - convertVector([0, 0, 0, 0, 0])
# Out - {}

#function that converts a sparse vector into a dictionary
def convertVector(ip_lst):
    new_dict = {}
    for i in range(len(ip_lst)):
        if int(ip_lst[i]) != 0:
            new_dict.update({ip_lst.index(ip_lst[i], i, len(ip_lst)): ip_lst[i]})

    print(new_dict)


# Getting list and value from user
sparse_vector_list = eval(input("Enter a sparse vector"))

# Function call for convertVector function
convertVector(sparse_vector_list)


# Qn
# Write a function that converts a dictionary back to its 
# sparse vector representation.
# In - convertDictionary({0: 1, 3: 2, 7: 3, 12: 4})
# Out - [1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]
# In - convertDictionary({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})
# Out - [1, 0, 1, 0, 2, 0, 1, 0, 0, 1]
# In - convertDictionary({})
# Out - []


# function that converts a dictionary back to its sparse vector representation.
def convertDictionary(ip_dict):
    if ip_dict != {}:
        last_item = ip_dict.popitem()
        out_list = [0] * int(last_item[0] + 1)
        out_list[last_item[0]] = last_item[1]

        for key, values in ip_dict.items():
            out_list[key] = values

    else:
        out_list = []

    print(out_list)


# Getting dictionary from user
inp_dict = eval(input("Enter a dictionary"))

# Function call for convertDictionary function
convertDictionary(inp_dict)


# Qn
# Given a Python dictionary, Change Brad’s salary to 8500
# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}
# }

# Expected Output
# sampleDict = {
#      'emp1': {'name': 'Jhon', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 8500}
# }

sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
print("Original dictionary is ", sampleDict)

ip_name = input("Enter the name of employee whose salary needs to be updated")
ip_salary = int(input("Enter salary of employee"))
chk_lst = []

for key, inner_dict in sampleDict.items():
    chk_lst.extend(list(inner_dict.values()))
    if ip_name in inner_dict.values():
        emp_name = inner_dict['name']
        emp_salary = inner_dict['salary']
        if emp_name == ip_name:
            inner_dict['salary'] = ip_salary

if ip_name not in chk_lst:
    print("Name not found")
else:
    print("Updated dictionary is ", sampleDict)


# Qn
# Get the key corresponding to the minimum value from the following dictionary
# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# Expected Output
# Math

ip_dict = {'Physics': 82, 'Math': 65, 'History': 75}
print("Original dictionary is:", ip_dict)

#Getting values list and key list
val_lst = list(ip_dict.values())
key_lst = list(ip_dict.keys())

#Getting minimum value from the dictionary
minimum_val = min(val_lst)
print("The minimum value in the list is:", minimum_val)

#Printing the key corresponding to minimum value in dictionary
print("Key corresponding to the min value : ",minimum_val," in the dictionary is:", key_lst[val_lst.index(minimum_val)])


# Qn
# Rename key city to location in the following dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# Expected Output
# {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "location": "New york"
# }

#Getting dictionary from user
ip_dict = eval(input("Enter a dictionary"))
print("Original dictionary is ", ip_dict)

#Getting old key and new key from the user
old_key = str(input("Enter a key whose value needs to be updated"))
new_key= str(input("Enter the new key"))

#Updating the dictionary
ip_dict[new_key]=ip_dict[old_key]

#Printing the updated dictionary
print("Updated dictionary is ", ip_dict)


# Qn
# Check if a value 200 exists in a dictionary
# sampleDict = {'a': 100, 'b': 200, 'c': 300}
# Expected Output: True


#Getting dictionary from user
ip_dict = eval(input("Enter a dictionary"))
print("Original dictionary is ", ip_dict)

#Getting input value from the user
ip_value = eval(input("Enter a value"))

#Checking if the value exists in a dictionary and printing the output
print("Does",ip_value,"exist in Dictionary ?",ip_value in ip_dict.values())


# Qn
# Delete set of keys from Python Dictionary
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
  
# }
# keysToRemove = ["name", "salary"]

# Expected Output:
# {'city': 'New york', 'age': 25}

# Getting dictionary from user
ip_dict = eval(input("Enter a dictionary"))
print("Original dictionary is ", ip_dict)

# Getting keys to delete from the user
ip_str = str(input("Enter keys to remove separated by ',' comma"))
lst = ip_str.split(',')
print("Keys to remove are:",lst)

#Removing the keys from the dictionary
for i in lst:
    value = ip_dict.pop(i)

#Printing the updated dictionary
print("Updated dictionary is ", ip_dict)

