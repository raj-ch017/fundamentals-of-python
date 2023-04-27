#!/usr/bin/env python
# coding: utf-8

# # Variables, Functions and Conditionals
# ---
# 
# **Learning Objectives**
# 
# - Differentiate and convert between different data types utilizing variables
# - Define and call functions utilizing parameters and return data
# - Refactor code and write comments to reduce complexity and enhance code readability and code reuse
# - Compare values using equality operators and logical operators
# - Build complex branching scripts utilizing `if`, `else` and `elif` statements
# 
# ---

# ### Variables and Data Types
# 
# Variables can store data of different types, like strings and integers.
# 
# In Python, text in between quotes -- either single or double quotes -- is a string data type.
# 
# An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part. 
# 
# **For example**, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats. 
# 
# A `TypeError` may be encountered when attempting to mix incompatible data types. The `type()` function can be used to check the data type of an object.
# 
# 
# The four common data types are:
# 
# - **int**: A number without floating point.
# 
# - **float**: A number with floating point precision.
# 
# - **bool**: Data type representing truth value of either True or False.
# 
# - **str**: Sequence of characters.

# In[1]:


int_var = 7

float_var = 7.0

str_var = "Today is Wednesday"

bool_var = True

print("Data type of",int_var," is",type(int_var),end="\n\n")

print("Data type of",float_var," is",type(float_var),end="\n\n")

print("Data type of",str_var," is",type(str_var),end="\n\n")

print("Data type of",bool_var," is",type(bool_var),end="\n\n")


# **Variables** are names that are given to certain values in our programs. These values can be of any data type; numbers, strings or even the results of operations. 
# 
# When creating variables in code, a chunk of the computer's memory is reserved to store the value. This allows the computer to access the variable later and read or modify the value as needed. 
# 
# Values are stored in the variables using the **assignment** statement, which associates the name to the left of `=` symbol with the value to the right of the `=` symbol.
# 
# An **expression** is a combination of numbers, symbols or other variables that produce a result when evaluated.

# ### Variable Naming Restrictions
# 
# - Keywords and Function names not allowed
# 
# - Don't use spaces
# 
# - Must start with a letter or an underscore (_)
# 
# - Can only contain letters, numbers and underscore with no other characters
# 
# **Example 1**: `i_am_a_variable` is a valid name.
# 
# **Example 2**: `1_is_a_variable` is an invalid name because it starts with a number.
# 
# **Example 3**: `apple&orange` is also invalid since it uses a special character.

# ### Program 2
# ---
# 
# The code provided assigns the value of 13 to the variable `length` and the value of 3 to the variable `width`. It then calculates the product of length and width and stores it in the variable `area`. Finally, it outputs the value of area to the console using the `print()` function.
# 
# In this case, the variables `length` and `width` represent the length and width of a rectangle, and the calculation `length * width` gives us the area of the rectangle.

# In[2]:


length = 13
width = 3
area = length * width

print(area)


# ### Implicit vs Explicit Conversion
# 
# Some data types can be mixed and matched due to implicit conversion. **Implicit conversion** is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.
# 
# In contrast, **explicit conversion** refers to the manual conversion from one data type to another by calling the appropriate function for the desired data type.
# 
# 
# **For example**, a variable with integer value can be converted to string using `str()`.

# In[3]:


int_variable = 8

print("Type of int_variable is",type(int_variable))

str_variable = str(int_variable)

print("Type of str_variable is",type(str_variable))


# ### Program 3
# ---
# 
# In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "**Each person needs to pay:** " followed by the resulting number.

# In[3]:


bill = 47.28
tip = (0.15*bill)
total = bill + tip
share = total/2 

print("Each person needs to pay: $" + str(round(share,2)))


# ### Functions
# ---
# 
# A **function** is a block of code that performs a specific task and can be reused multiple times in a program. Functions allow us to organize our code and make it more modular, which makes it easier to read, debug, and maintain.
# 
# Functions in Python are defined using the `def` keyword followed by the function name and a set of parentheses that can include parameters (values passed to the function) and ends with a colon(:). The function code is then indented below the `def` statement.
# 
# A function can have no parameters, or it can have multiple parameters. Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters.
# 
# **Example**: The function `add_number` takes two parameters, `x` and `y`, adds them together, and prints the result with a meaningful message.

# In[5]:


def add_number(x,y):
    """ 
    Prints the sum of two numbers
    
    Parameters:
        x (int): First number
        y (int): Second number
        
    Returns:
        None
    """
    print("The sum of",x,"and",y,"equals",x+y)
    
add_number(77,33)


# ### Program 4
# ---
# 
# The function `book_store` takes one argument, `copies`, representing the number of copies of a book to be purchased. The function calculates the total cost of purchasing these copies including a discount on the marked price, delivery charges, and the selling price of the book.
# 
# - First, the function sets the `cover_price` of the book to 24.95. It then calculates the discount on this price, which is equal to 40% of the cover price, and stores it in the `discount` variable. The selling price of the book is then calculated by subtracting the discount from the cover price and storing it in the `sell_price` variable.
# 
# - Next, the function calculates the delivery charges based on the number of extra copies bought (i.e. the number of copies above the first one). The delivery charge for the first copy is 3, and for each additional copy, it is 0.75. The number of additional copies is calculated by subtracting 1 from the total number of copies, since the first copy has no additional delivery charge. The total delivery charges are then stored in the `deli_charges` variable.
# 
# - Finally, the function calculates the total cost of purchasing the given number of copies by adding the selling price and the delivery charges. The total cost is then printed to the console using the print function.
# 
# - Note that the function does not return any value, it just prints the total cost to the console.

# In[6]:


def book_store(copies):
    """ 
    Calculate the total cost of purchasing multiple copies of
    a book, including delivery charges.
    
    Parameters:
        copies (int): the number of copies being purchased
        
    Returns:
        None    
    """
    
    cover_price = 24.95 
    discount = 0.40 * cover_price   #calculates the discount based on the marked price
    sell_price = cover_price - discount #calculates the selling price, depending on the discount
    additional_copies = copies - 1  #the number of extra copies bought
    deli_charges = 3 + (additional_copies*0.75) #delivery charge calculation
    total = sell_price + deli_charges   #calculates the total
    
    print(total)
    
book_store(100)    


# ### Returning Values using Functions
# 
# The concept of return values in Python refers to the ability of a function to modify the passed data and return the result to the calling statement. The `return` keyword is used within a function to transfer data back to the calling statement. After calling the function, the returned value can be saved in a variable. This allows for greater versatility and power in functions, as they can be used repeatedly with different data.
# 
# 
# Functions can even produce multiple values, but it's crucial to store all the returned values in respective variables. Additionally, a function may return nothing, in which case, it will merely terminate.

# ### Program 5
# ---
# 
# This function `convert_distance` converts miles to kilometers (km).
# 
# - Complete the function to return the result of the conversion
# 
# - Call the function to convert the trip distance from miles to kilometers
# 
# - Calculate the round-trip in kilometers by doubling the result, and to print the result

# In[7]:




def convert_distance(miles):
    """
    Converts  a distance given in miles to kilometers.
    
    Parameter:
        miles (float): A distance in miles
        
    Returns:
        float: The distance in kilometers
    """
    return miles * 1.6  

my_trip_miles = 55



my_trip_km = convert_distance(55)

print("The distance in kilometers is " + str(my_trip_km))

total_km = 2 * my_trip_km
print("The round-trip distance in kilometers is " + str(total_km))


# ### Program 6
# ---
# 
# This function `order_numbers` compares two numbers and returns them in increasing order.
# 
# - Write the function so the print statement displays the result of the function call in order.

# In[8]:


def order_numbers(number1, number2):
    """ 
    Returns two numbers in ascending order
    
    Parameters:
        number1 (int): A number
        number2 (int): A number
        
    Returns:
        Two numbers in ascending order
    """
    if number2 > number1:
        return number1, number2

    else:
        return number2, number1

    

smaller, bigger = order_numbers(888, 99)
print(smaller, bigger)


# ### Conditionals - Making Complex Decisions
# ---
# 
# In Python, the comparison operators are used to compare values, and upon doing so, Python returns a **boolean** result, i.e., `True` or `False`.
# 
# - For verifying if two values are identical, we can use the **equality operator**: `==`.
# 
# - To confirm if two values are not the same, we can employ the **not equals operator**: `!=`. 
# 
# - Additionally, we can compare values using **greater than** (>) or **lesser than** (<) operators. 
# 
# Nonetheless, if we try to compare incompatible data types, such as an integer with a string, Python raises a `TypeError`.
# 
# By combining statements with **logical operators** and **comparison operators**, we can create complex comparisons. The three logical operators available in Python are `and`, `or`, and `not`. 
# 
# - When the `and` operator is used, both sides of the evaluated statement must be true for the complete statement to be true. 
# 
# - On the other hand, when the `or` operator is used, the complete statement becomes true if any of the two sides in the comparison is true. 
# 
# - Finally, the `not` operator reverses the value of the statement following it. So, if a statement evaluates to True, and we use the not operator with it, the statement becomes False.

# In[9]:


# Example 1 - Greater Than Operator

conditional1 = 42 > 20

print("Is 42 greater than 20?",conditional1,end="\n\n")


# Example 2 - Equality Operator

conditional2 = (25 == 15)

print("Is 25 equal to 15?",conditional2,end="\n\n")


# Example 3 - Not Equals Operator

conditional3 = (100 != 200)

print("100 does not equal 200?",conditional3,end="\n\n")


# Example 4 - `and` operator

conditional4 = (16 % 2 == 0) and (19 % 2 == 0)

print("16 is even and 19 is even?",conditional4,end="\n\n")


# Example 5 - `or` operator

conditional5 = (16 % 2 == 0) or (19 % 2 == 0)

print("16 is even or 19 is even?",conditional5,end="\n\n")


# ### Branching 
# 
# - **If Statement**
# 
# In Python, **branching** is used to modify the execution sequence of code based on the values of variables. 
# 
# An `if` statement is used to compare values. We start the if statement with the keyword `if`, followed by the comparison. A colon is used to end the line. The code block under the `if` statement is indented to the right. 
# 
# If the comparison is evaluated as `True`, the code within the body is executed. However, if the comparison evaluates to `False`, the code block is skipped and not executed.

# In[10]:


def check_username(username):
    """ 
    Checks if a given username is valid or not
    
    Parameters:
        username (str): The username to be checked
        
    Returns:
        None: Prints a message to the console if given
        username is invalid
    """
    
    if len(username) <= 3:
        print(username,"is invalid username. Minimum length should be 4.",end="\n\n")
        
        
# Should print 'invalid'
print("Run 1")
check_username('rik')

# Should print nothing
print("Run 2")
check_username('rick')


# - **If Else Statement**
# 
# Suppose we want our code to perform an alternative action if the evaluation of `if` is `False`. One way is to use the `else` statement. 
# 
# The else statement follows an if block and is made up of the keyword `else` followed by a colon. The body of the `else` statement is indented to the right and will be executed if the preceding `if` statement is not executed.

# In[11]:


def check_username(username):
    """
    Checks whether the given username is valid
    or not
    
    Parameters:
        username (str): The username to be checked
        
    Returns:
        None
    """
    
    if len(username) <= 3:
        print(username,"is invalid username. Minimum length should be 4.",end="\n\n")
    
    else:
        print(username,"is valid username.",end="\n\n")

# Should print 'invalid'
print("Run 1")
check_username('rik')

# Should print 'valid'
print("Run 2")
check_username('rick')


# - **If-Elif-Else Statement**
# 
# By using `if` and `else` blocks, we can control the flow of our code based on the evaluation of a single statement. To perform more complex branching, we can use the `elif` statement. 
# 
# It is similar to `if` statements and starts with the `elif` keyword, followed by a comparison to be evaluated. Then, a colon is placed, and the code block is written on the next line, indented to the right. However, an `elif` statement must come after an `if` statement and will only be evaluated if the `if` statement was false.

# In[12]:


def check_username(username):
    """ 
    Checks whether the given username is valid or not.
    
    Parameters:
        username (str): The username to be checked
        
    Returns:
        None
    """
    
    if len(username) <= 3:
        print(username,"is invalid username. Minimum length should be 4.",end="\n\n")
    
    elif len(username) > 15:
        print(username,"is invalid username. Maximum length is 15.",end="\n\n")
        
    else:
        print(username,"is valid username.",end="\n\n")
        
# Should print 'invalid'
print("Run 1")
check_username('rik')

# Should print 'valid'
print("Run 2")
check_username('rick')

# Should print 'invalid'
print("Run 3")
check_username('pickle_rick_tiny')


# ### Exercises
# ---
# 
# #### Exercise 1
# 
# The function `format_name` that takes two parameters, `first_name` and `last_name`.
# 
# The function checks if both `first_name` and `last_name` are not empty strings by using the `len()` function to check their length. If both are non-empty, the function creates a string name by concatenating `last_name`, a comma, and `first_name` with the format "`Name: last_name, first_name`", and returns it.
# 
# If `first_name` is an empty string but `last_name` is not, the function creates a string name with just the last name and returns it.
# 
# If `last_name` is an empty string but `first_name` is not, the function creates a string name with just the first name and returns it.
# 
# If both `first_name` and `last_name` are empty strings, the function returns an empty string.

# In[4]:


def format_name(first_name,last_name):
    """ 
    Parameters:
        first_name(str): The first name of the person
        last_name (str): The last name of the person
        
    Returns:
        str: A formatted string in the format 
        "Name: last_name, first_name" or "Name: last_name" or "Name: first_name"
        or an empty string.
    """
    
    if len(first_name) > 0 and len(last_name) > 0:
        name = "Name: " + last_name + ", " + first_name
        return name
    
    elif len(first_name)==0 and len(last_name) > 0:
        name = "Name: " + last_name
        return name
    
    elif len(first_name) > 0 and len(last_name)==0:
        name = "Name: " + first_name
        return name
    
    else:
        return ""


# In[5]:


# Should return the string "Name: Hemingway, Ernest"
print("Run 1")
print(format_name("Ernest", "Hemingway"),end="\n\n")

# Should return the string "Name: Madonna"
print("Run 2")
print(format_name("", "Madonna"),end="\n\n")

# Should return the string "Name: Voltaire"
print("Run 3")
print(format_name("Voltaire", ""),end="\n\n")

# Should return an empty string
print("Run 4")
print(format_name("", ""),end="\n\n")


# 
# #### Exercise 2
# 
# The `fractional_part` function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number.
# 
# **Note**: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

# In[6]:


def fractional_part(numerator,denominator):
    """
    Parameters:
        numerator (float or int): The numerator of the division
        denominator (float or int): The denominator of the division
        
    Returns:
        The fractional part of the division (float) if the
        denominator is not zero, otherwise 0
    """
    
    if denominator == 0:
        return 0
    
    mod_r = numerator % denominator
    frac_r = mod_r / denominator
    
    if frac_r == 0:
        return int(frac_r)
    
    return frac_r


# In[8]:


# Should be 0
print("Run 1")
print(fractional_part(5, 5),end="\n\n")

# Should be 0.25
print("Run 2")
print(fractional_part(5, 4),end="\n\n")

# Should be 0.66...
print("Run 3")
print(fractional_part(5, 3),end="\n\n")

# Should be 0.5
print("Run 4")
print(fractional_part(5, 2),end="\n\n")

# Should be 0
print("Run 5")
print(fractional_part(5, 0),end="\n\n")

# Should be 0
print("Run 6")
print(fractional_part(0, 5),end="\n\n") 


# #### Exercise 3
# 
# Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". 
# 
# Complete the function so that it returns the proper grade.

# In[9]:


def exam_grade(score):
    """
    Determines the exam grade based on the
    provided score
    
    Parameters:
        score (float): The score obtained in the exam
        
    Returns:
        str: A string indicating the grade
    """
    
    if score > 95:
        grade = "Top Score"

    elif score >= 60 and score <= 95:
        grade = "Pass"

    else:
        grade = "Fail"

    return grade


# In[10]:


# Should be Pass
print("Run 1")
print("Score of 65:",exam_grade(65),end="\n\n")

# Should be Fail
print("Run 2")
print("Score of 55:",exam_grade(55),end="\n\n")

# Should be Pass
print("Run 3")
print("Score of 60:",exam_grade(60),end="\n\n")

# Should be Pass
print("Run 4")
print("Score of 95:",exam_grade(95),end="\n\n")

# Should be Top Score
print("Run 5")
print("Score of 100:",exam_grade(100),end="\n\n")

# Should be Fail
print("Run 6")
print("Score of 0:", exam_grade(0),end="\n\n") 


# #### Exercise 4
# 
# The `longest_word` function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length).

# In[11]:


def longest_word(word1, word2, word3):
    """
    Returns the longest word among the given three words
    
    Parameters:
        word1 (str): String representing the first word
        word2 (str): String representing the second word
        word3 (str): String representing the third word
        
    Returns:
        The longest word. In case of a tie, 
        the first longest encountered is returned.
    """
    
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1

    elif len(word1) < len(word2) and len(word2) >= len(word3):
        word = word2

    else:
        word = word3

    return(word)


# In[12]:


# Should return 'chair'
print("Run 1")
print(longest_word("chair", "couch", "table"),end="\n\n")

# Should return 'beyond'
print("Run 2")
print(longest_word("bed", "bath", "beyond"),end="\n\n")

# Should return 'notebook'
print("Run 3")
print(longest_word("laptop", "notebook", "desktop"),end="\n\n")


# ---
