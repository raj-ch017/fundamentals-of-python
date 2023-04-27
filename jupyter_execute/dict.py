#!/usr/bin/env python
# coding: utf-8

# # Dictionaries
# ---
# 
# **Learning Objectives**
# 
# - Leverage dictionaries to store more complex data, reference data by keys, and manipulate data stored
# 
# ---

# Dictionaries are a data structure in Python that are used to organize data into collections. Unlike lists, the data in a dictionary is not accessed based on its position. Instead, it is organized into pairs of keys and values. The key is used to access the corresponding value. A dictionary key can be a different data type, such as a string, integer, float, or tuple.
# 
# - To create a dictionary, you use curly brackets: `{}`. 
# 
# - To store values in a dictionary, you first specify the key, followed by a colon and the corresponding value, seperated by a comma. 
# 
#                 For example, animals = {"bears": 10, "lions": 1, "tigers": 2}
#     
# The above block represents a dictionary with three key-value pairs, stored in the variable **animals**. The key `"bears"` points to the integer value `10`, while the key `"lions"` points to the integer value `1`, and `"tigers"` points to the integer `2`.
# 
# - To access the values, the key can be referenced, like this: animals["bears"]. This returns the integer 10, since that is the corresponding value for this key.
# 

# ### Initializing Dictionaries

# In[1]:


empty_dict = {}

print("Dictionary: {}".format(empty_dict))
print("Type: {}".format(type(empty_dict)))


# In[2]:


animals = {"bears": 10, "lions": 1, "tigers": 2}

print("Number of bears: {}".format(animals['bears']))


# The `in` keyword can be used to check if a key is present in a dictionary. If the key is found in the dictionary, it returns `True`, otherwise it returns `False'.

# In[3]:


print("lion in dictionary: {}".format("lions" in animals),end="\n\n")

print("zebra in dictionary: {}".format("zebras" in animals))


# ### Mutability of Dictionaries

# Dictionaries are `mutable`, meaning they can be modified by adding, removing, and replacing elements.
# 
# - A new `key-value` pair can be added to a dictionary by assigning a value to a new key.
# 
# - Value of an existing key in the dictionary is also modified the same way. 
# 
# - The `del` keyword helps in removing elements from a dictionary.

# In[4]:


# Adding a new key-value pair: zebra - 25
animals['zebras'] = 25
print("Dictionary after adding Zebras: {}".format(animals),end="\n\n")

# Changing value of existing key: lions - 50
animals['lions'] = 50
print("Lion population changes: {}".format(animals),end="\n\n")

# Removing 'tigers' from the dictionary
del(animals['tigers'])
print("Final dictionary: {}".format(animals),end="\n\n")


# In Python, we can iterate over dictionaries using a `for loop`, similar to strings, lists, and tuples. However, since dictionaries have `key-value pairs`, the for loop will iterate over the sequence of keys in the dictionary. To access the corresponding values associated with the keys, we can use the keys as indexes.
# 
#  Alternatively, we can use the `items()` method on the dictionary, which returns a tuple for each element in the dictionary where the first element in the tuple is the key and the second element is the value.
# 

# In[5]:


print(animals,end="\n\n")

# Using '.items()' method   
for animal, count in animals.items():
    print("There are {} {} in the zoo.".format(count,animal))


# If we only wanted to access the keys in a dictionary, we can use the `keys()` method on the dictionary, which returns a list of all the keys in the dictionary. 
# 
# Similarly, if we only wanted the values, we can use the `values()` method, which returns a list of all the values in the dictionary.

# In[6]:


# Using '.keys()' method to obtain the keys of the dictionary
for animal in animals.keys():
    print("The zoo has {} in it.".format(animal))


# In[7]:


total = 0

# Using '.values' method to obtain the values of the dictionary
for amount in animals.values():
    total += amount 

print("There are total {} animals in the zoo.".format(total))


# ### Program 19
# ---
# 
# Write a function that takes a permission value in octal notation and returns a string representing the permissions in the symbolic notation.
# 
# 
# **Instructions**:
# 
# - Define a function named `octal_to_symbolic(permission)` that takes one parameter:
# 
#             permission: an integer value representing the permission in octal notation.
# 
# - In the function, convert the octal permission value to a string using the built-in `str()` function, which returns a string representing the octal notation of the given integer.
# - Extract the last three characters from the string. These represent the permission values for others, group, and owner.
# - Create a dictionary that maps each permission value to its symbolic notation: `'4' to 'r', '2' to 'w', and '1' to 'x'`.
# - Using string slicing and dictionary lookups, convert each permission value to its corresponding symbolic notation.
# - Return a string that represents the permission in symbolic notation.

# In[1]:


def octal_to_string(octal):
    
    """ 
    Convert an octal permission number to a string representation

    Parameter:
        octal (int): An octal number representing file permission bits

    Returns:
        str: A string representation of file permission bits
    
    """

    octal_in_str = str(octal)
    permission_list = []
    x = 1
    j = 0

    check_dict = {"0": "---", "1": "--x", "2": "-w-", "3": "-wx", "4": "r--", "5": "r-x", "6": "rw-", "7": "rwx"}

    for characters in octal_in_str:
        permission_list.append(check_dict[characters])
    
    output_str = "".join(permission_list)

    return output_str


# In[2]:


# Should be rwxr-xr-x
print("Run 1")
print(octal_to_string(755),end="\n\n")

# Should be rw-r--r--
print("Run 2")
print(octal_to_string(644),end="\n\n")

# Should be rwxr-x---
print("Run 3")
print(octal_to_string(750),end="\n\n")

# Should be rw-------
print("Run 4")
print(octal_to_string(600))


# ### Program 20
# ---
# 
# Write a Python function called `email_list` that takes one argument:
# 
#     users: a dictionary where each key is a domain name (string), and each value is a list of usernames (strings) for that domain.
# 
# 
# The function should create and return a list of complete email addresses for all users in the dictionary, in the format `"username@domain.com"`. 
# 
# For example, if the input dictionary is:
# 
#             {
#                 'gmail' : ['diana.prince', 'bruce.wayne']
#                 'yahoo' : ['clark.kent', 'lois.lane', 'peter.parker']
# 
#             }
# 
# The output list should be:
# 
#             ['diana.prince@gmail.com', 'bruce.wayne@gmail.com', 'clark.kent@yahoo.com', 'lois.lane@yahoo.com', 'peter.parker@yahoo.com']

# In[9]:


def email_list(domains):
    
    """ 
    Parameters:
        domains (dict): A dictionary containing domain names as keys 
                 and a list of users as values
 
    Returns:
        emails (list): A list of complete email addresses for all the 
        users in the input dictionary
    
    """
    emails = []

    for domain in domains.keys():
        for user in domains[domain]:
            x = user + "@" + domain
            emails.append(x)
    return(emails)

print("Run 1")
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# ### Program 21
# ---
# 
# Write a function named `add_prices` that returns the total price of all the groceries in the dictionary.

# In[10]:


def add_prices(basket):
    
    """
    Parameters:
        basket (dict): A dictionary containing the name of
        items as keys and their prices as values.
        
    Returns:
        The total price of all the items in the basket.
    """

    total = 0

    total = sum(list(basket.values()))

    return round(total,2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

# Should print 28.44
print("Run 1")
print(add_prices(groceries)) 


# ---
