#!/usr/bin/env python
# coding: utf-8

# # Exercise Book: Strings, Lists and Dictionaries
# ---
# 
# This notebook includes a series of exercises that focus on strings, lists, and dictionaries. Through these exercises, emphasis is placed on developing problem-solving skills and intuition on which data structure to use in different scenarios, with the goal of becoming a better programmer.
# 
# ---

# ### Exercise 1
# 
# You are tasked to implement a function called `format_address(address)` that separates out parts of the `address string` into `new strings: house_number and street_name`, and returns:
# 
#             `"house number X on street named Y"`. 
# 
# The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. 
# 
# **For example**:
# 
#             "123 Main Street", "1001 1st Ave", or "55 North Center Drive".
# 
# 
# The function should take in one parameter:
# 
# - `a string address` representing the address to be formatted.

# In[1]:


def format_address(address_string):
    """ 
    Parameters:
        address_string (str): A string representing the address
        with a numerica house number followed by the street name

    Returns:
        A formatted string containing the house number and
        the street name separated by the words 
        "on street named". 
    """

    list1 = address_string.split(" ")
    house_number = list1[0]
    list1.pop(0)
    street_number = " ".join(list1)
    address_str = "house number {} on street named {}".format(house_number,street_number)
    return address_str


# In[2]:


# Should print: "house number 123 on street named Main Street"
print("Run 1")
print("Output Returned: {}".format(format_address("123 Main Street")),end="\n\n")

# Should print: "house number 1001 on street named 1st Ave"
print("Run 2")
print(format_address("1001 1st Ave"),end="\n\n")

# Should print "house number 55 on street named North Center Drive"
print("Run 3")
print(format_address("55 North Center Drive"))


# ---
# 
# ### Exercise 2
# 
# The function `replace_domain` takes an `email` address, an `old_domain`, and a `new_domain` as arguments. If the email address contains the `old_domain`, the function replaces it with the `new_domain` and returns the updated email address. If the email address does not contain the `old_domain`, the function simply returns the original email address.
# 

# In[3]:


def replace_domain(email,old_domain,new_domain):
    """
    Parameters:
        email (str): The email address to modify
        old_domain (str): The domain to replace in the email address
        new_domain (str): The new domain to replace the old domain with
        
    Returns:
        str: The modified email address with the new domain
    """

    if "@" + old_domain in email:
        index = email.index("@")
        new_email = email[:index] + "@" + new_domain
        return new_email
    
    return email


# In[4]:


# Input = viktor_pal17@yahoo.com , Expected Output = viktor_pal@google.com
print("Run 1")
print(replace_domain("viktor_pal17@yahoo.com","yahoo.com","google.com"),end="\n\n")


# Input = jesse_roy@google.com, Expected Output = jesse_roy@gmail.com
print("Run 2")
print(replace_domain("jesse_roy@google.com","google.com","gmail.com"),end="\n\n")


# ---
# 
# ### Exercise 3
# 
# You are given three lists: `drews_list`, `jamies_list`, and `professors_list`. The two lists, `drews_list` and `jamies_list` contain the names of the students in the order they arrived in the classroom. The professor needs to combine `drews_list` and `jamies_list` into one list in the order that the students arrived.
# 
# However, Jamie's list is in reverse order, so you need to reverse it before combining it with Drew's list. Write a function named `combine_lists` to take in the two lists and return the combined list in the correct order.
# 
# **Input**:
# 
# - drews_list (list): A list of strings containing the names of students in the order they arrived in the classroom. Length is n.
# 
# - jamies_list (list): A list of strings containing the names of students in reverse order that Jamie noted. Length is m.
# 
# **Output**:
# 
# - Returns a list of strings containing the names of students in the order they arrived in the classroom. The length of the combined list should be n + m.
# 

# In[5]:


def combine_lists(list1,list2):
    """ 
    Parameters:
        list1 (list): A list of strings containing the name of students in
                      the reverse order that Jamie noted
        list2 (list): A list of strings containing the name of students in 
                      the order they arrived in the classroom

    Return:
        final_list (list): A list of strings containing the names of students 
                            in the order they arrived in the classroom.
    """

    first_list = list2
    second_list = []
    length_list1 = len(list1)
    count = -1

    for index in range(length_list1):

        student_name = list1[count]
        second_list.append(student_name)
        count -= 1
        if abs(count) > length_list1:
            break
    
    final_list = first_list + second_list
    return (final_list)


# In[6]:


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print("Jamies' List: {}".format(Jamies_list))
print("Drews' List: {}".format(Drews_list),end="\n\n\n")

print("Run 1")
print("Expected Output: ['Mike', 'Carol', 'Greg', 'Marcia', 'Peter', 'Jan', 'Bobby', 'Cindy', 'Alice']")
print("Output Returned: {}".format(combine_lists(Jamies_list, Drews_list)))


# ---
# 
# ### Exercise 4
# 
# You are tasked with combining two dictionaries, containing information about the guests attending a party hosted by Taylor and Rory. The two dictionaries are named `taylor_guests` and `rory_guests`.
# 
# `taylor_guests` contains partial information about the guests attending the party, where the **key** is the `name of the guest` and the **value** is the `number of guests` the guest is bringing. `rory_guests` also contains similar information but with more current and updated data about the guests.
# 
# Write the code to combine both dictionaries into one, with each friend listed only once, and the number of guests from `rory_guests` taking precedence, if a name is included in both dictionaries. Finally, print the resulting dictionary.
# 
# **Note**
# - `taylor_guests` contains 2 guests for "Alice" while `rory_guests` contains guest for "Alice". Therefore, the combined dictionary contains "Alice" with 1 guest, taking the value from `rory_guests`.

# In[7]:


def combine_guests(guests1,guests2):
    """ 
    Parameters:
        taylor_guests (dict): A dictionary with names of guests as keys and the
                              number of guests each friend is bringing as values
        rory_guests (dict): A dictionary with names of guests as keys and the
                            number of guests each friend is bringing as values

    Returns:
        A dictionary with each friend listed only once, and the number of guests
        rory_guests taking precedence, if a name is included in both dictionaries
    """
    
    # guests1 represents Rory's list
    # guests2 represents Taylor's list

    final_dict = {}
    r_guestlist = list(guests1.keys())
    t_guestlist = list(guests2.keys())
    actual_guestlist = r_guestlist + t_guestlist
    
    for names in actual_guestlist:

        if names in guests1:
            peeps_they_bring = guests1[names]
            final_dict[names] = peeps_they_bring
        
        elif names in guests2:
            peeps_they_bring = guests2[names]
            final_dict[names] = peeps_they_bring
        
        if names in t_guestlist and names in r_guestlist:
            b = guests1[names]
            final_dict[names] = b
    
    return final_dict


# In[8]:


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print("Rory's Guest List: {}".format(Rorys_guests))
print("Taylor's Guest List: {}".format(Taylors_guests),end="\n\n\n")

print("Run 1")
print(combine_guests(Rorys_guests, Taylors_guests))


# ---
# 
# ### Exercise 5
# 
# You are given an input string, and your task is to write a function `count_letters(string)` to count the frequency of letters in the input string. The output should be a dictionary where the keys are the lowercase letters that appear in the string, and the values are the frequency of those letters.
# 
# **Note**:
# 
# - Only letters should be counted, not blank spaces, numbers, or punctuation.
# - Upper case should be considered the same as lower case.

# In[9]:


def count_letters(text):
    """ 
    Parameters:
        text (str): A string of length n containing letters, blank spaces,
        numbers and punctuation
            
    Return:
        A dictionary where the keys are lowercase letters that appear 
        in the input string, and the values are the frequency of
        those letters.
    """
    
    result = {}
    text_lower = text.lower()
    text_in_list = text_lower.split()
    
    for words in text_in_list:
        
        for letter in words:
            
            if letter.isalpha():
                count = 1
                
                if letter not in result:
                    result[letter] = count
                
                else:
                    character = result[letter]
                    count = character + 1
                    result[letter] = count
    return result


# In[10]:


# Should be {'a': 2, 'b': 2, 'c': 2}
print("Run 1")
print("Output: {}".format(count_letters("AaBbCc")),end="\n\n")


# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print("Run 2")
print("Output: {}".format(count_letters("Math is fun! 2+2=4")),end="\n\n")

# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
print("Run 3")
print("Output: {}".format(count_letters("This is a sentence.")),end="\n\n")


# ---
# 
# ### Exercise 6
# 
# Create a program that reads integers from the user
# until a blank line is entered.
# 
# Once all of the integers have been read, your program
# should display all of the negative numbers, followed
# by all of the zeros, followed by all of the positive
# numbers.
# 
# Within each group the numbers should be displayed in
# the same order that they were entered by the user.
# 
# For example, if the user enters the values:
# 
#     3, -4, 1, 0, -1, 0 and -2
#     
# Then your program should output the values:
# 
#     -4, -1, -2, 0, 0, 3 and 1
#     
# Your program should display each value on it's own
# line.

# In[11]:


# Generating a list

user_list = []
flag = True

while flag:
    user_in = input("Enter a number: ")
    
    if user_in == "":
        flag = False
        
    else:
        user_list.append(int(user_in))


# In[12]:


def list_group(input_list):
    """
    Group a list of numbers into three categories: negatives, zeros and positives.

    Parameters:
        input_list (list) : list of int or float

    Returns:
        A new list with the same numbers as `input_list`, but sorted into three
        sub-lists in this order: negatives, zeros, positives.
    """    
    
    negative_list = []
    zero_list = []
    positive_list = []
    output_list = []
    
    for ele in input_list:
        
        if ele < 0:
            negative_list.append(ele)
        elif ele == 0:
            zero_list.append(ele)
        else:
            positive_list.append(ele)
            
    output_list.extend(negative_list)
    output_list.extend(zero_list)
    output_list.extend(positive_list)
    
    return output_list


# In[13]:


ordered_list = list_group(user_list)

# Expected output = [-4, -1, -2, 0, 0, 3, 1]
print("Run 1")
print('Initial list: {} | Ordered list: {}'.format(user_list,ordered_list))


# ---
# 
# ### Exercise 7
# 
# 
# A proper divisor of a positive integer (n) is a positive
# integer less than (n) which divides evenly into n.
# 
# Write a function that computes all of the proper
# divisors of a positive integer. The integer will be
# passed to the function as it's only parameter.
# 
# The function will return a list containing all of the
# proper divisors as its only result. Complete this 
# exercise by writing a main program that demonstrates 
# the function by reading a value from the user and 
# displaying the list of its proper divisors. Ensure 
# that your main program only runs when your solution has 
# not been imported into another file.
# 

# In[14]:


def proper_divisors(n):
    """
    Parameters:
        n (int) - positive integer
        
    Returns:
        divisor_list - A list containing all of the
        proper divisors of n
    """
    
    divisor_list = []
    
    for value in range(1,n):
        
        if (n % value) == 0:
            divisor_list.append(value)
            
    return divisor_list


# In[15]:


print("Proper Divisors for numbers 1 - 50",end = "\n\n")

for run in range(1,51):
    
    print("{} | {}".format(run,proper_divisors(run)))


# ---
# 
# ### Exercise 8
# 
# An integer (n) is said to be perfect when the sum of
# all of the proper divisors of (n) is equal to (n).
# 
# **For example**:
# 
#     28 is a perfect number because it's proper divisors
#     are 1, 2, 4, 7, 14 and 1 + 2 + 4 + 7 + 14 = 28
#     
# Write a function that determines whether or not a 
# positive integer is perfect. Your function will take
# one parameter. If that parameter is a perfect number,
# then your function will return true. Otherwise, it 
# will return false.
# 
# In addition, write a main program that uses your
# function to identify and display all of the perfect
# numbers between 1 and 10,000.
# 
# Import your solution to previous exercise when completing
# this task.

# In[16]:


def perfect_number(input_number):
    """
    Parameters:
        input_number (int): a number to check whether it's a perfect number
        
    Returns:
        True if the parameter turns out to be perfect number, else
        False
    """
    
    divisor_list = proper_divisors(input_number)
    the_sum = sum(divisor_list)
    
    if the_sum == input_number:
        return True
    else:
        return False


# In[17]:


perfect_numlist = []

for j in range(1,10001):
    
    if perfect_number(j):
        #print("{}: Yes".format(j))
        perfect_numlist.append(j)

print("Here is a list of perfect numbers between 1 and 10,000: \n{}\n\n".format(perfect_numlist))    

print("For the first 10,000 positive integers, only {}% are perfect numbers".format(len(perfect_numlist)/10000 * 100))


# ---
# 
# ### Exercise 9
# 
# Write a program that reads numbers from the user until
# a blank line is entered. Your program should display
# the average of all of the values entered by the user.
# 
# Then the program should display all of the below
# average values, followed by all of the average values
# (if any), followed by all of the above average grades.
# An appropriate label should be displayed before each
# list of values.

# In[18]:


the_avg = 0
flag = True
store_list = []

while flag:
    
    user_in = input("Enter a number: ")
    
    if user_in != "":
        store_list.append(float(user_in))
    else:
        flag = False
        
the_avg = sum(store_list) / len(store_list)

below_average = []
just_average = []
above_average = []

for val in store_list:
    
    if val < the_avg:
        below_average.append(val)
    elif val == the_avg:
        just_average.append(val)
    else:
        above_average.append(val)


# In[19]:


print("Average value: {}".format(the_avg))
print("Numbers below average: {}".format(below_average))
print("Numbers equal to average: {}".format(just_average))
print("Numbers above average: {}".format(above_average))


# ---
# 
# ### Exercise 10
# 
# Two words are anagrams if they contain all of the same
# letters, but in a different order.
# 
# **For example**, `evil` and `live` are anagrams because
# each contains one 'e', one 'v', one 'i' and one 'l'.
# 
# Create a program that reads two strings from the user,
# determines whether or not they are anagrams, and
# reports the result.

# In[20]:


def check_anagram(str1,str2):
    
    """
    Check if two input strings are anagrams of each other.

    Parameters:
        str1 (str): First input string.
        str2 (str): Second input string.

    Returns:
        bool: True if the input strings are anagrams of each other, False otherwise.
        int: -1 if the input strings are of different lengths.

    """
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    if len(str1) == len(str2):
        
        dict1 = {}
        dict2 = {}
        
        for k in range(len(str1)):
            char1 = str1[k]
            char2 = str2[k]
            
            if char1 not in dict1:
                dict1[char1] = 1
            else:
                dict1[char1] = dict1[char1] + 1
                
            if char2 not in dict2:
                dict2[char2] = 1
            else:
                dict2[char2] = dict2[char2] + 1
                
        if dict1 == dict2:
            return True
        else:
            return False
        
    else:
        return -1


# In[21]:


print("Run 1",end="\n\n\n")

user_str1 = input("Enter a string: ")
user_str2 = input("Enter another string: ")

is_anagram = check_anagram(user_str1,user_str2)

if is_anagram == True:
    print("\n'{}' and '{}' are anagrams".format(user_str1,user_str2))
    
elif is_anagram == -1:
    print("\nString lengths different, invalid entry")
    
else:
    print("\n'{}' and '{}' are not anagrams".format(user_str1,user_str2))


# In[22]:


print("Run 2",end="\n\n\n")

user_str1 = input("Enter a string: ")
user_str2 = input("Enter another string: ")

is_anagram = check_anagram(user_str1,user_str2)

if is_anagram == True:
    print("\n'{}' and '{}' are anagrams".format(user_str1,user_str2))
    
elif is_anagram == -1:
    print("\nString lengths different, invalid entry")
    
else:
    print("\n'{}' and '{}' are not anagrams".format(user_str1,user_str2))


# In[23]:


print("Run 3",end="\n\n\n")

user_str1 = input("Enter a string: ")
user_str2 = input("Enter another string: ")

is_anagram = check_anagram(user_str1,user_str2)

if is_anagram == True:
    print("\n'{}' and '{}' are anagrams".format(user_str1,user_str2))
    
elif is_anagram == -1:
    print("\nString lengths different, invalid entry")
    
else:
    print("\n'{}' and '{}' are not anagrams".format(user_str1,user_str2))


# ---
