#!/usr/bin/env python
# coding: utf-8

# # Strings
# ---
# 
# **Learning Objectives**
# 
# - Manipulate strings using indexing, slicing, and formatting
# 
# ---

# 
# A `string` is a data type utilized to denote a sequence of characters. The string is enclosed in quotes, either double quotes or single quotes, with the option to choose either one. **It is important to use matching quotes since using mismatched quotes will result in a syntax error**. 
# 
# A string can range from having zero length, called an **Empty String**, to an extremely lengthy sequence of characters. 
# 
# **Concatenation**, accomplished by using the plus sign, is a means of building longer strings using shorter ones. A less common operation is to multiply the string by a number, resulting in the content of the string being repeated that many times.

# In[1]:


fruit = "Pineapple"

print("The word 'Pineapple' is",len(fruit),"characters long.")


# The `len()` function is a built-in function that returns the number of items in a sequence or the number of characters in a string, which in the case of 'Pineapple' is 9.

# ### String Indexing and Slicing
# 
# String indexing enables accessing individual characters in a string through the use of square brackets and the location or index of the character to be accessed. Python starts indexing at 0, so to access the first character in a string, one would use the index [0].

# In[2]:


print("The first character in",fruit,"is",fruit[0])


# Attempting to access an index that's greater than the string's length raises an `IndexError` as the accessed item doesn't exist.

# In[3]:


# Running this code raises 'IndexError'
##print(fruit[9])


# The word 'Pineapple' having 9 characters, has index values ranging from 0 to 8. 
# Therefore, using '9' as index to access a character in it produces an error.


# Negative index values can also be used to access the string's indexes from the end towards the start, with `[-1]` accessing the last character and `[-2]` accessing the second-to-last character.
# 
# Additionally, a slice or substring of a string, which comprises multiple characters, can be accessed. To do so, a range is created using a colon as a separator between the start and end of the range, such as `[2:5]`.

# In[4]:


print("The last character for",fruit,"is",fruit[-1])

print("The substring from index 4 to index 6 for",fruit,"gives:",fruit[4:7])


# An alternative approach for defining the range involves specifying only one of the two indices. In this scenario, it is implied that the missing index corresponds to either the first value of 0 or the second value of the string's length.

# In[5]:


print("The substring of first four characters in",fruit,"is",fruit[:4])

print("The substring of last five characters in",fruit,"is",fruit[4:])


# Stings are **immutable**, which means they cannot be changed. Modifying a single character within a `string` is not possible, and any correction requires creating a new string that fixes the mistake. Alternatively, one can reassign the variable that holds the string to a new value with the mistake fixed.

# In[6]:


greeting = "Hellop, world!"

print("Old greeting:",greeting)

new_greeting = greeting[:5] + ", " + greeting[-6:-1]

print("New greeting:",new_greeting)


# To locate the index of a specific character or subtring within a string, we can use the string method called `index()`. This method returns the index of the first occurrence of a character or substring. If the index is not found in the string, then a `ValueError` is raised. In case of multiple matches, only the index of the first occurrence is returned.
# 
# To avoid a **ValueError**, the `in` keyword can be used to first check if the substring exists in the string. It is used as a conditional operator and returns a boolean value of `True` if the substring exists in the string and `False` otherwise.

# In[7]:


new_string = "An apple a day keeps the doctor away."

if 'apple' in new_string:
    print("'apple' is located at index",new_string.index('apple'))


# ### String Methods
# 
# - The `lower()` and `upper()` string methods can be used to convert a string to all lowercase or all uppercase characters, respectively. These methods are called using dot notation on a string and can be useful when checking user input.
# 
# - The `strip()` method can be used to remove any whitespace characters, such as spaces, tabs `(\t)`, and newline characters `(\n)`, from the beginning and end of a string.
# 
# - The `count()` method can be used to count the number of times a substring appears in a string.
# 
# - The `endswith()` method can be used to check if a string ends with a particular substring. If the substring is found at the end of the string, the method will return `True`, otherwise it will return `False`.
# 
# - The `isnumeric()` method can be used to determine if a string contains only numeric characters. If the string contains only numbers, the method will return `True`. This can be useful for checking if a string can be converted to an integer using the `int()` function.
# 
# - The `join()` method can be used for concatenating strings. This method is called on a string and takes a list of strings as parameter. It returns a new string composed of the strings from the list joined using the initial string.
# 
# - The inverse of the `join()` method is the `split()` method, which splits a string into a list of strings. By default, the `split()` method splits the string by any whitespace characters, but it can also split by any other character specified by a parameter.

# In[8]:


basic_string = "This is the test string."

# Using `.upper()`
print("Converting to upper-case:",basic_string.upper(),end="\n\n")

# Using '.lower()'
print("Converting to lower-case:",basic_string.lower(),end="\n\n")

# Using '.count()'
print("Frequency of 's':",basic_string.count('s'),end="\n\n")

# Using '.isnumeric()'
print("Is the string numeric?",basic_string.isnumeric(),end="\n\n")

string_to_join = ["Today","is","Monday.","We","are","going","to","the","beach","on", "Saturday."]

# Using '.join()`
joined_string = " ".join(string_to_join)
print(joined_string,end="\n\n")

# Using `.split()`
print("Splitting 'This is the test string' gives us",basic_string.split())


# ### String Formatting
# 
# The `format()` method provides a powerful way to concatenate and format strings. The format method works by creating a string containing curly brackets `{}` as placeholders, to be replaced. We then call the format method on the string using `.format()` and pass variables as parameters. The method automatically handles any necessary conversion between data types.
# 
# If the curly brackets are left empty, the variables are populated in the order they're passed.

# In[9]:


# base string with {} placeholders

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)


# However, we can use expressions inside the curly brackets to do more powerful string formatting. For example, we can put the variable name inside the curly brackets and use its name as a parameter. This provides more readable code and more flexibility with the order of variables.

# In[10]:


# Variable name inside curly brackets

name = "Swanson"
job = "Researcher"

print("Hello, I am {name} and I am a {job}!".format(name=name,job=job))


# If the placeholders indicate a number, they are replaced by the variable corresponding to that order (starting at zero).

# In[11]:


# "{0} {1}".format(first,second)

first = "apple"
second = "banana"
third = "carrot"

format_string = "List of items: {0}, {2} and {1}".format(first,second,third)

print(format_string)


# We can also use formatting expressions inside the curly brackets to alter the way the string is formatted. 
# 
# - **Example 1**: The expression `{:.2f}` formats the variable as a float number with two decimal places. The colon acts as a separator from the field name, if specified. We can also specify text alignment using the greater than operator `>`. 
# 
# - **Example 2**: The expression `{:>3.2f}` would align the text three spaces to the right and specify a float number with two decimal places.

# In[12]:


# Example 1 

two_third = 2 / 3

print("Without formatting: {}".format(two_third))
print("With formatting: {:.3f}".format(two_third))


# ### Program 13
# ---
# 
# Write a function called `is_palindrome` that takes in a string and checks if it's a palindrome. A palindrome is a string that can be read equally from left to right or right to left, ignoring capitalization and blank spaces. The function should return `True` if the passed string is a palindrome, and `False` if not.
# 
# **Note**:
# In the above example, the function should return True because "Kayak" is a palindrome string. When we read it from left to right or right to left, ignoring capitalization and blank spaces, the string remains the same.

# In[1]:


def is_palindrome(input_string):
    
    """
    Parameters:
        input_string (str): A string to be checked
        
    Returns:
        True if input_string is palindrome, 
        False otherwise.
    """
    
    actual_input_string = input_string.lower()
    str_len = len(actual_input_string)
    str_ind = str_len-1
    
    new_string = ""
    actual_reverse = ""
    
    reverse_string = actual_input_string[str_ind::-1]
    reversing1 = reverse_string.split()
    
    for letter in actual_input_string:
        
        if letter != " ":
            new_string = new_string + letter
    
    for letter in reversing1:
        actual_reverse = actual_reverse + letter
    
    if new_string == actual_reverse:
            return True
    else:
        return False


# In[2]:


# Should be True
print("Run 1")
print("Is 'Never Odd or Even' a palindrome? - ",is_palindrome("Never Odd or Even"),end="\n\n")

# Should be False
print("Run 2")
print("Is 'abc' a palindrome? - ",is_palindrome("abc"),end="\n\n")

# Should be True
print("Run 3")
print("Is 'kayak' a palindrome? - ",is_palindrome("kayak"))


# ### Program 14
# ---
# 
# Write a function called `replace_ending` that takes three parameters: `sentence`, `old`, and `new`. The function should replace the old string in the sentence with the new string, but only if the sentence ends with the old string. If there is more than one occurrence of the old string in the sentence, only the one at the end is replaced, not all of them. The function should then return the updated sentence.
# 
# **For example**
# 
# replace_ending("abcabc", "abc", "xyz") should return "abcxyz", not "xyzxyz" or "xyzabc". 
# 
# **Note** that the string comparison should be case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return "abcabc" (no changes made).

# In[3]:


def replace_ending(sentence, old, new):
    
    """
    Parameters:
        sentence (str): The input sentence
        old (str): the string to be replaced
        new (str): the string that replaces the old string
        
    Returns:
        str: the modified sentence with old string
        replaced by new string. if old is found at the
        end of the sentence. Otherwise, returns the 
        original sentence.
    """

    # Checking if the old string is at the end of the sentence 
    if sentence.endswith(old):
        
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

     
    return sentence


# In[4]:


# Should display "It's raining cats and dogs"   
print("Run 1")
print(replace_ending("It's raining cats and cats", "cats", "dogs"),end="\n\n")

# Should display "She sells seashells by the seashore"
print("Run 2")
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"),end="\n\n")

# Should display "The weather is nice in May"
print("Run 3")
print(replace_ending("The weather is nice in May", "may", "april"),end="\n\n")

# Should display "The weather is nice in April"
print("Run 4")
print(replace_ending("The weather is nice in May", "May", "April"),end="\n\n") 


# ---
