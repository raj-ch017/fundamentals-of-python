#!/usr/bin/env python
# coding: utf-8

# # Loop - Over and Over
# ---
# 
# **Learning Objectives**
# 
# - Use the `range()` function to control `for loops`
# - Utilize `for loops` to iterate over a block of code
# - Identify and fix infinite loops when using `while loops`
# - Implement `while loops` to continuously execute code while a condition is true
# - Use nested `while` and `for` loops with `if statements`
# - Identify and correct common errors when using loops
# 
# ---

# ### While Loop
# 
# A **while loop** executes code repeatedly based on the value of a condition. It starts with the `while` keyword, followed by a comparison that is to be evaluated, and ends with a colon. The code block to be executed is indented to the right on the next line. 
# 
# Like an **if statement**, the body of code is executed only if the comparison evaluates to `True`. However, the key feature of a while loop is that the code block keeps executing as long as the evaluation statement remains True. Once the statement is no longer True, the loop terminates, and the next line of code is executed.

# ### Program 7
# ---
# 
# - The `squares` function takes a number `n` as input and returns the square of that number.
# 
# - The `sum_squares` function takes a number `x` as input. It initializes a variable `input` to be equal to `x` and initializes two more variables `sum` and `num` to 0.
# 
# - The function then enters a while loop that continues until `num` is less than `input`. 
# 
# - In each iteration of the loop, the function calls the `squares` function with `num` as input and adds the result to the `sum` variable. It also prints the current value of `num`. Finally, it increments `num` by 1.
# 
# - Once the loop has finished, the function returns the final value of `sum`, which is the sum of squares from 0 to (x-1).
# 

# In[1]:


def squares(n):
    """
    Parameters:
        n (int): Input number, the base
        
    Returns:
        n**2 (int): Square of the base
    """
    return n**2


def sum_squares(x):
    """
    Parameters:
        x (int): The upper limit (exclusive) of the range of numbers
        
    Returns:
        int: The sum of squares from 0 to (x-1)
    """
    
    input = x
    sum = 0
    num = 0
    
    while num < input:
    
        a = squares(num)
        sum += a
        print("Loop run number: " + str(num))
        num += 1
    
    return sum

sum_squares(5)


# It's crucial to keep in mind that the while loop's condition must result in either `True` or `False`. Achieving a certain result in programming can be done through the use of comparison operators or the invocation of other functions.
# 
# Furthermore, the condition for while loops can become more intricate by utilizing logical operators such as `and`, `or`, and `not`.

# ### Breaking the Loop: Handling and Avoiding Errors
# 
# - One should watch out for a common mistake in `while` loops: **forgetting to initialize variables**. If a variable is used without being initialized, a `NameError` will occur. The Python interpreter will catch the mistake and inform the user that an undefined variable is being used. The solution is simple: initialize the variable by assigning it a value before it is used.
# 
# - Another common mistake to watch out for, which can be trickier to spot, is forgetting to initialize variables with the correct value. If a variable is used earlier in the code and then reused later in a loop without first setting it to the desired value, the code may produce unexpected results. **It is important to always initialize variables before using them**.
# 
# - **Infinite Loop**: An infinite loop occurs when the code block in the loop continues to execute and never stops. This can occur when the condition being evaluated in a while loop doesn't change. One should pay close attention to their variables and consider unexpected values.

# ### Program 8
# ---
# 
# The function `print_prime_factors` takes a single argument called `number`. The function finds all prime factors of the number and prints them in order. 
# 
# It starts with the first prime factor which is 2, and continues to check each consecutive factor to see if it is a divisor of number. If it is, then it prints the factor and divides the number by that factor. If it's not a divisor, it increments the factor by one and checks the next number. This process is repeated until the factor is greater than the number. Finally, the function returns a string "Done". 
# 
# **An example** usage of the function is shown at the bottom, where it's called with argument 100 and prints the prime factors 2, 2, 5, and 5.

# In[1]:


def print_prime_factors(number):
    """
    Parameters:
        number (int): A positive integer for which to
        find the prime factors
        
    Returns:
        str: A message indicating the function has finished
        execution
    """
    
    factor = 2
    
    while factor <= number:
        
        if number % factor == 0:
            
            print(factor)
            
            number = number / factor
            
        else:
                        
            factor += 1
            
    return "Done"


# In[2]:


# Should print 2, 2, 5 and 5    
print("Run 1")
print_prime_factors(100)
print()

# Should print 2, 2, 3, 3, 3 and 5
print("Run 2")
print_prime_factors(540)


# ### Program 9
# ---
# 
# The function `is_power_of_two` takes a single argument `in_num`. The function checks if `in_num` is a power of two by continuously dividing it by 2 as long as the result is an even number. 
# 
# If the final result is 1, then the original number was a power of two, and the function returns `True`. If the final result is not 1, then the original number was not a power of two, and the function returns `False`. If the initial value of `in_num` is 0, the function returns `False` without executing the while loop.

# In[3]:


def is_power_of_two(in_num):
    """ 
    Parameters:
        in_num (int): The number to be checked
        
    Returns:
        bool: True if in_num is a power of two,
              False otherwise   
    """
    
    # Check if the number can be divided by two without a remainder
    
    while (in_num != 0) and (in_num % 2 == 0):
        in_num = in_num / 2
        
    if in_num == 1:
        return True
    
    return False


# In[4]:


# Should be False
print("Run 1")
print(is_power_of_two(0),end="\n\n")

# Should be True
print("Run 2")
print(is_power_of_two(1),end="\n\n") 

# Should be True
print("Run 3")
print(is_power_of_two(8),end="\n\n")

# Should be False
print("Run 4")
print(is_power_of_two(9),end="\n\n") 


# ### Program 10
# ---
# 
# The function `sum_divisors` takes a single integer argument `input_num`. The function computes the sum of all divisors of `input_num`, excluding `input_num` itself. 
# 
# It starts by initializing a variable `sum` to 0 and a variable `div` to 1. Then, it enters a while loop that continues as long as `div` is less than `input_num`. Inside the loop, the function checks whether `input_num` is divisible by `div`. If it is, then the value of `div` is added to the `sum` variable, and `div` is incremented by 1. Otherwise, `div` is simply incremented by 1. Finally, the function returns the value of `sum`.

# In[5]:


def sum_divisors(input_num):
    """ 
    Parameters:
        input_num (int): A positive integer
        
    Returns:
        An integer representing the sum of all
        positive divisors of the input number
    """
    
    sum = 0
    div = 1
    
    while div < input_num:
        
        if (input_num % div == 0):
            
            sum += div
            div += 1
            
        else:
            
            div += 1
            
    return sum


# In[6]:


# Should return 0
print("Run 1")
print(sum_divisors(0),end="\n\n")

# Should sum of 1 = 1
print("Run 2")
print(sum_divisors(3),end="\n\n") 

# Should sum of 1+2+3+4+6+9+12+18 = 55
print("Run 3")
print(sum_divisors(36),end="\n\n") 

# Should be sum of 2+3+6+17+34+51 = 114
print("Run 4")
print(sum_divisors(102),end="\n\n") 


# ### Program 11
# ---
# 
# `multiplication_table` takes a single argument `input_number`. It uses a while loop to print out a multiplication table for number up to 5 times. The loop calculates the result of multiplying number by multiplier and prints it out in a formatted string. 
# 
# The loop also checks if the result is greater than 25, and if it is, it breaks out of the loop.

# In[7]:


def multiplication_table(input_number):
    """ 
    Parameters:
        input_number (int): An integer to generate
        the multiplication table for.
        
    Returns:
        None
    """
    
    # Initialize the starting point of the multiplication table
    
    multiplier = 1
    
    # Looping up to 5
    
    while multiplier <= 5:
        
        result = input_number * multiplier
        
        # Condition to exit out of the loop
        
        if result >= 25:
            break
            
        print(str(input_number) + " x " + str(multiplier) + " = " + str(result))
        
        # increment the variable for the loop
        
        multiplier += 1
        
    print()


# In[8]:



# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
print("Run 1")
multiplication_table(3)

# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
print("Run 2")
multiplication_table(5) 

# Should print: 8x1=8 8x2=16 8x3=24        
print("Run 3")
multiplication_table(8)


# ---
# 
# ### For Loop
# 
# The `for loop` starts with the keyword `for` followed by a colon, similar to `if statements` and `while loops`. The code block following the for loop is executed for each element in the sequence defined by the `range()` function or any other iterable object. 
# 
# The loop variable, such as `x` in the **example below**, is assigned to each element in the sequence in turn. The `range()` function generates a sequence of numbers from 0 to n-1, where `n` is the argument passed to the function.
# 
# `For loops` are useful when you want to perform a repetitive task for each element in a sequence, such as iterating over a list of strings or a file. If there is a need to repeat an action until a specific condition is met, then a `while loop` is more appropriate.

# In[6]:


for x in range(5):
    
    print(x)


# #### Range Function
# 
# The `range()` function can take up to three parameters:  `range(start, stop, step)` 
# 
# - **Start**: 
# The first item in the range() function parameters is the starting position of the range. The default is the first index position, which points to the numeric value 0. This value is included in the range. 
# 
# 
# - **Stop**:
# The second item in the range() function parameters is the ending position of the range. There is no default index position, so this index number must be given to the range() parameters. For example, the line `for n in range(4)` will loop 4 times with the n variable starting at 0 and looping 4 index positions: 0, 1, 2, 3. As you can see, range(4) (meaning index position 4) ends at the numeric value 3. In Python, this structure may be phrased as **the end-of-range value is excluded from the range.** In order to include the value 4 in  range(4), the syntax can be written as range(4+1) or range(5). Both of these ranges will produce the numeric values 0, 1, 2, 3, 4. 
# 
# 
# - **Step**:
# The third item in the range() function parameters is the incremental step value. The default increment is +1. The default value can be overridden with any valid increment. However, note that the loop will still end at the end-of-range index position, regardless of the incremental value. For example, if you have a loop with the range: `for n in range(1, 5, 6)`, the range will only produce the numeric value 1. This is because the incremental value of 6 exceeded the ending point of the range.
# 
# 
# Here are some **examples** of `range()` in code:
# 

# **Example 1**
# 
# In this code, a range from 0 to 10 is used to iterate through the values of the variable `n`. The loop increments by 2 on each iteration, and the `print()` function is used to display the current value of `n` as it counts from 0 to 10 (excluding the end-of-range index 11). This is a way to generate and print a list of even numbers in Python.

# In[7]:


for n in range(0,11,2):
    print(n)


# **Example 2**
# 
# This loop iterates on the value of the `number` variable in a range of 2 to 7+1 (the value of the end-of-range index 7 is excluded, so +1 has been added to the parameter to include the numeric value 7 in the range). The incremental value for the loop is the default of +1.
# 
# The `print()` function will output the resulting value of `number` multiplied by 3.

# In[8]:


for number in range(2,7+1):
    print(number * 3)


# **Example 3**
# 
# This code uses a `for loop` to iterate through a range of numbers, with the variable `x` taking on each value in turn. The range starts at 2 and goes down to -1 (excluding the end-of-range index -2) in decrements of -1. The `print()` function displays the current value of `x` during each iteration of the loop, as it counts down from 2 to -1.

# In[9]:


for i in range(2,-2,-1):
    print(i)


# ### Pitfalls Using For Loops:
# 
# - The upper limit of `range()` is not included in the sequence produced.
# - Iterating over non-sequences.

# ### Program 12
# ---
# 
# Complete the `factorial` function so that it returns the factorial of the input integer `num`. Once the function is complete, print the first 10 factorials (from 0 to 9) along with their corresponding numbers. 
# 
# It's **important** to remember that the factorial of a number is calculated as the product of that number and all positive integers before it.
# 
# **For instance**, the factorial of 5 (5!) is equal to 1* 2 * 3 * 4 * 5 = 120, and the factorial of 0 (0!) is 1.

# In[10]:


def factorial(n):
    """
    Calculates the factorial of a given integer.

    Parameters:
        n (int): The integer to calculate the factorial of.

    Returns:
        result (int): The factorial of the given integer.
    """
    
    result = 1
    in1= n + 1
    
    if n==0:
        return result
    
    for x in range(1,in1):
        result = result * x
    
    return result


# In[11]:


for j in range(10):
    
    output = factorial(j)
    print("Factorial of",j," = ",output)


# ### Exercises
# ---
# 
# **Exercise 1**
# 
# Implement a function called `digits(n)` that determines the number of digits in a given integer `n`.

# In[9]:


def digits(n):
    """
    Computes the number of digits in a non-negative integer.
    
    Parameters:
        n (int): The integer to count the digits of.
    
    Returns:
        int: The number of digits in n.
    """
    count = 0
    
    if n <= 9:
        count = 1
    
    if n > 9:
    
        while (n > 0):
         n = n // 10
         count = count + 1
    
    return count


# In[10]:


# Should return 2
print("Run 1")
print(digits(25),end="\n\n")

# Should return 3
print("Run 2")
print(digits(144),end="\n\n")


# **Exercise 2**
# 
# Create a function called `counter` that takes in two parameters, `start` and `stop`. The function should count down from `start` to `stop` if `start` is greater than `stop`, and count up from `start` to `stop` otherwise.

# In[13]:


def counter(start,stop):
    """
    Parameters:
        start (int): The starting number for the sequence
        stop (int): The ending number for the sequence
        
    Returns:
        A string that describes a sequence of numbers based
        on the input arguments.
    """

    if start > stop:
        return_string = "Counting down: "
        for j in range(start,stop-1,-1):
            
            if j == stop:
                return_string = return_string + str(j)
            
            else:
                return_string = return_string + str(j) + ","
            
            j += 1
    
    elif stop > start:
        
        return_string = "Counting up: "
        
        for j in range(start,stop+1):
            
            if j == stop:
                return_string = return_string + str(j)
            
            else:
                return_string = return_string + str(j) + ","
            
            j += 1
    
    else:
        return_string = "Counting up: "
        return_string = return_string + str(start)
    
    return return_string


# In[14]:


# Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print("Run 1")
print(counter(1, 10),end="\n\n")

# Should be "Counting down: 2,1"
print("Run 2")
print(counter(2, 1),end="\n\n") 

# Should be "Counting up: 5"
print("Run 3")
print(counter(5, 5),end="\n\n")


# **Exercise 3**
# 
# The `even_numbers` function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function. 
# 
# **For example**, even_numbers(6) returns “2 4 6”.

# In[11]:


def even_numbers(maximum):
    """
    Parameters:
        maximum (int): The maximum number to consider
        
    Returns:
        str: A space-separated string of even numbers
        from 2 to 'maximum'
    """
    
    return_string = ""

    for x in range(2,maximum+1):

        if x % 2 == 0:
            return_string += str(x) + " "

    return return_string.strip()
 


# In[12]:


# Should be 2 4 6
print("Run 1")
print(even_numbers(6),end="\n\n")

# Should be 2 4 6 8 10
print("Run 2")
print(even_numbers(10),end="\n\n")

# No numbers displayed
print("Run 3")
print(even_numbers(1),end="\n\n")

# Should be 2
print("Run 4")
print(even_numbers(3),end="\n\n")

# No numbers displayed
print("Run 5")
print(even_numbers(0),end="\n\n") 


# ---
