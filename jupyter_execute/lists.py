#!/usr/bin/env python
# coding: utf-8

# 
# ### Lists and Tuples
# ---
# 
# **Learning Objective**
# 
# - Use lists and tuples to store, reference, and manipulate data
# 
# ---

# 
# In Python, `lists` are defined using square brackets and can contain multiple elements separated by commas. For instance, a list of words can be defined as:
#  
#             list1 = ["This", "is", "a", "list"]. 
#  
#  The `len()` function can be used to determine the number of elements in a list, as in:
#  
#             len(list1) = 4. 
#  
#  
#  Similarly, the `in` keyword can be used to check if an element is present in the list. If the element is found, it returns `True`, and `False` otherwise. For example:
#  
#             "This" in list1 would return `True`.

# In[1]:


days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

print("List: {}".format(days),end="\n\n")

print("Length: {}".format(len(days)),end="\n\n")


# ### List Operations
# 
# - The `append` method is used to add an element to the end of a list. This method is called using dot notation, and the element to be added is passed as a parameter.
# 
# 
# **For instance**, `list1.append("New data")` adds "New data" to the end of the list called list1.
# 
# 
# - To add an element to a specific position in a list, we use the `insert` method. This method takes two parameters: the **index** at which the element is to be inserted and the **element** to be inserted. If the index specified is larger than the length of the list, the element will be added to the end of the list.
# 
# 
# **For example**, `list1.insert(0, "New data")` inserts "New data" at the front of the list, without overwriting the existing element.
# 
# 
# - The `remove` method removes elements from the list. This method takes an `element` as a parameter and removes the first occurrence of that element from the list. If the element isn't found in the list, a `ValueError` error is raised.
# 
# 
# - Alternatively, elements can also be removed from a list using the `pop` method. This method takes an `index` as a parameter and returns the element that was removed.
# 
# 
# - Finally, you can change the value of an element in a list by using `indexing` to access the specified index and overwrite the value stored there.
# 
# 
# **For example**, `list1[0] = "Old data"` would replace the first element in the list with "Old data".
# 
# 
# 
# 

# In[2]:


food_menu = ["Pizza","Pasta","Caesar Salad","Burger"]
print("Initial list: {}".format(food_menu),end="\n\n")

# Using `.append()` to add 'Tacos'
food_menu.append("Tacos")
print("List after appending: {}".format(food_menu),end="\n\n")

# Using `.insert()` to add 'Chicken Wings' at index 0
food_menu.insert(0,"Chicken Wings")
print("Chicken Wings added: {}".format(food_menu),end="\n\n")

# Using `.remove()` to remove 'Pasta' 
food_menu.remove("Pasta")
print("Pasta has been removed: {}".format(food_menu),end="\n\n")

# Using `.pop()` to remove 'Caesar Salad'
food_menu.pop(-3)
print("Caesar Salad removed: {}".format(food_menu),end="\n\n")

# Using indexing to change 'Burger' to 'Burger & Fries' 
food_menu[-2] = "Burger & Fries"
print("Our final menu: {}".format(food_menu),end="\n\n")


# ### Tuples
# ---
# 
# In Python, tuples are similar to lists in that they can store multiple values in a single variable, but they have an important difference: **tuples are immutable**, meaning they cannot be changed once created. This makes tuples useful when we need to ensure that an element remains in a certain position and will not be changed by other parts of the program.
# 
# One common use case for tuples is when a function returns multiple values. In this case, the values are often packed into a tuple, with each value being an element in the tuple. Since the order of the returned values is important, using a tuple ensures that the order will not change unexpectedly.
# 
# To access the values in a tuple, we can use `indexing` just like with lists. However, Python also allows us to unpack the values of a tuple into separate variables. This can be useful when we want to use the individual values in different parts of our program. To do this, we simply assign the tuple to multiple variables, with one variable for each element in the tuple.
# 

# In[3]:


name = ("Aldous","Marx","Fleischman")

first_name, middle_name, last_name = name 

print("First Name: {}\nMiddle Name: {}\nLast Name: {}".format(first_name,middle_name,last_name),end="\n\n")

print("Initials: {}{}{}".format(first_name[0],middle_name[0],last_name[0]))


# ### `Enumerate()` - List labeling service
# 
# The `enumerate()` function is a built-in Python function that allows you to loop over an iterable (e.g., a list, tuple, or string) and get both the index and the value of each element. 
# 
# It returns a tuple for each element in the list. The first value in the tuple (`index 0`) is the index of the element in the list, while the second value is the element itself.

# In[4]:


team_list = ["Arsenal","Man City", "Spurs", "Newcastle","Man Utd"]

for pos, team in enumerate(team_list):
    print("{} - {}".format(pos+1,team))


# ### List Comprehension
# 
# List comprehensions allows us to create new lists based on a sequence or range of values.
# 
# **For example** - `[x**2 for x in range(1,11)]` is a simple list comprehension. This expression generates a new list by iterating over the range of integers from 1 to 10, raising each of them to an exponent of 2 and storing the result in the new list.

# In[5]:


square_list = [x**2 for x in range(1,11)]

print("Square of integers from 1 to 10: {}".format(square_list),end="\n\n")

cube_list = [x**3 for x in range(1,11)]

print("Cube of integers from 1 to 10: {}".format(cube_list),end="\n\n")


# `Conditionals` can also be used to create more sophisticated and powerful list comprehensions. This is done by simply adding an `if statement` to the end of the comprehension.
# 
# **For instance** - `[x for x in range(1,101) if x % 7 == 0]` produces a list containing all integers from 1 to 100 that are divisible by 7. In this case, the if statement evaluates each value in the range to determine if it is divisible by 7. If the result is `True`, then it adds the value to the list.

# In[6]:


# List Comprehension with Conditionals

div_by_7 = [x for x in range(1,101) if x % 7 == 0]

print("Multiples of 7 from 1 to 100: {}".format(div_by_7))


# ### Program 15
# ---
# 
# You are given a list of filenames. Your task is to rename all the files with extension hpp to the extension h. You should generate a new list called newfilenames, which will consist of the new filenames.
# 
#             filenames = ["program.cpp", "data.hpp", "output.hpp", "file.hpp"]
#             newfilenames = []

# In[7]:


def change_filename(filenames):
    """
    Changes the file extension from '.hpp' to '.h'
    in the given list of filenames.
    
    Parameters:
        filenames (list): A list of filenames.
    
    Returns:
        list: A new list of filenames with 
        the extension changed from '.hpp' to '.h'.
    """
    x = 0
    to_check = '.hpp'
    newfilenames = []
    
    for file in filenames:
        
        if to_check in file:
            x = file.split(".")
            y = x[0] + ".h"
            newfilenames.append(y)
        
        else:
            newfilenames.append(file)
    
    return newfilenames


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
print("Run 1")
print("Input list: {}".format(filenames))
print("Output list: {}".format(change_filename(filenames)))


# ### Program 16
# ---
# 
# Write a function called `pig_latin()` that takes a string as input and returns the pig latin version of the string. The function should perform the following steps:
# 
# - Convert the string to a list of words using the split() method.
# - For each word in the list, move the first letter to the end of the word and append "ay" to the end.
# - Join the list of words back into a single string using the join() method, with a space between each word.
# - Return the resulting pig latin string.
# 
# **For example**, the input string "Let's create pig latin" should produce the output string "et'sLay reatecay igpay atinlay".

# In[1]:


def pig_latin(text):
    
    """ 
    A function that converts texts into pig latin by moving the
    first character of each word to the end and appending 'ay' to it.

    Parameters:
        text(str): The text to be converted into pig latin.

    Returns:
        str: The converted text in pig latin.
    """
    
    words = text.split(" ")
    say = []
    
    for word in words:
        
        first_char = word[0]
        word_to_add = word[1:]
        new_word = word_to_add + first_char + "ay"
        say.append(new_word)
    
    saying = " ".join(say)
    return saying


# In[2]:


# Should be "ellohay owhay reaay ouyay"
print("Run 1")
print("Input: {}".format("hello how are you"))
print("Output: {}".format(pig_latin("hello how are you")),end="\n\n\n")

# Should be "rogrammingpay niay ythonpay siay unfay"
print("Run 2")
print("Input: {}".format("programming in python is fun"))
print("Output: {}".format(pig_latin("programming in python is fun")))


# ### Program 17
# ---
# 
# Write a Python function `group_list` that accepts two parameters:
# 
#     group_name: A string representing the name of the group.
#     members: A list containing the members of the group.
# 
# The function should return a string in the format `"group_name: member1, member2, ..."` where each member is separated by a comma and a space.
# 
#      For example, calling group_list("g", ["a", "b", "c"]) should return the string "g: a, b, c".
# 

# In[3]:


def group_list(group, users):
    """
    Returns a string with the format "group_name: member1, member2, ..."
    
    Parameters:
        group (str): The name of the group
        users (list): A list of members
    
    Returns:
        str: A string with the format "group_name: member1, member2, ..."
    """
    
    members = users
    member_list = []
    x = len(members)
    group_stat = group + ": "
    
    for y in range(x):
        j = members[y]
        member_list.append(j)
    
    out_str = ", ".join(member_list)
    final_list = group_stat + out_str
    return final_list


# In[4]:


# Should be "Marketing: Mike, Karen, Jake, Tasha"
print("Run 1")
print("Output: {}".format(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])),end="\n\n")

# Should be "Engineering: Kim, Jay, Tom"
print("Run 2")
print(group_list("Engineering", ["Kim", "Jay", "Tom"]),end="\n\n")

# Should be "Users:"
print("Run 3")
print(group_list("Users", "")) 


# ### Program 18
# ---
# 
# Write a function that reads in a list of tuples representing party guests, where each tuple contains the guest's name, age, and profession. The function should then print out a sentence for each guest in the format `"Guest is X years old and works as __."` with the appropriate values inserted for name, age, and profession.
# 
# For example, if the input list is `[('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")]`, the function should output:
# 
#     Ken is 30 years old and works as Chef.
#     Pat is 35 years old and works as Lawyer.
#     Amanda is 25 years old and works as Engineer.

# In[10]:


def guest_list(guests):
    
    """ 
    Parameters:
        guests: a list of tuples where each tuple contains the name,
        age, and profession of a guest.

    Returns:
        None
    """
    
    for i in range(len(guests)):
        
        name, age, profession = guests[i]
        print("{} is {} years old and works as {}".format(name,age,profession))
    
    return None 


#Output should match:

#Ken is 30 years old and works as Chef
#Pat is 35 years old and works as Lawyer
#Amanda is 25 years old and works as Engineer

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])


# ---
