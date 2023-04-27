#!/usr/bin/env python
# coding: utf-8

# # Object Oriented Programming
# ---
# 
# **Learning Objectives**
# 
# - Demonstrate object-oriented programming using classes and objects
# - Implement classes with custom attributes and methods
# - Write docstrings to document classes and methods
# - Leverage inheritance to reduce code duplication
# - Import and use Python modules to access powerful classes and methods
# 
# ---

# In object-oriented programming, concepts are modeled as `classes` and `objects`. An idea is defined using a class, and an instance of this class is called an object. 
# 
# **Almost everything in Python is an object, including strings, lists, dictionaries, and numbers.**
# 
# When a list is created in Python, an object is generated, which is an instance of the list class that signifies the concept of a list. Classes also have attributes and methods associated with them. **Attributes** are the characteristics of the class, while **Methods** are functions that are part of the class.
# 
# 

# When using the `type` function, Python tells us which class the value or the variable belongs to. And since it is a class, it has a bunch of attributes and methods associated with it.

# In[1]:


print(type(5))
print(type('5'))


# Listing all the attributes and methods in a class can be achieved in Python by using the `dir` function.

# In[2]:


dir('')


# Some of the familiar string methods like `lower`, `split` and `isnumeric` can be seen in the output returned.

# When creating classes in Python, the `class` keyword is used, followed by the desired class name and a colon (:), in a manner similar to defining functions. The recommended way of naming a class is with a capital letter.
# 
# The class body is indented to the right. Inside the class body, we define the attributes and methods for the instances of the class.
# 
# **Example** - An Apple Class

# In[3]:


class Apple:
    
    color = ""
    flavor = ""


# New instance for the `Apple` class can be created by assigning a variable. This is done by calling the class name.
# 
# The attributes for the class instance can be set by accessing them using dot notation.
# 
# The dot notation can be used to set or retrieve object attributes, as well as call methods associated with the class.

# In[4]:


# Creating an instance
first_apple = Apple()

# Setting the 'color' attribute
first_apple.color = "red"

# Setting the 'flavor' attribute
first_apple.flavor = "sweet"


# Another instance of an Apple can be created in Python and assigned different attributes to differentiate between two different varieties of apples.

# In[5]:


second_apple = Apple()

second_apple.color = 'green'

second_apple.flavor = 'soft'


# ### Program 22
# ---
# 
# Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. The values of these attributes can be easily changed at the object level.  
# 
# The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people. 
# 
# Complete the code satisfy the behavior described in the quote. 

# #### “If you have an apple and I have an apple and we exchange these apples then
# #### you and I will still each have one apple. But if you have an idea and I have
# #### an idea and we exchange these ideas, then each of us will have two ideas.”
# #### George Bernard Shaw

# In[1]:



class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 3

martin = Person()
martin.apples = 2
martin.ideas = 2

def exchange_apples(you, me):
    
    #Here, despite G.B. Shaw's quote, our characters have started with       
    #different amounts of apples so we can better observe the results. 

    #We're going to have Martin and Johanna exchange ALL their apples with #one another.

    #Hint: how would you switch values of variables, 
    #so that "you" and "me" will exchange ALL their apples with one another?

    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    
    you_share = you.ideas
    me_share = me.ideas
        
    you.ideas += me_share
    me.ideas += you_share
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


# ### Program 23
# ---
# The City class has the following attributes: `name`, `country` (where the city is located), `elevation` (measured in meters), and `population` (approximate, according to recent statistics). 
# 
# Fill in the blanks of the `max_elevation_city` function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. 
# 
# **For example**, calling the function for a minimum population of 1 million: `max_elevation_city(1000000)` should return `Sofia, Bulgaria`. 

# In[7]:


# define a basic city class

class City:
    
    name = ""
    country = ""
    elevation = 0
    population = 0
    
    
# create a new instance of the City class and
# define each attribute

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute

city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
    
    return_city = City()
    highest_ele = 0
    
    
    # Evaluating the 1st instance to meet the requirements:
    # does city1 have at least min_population
    # and is its elevation the highest evaluated so far
    
    if city1.population >= min_population and highest_ele < city1.elevation:
        
        return_city = city1
        highest_ele = city1.elevation
        
        
    # Evaluating the 2nd instance to meet the requirements:
    # does city2 have at least min_population and 
    # is its elevation the highest evaluated so far?
    
    if city2.population >= min_population and highest_ele < city2.elevation:
        
        return_city = city2
        highest_ele = city2.elevation
        
        
    # Evaluating the 3rd instance to meet the requirements:
    # does city3 have at least min_population and
    # is its elevation the highest evaluated so far?
    
    if city3.population >= min_population and highest_ele < city3.elevation:
        
        return_city = city3
        highest_ele = city3.elevation
        
        
    # Formatting the return string
    
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""


# In[8]:


# Should print "Cusco, Peru"
print("Run 1")
print(max_elevation_city(100000),end="\n\n")

# Should print "Sofia, Bulgaria"
print("Run 2")
print(max_elevation_city(1000000),end="\n\n")


# Should print ""
print("Run 3")
print(max_elevation_city(10000000))     
    


# ### Program 24
# ---
# 
# There are two pieces of furniture: a brown wood table and a red leather couch. 
# 
# Complete the code so that the `describe_furniture` function can format a sentence that describes these pieces as follows: 
# 
# `This piece of furniture is made of {color} {material}`.

# In[9]:


class Furniture:
    color = ""
    material = ""
    

table = Furniture()
table.color = "brown"
table.material = "wood"


couch = Furniture()
couch.color = "red"
couch.material = "leather"


def describe_furniture(piece):
    return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


# Should be "This piece of furniture is made of brown wood"
print("Run 1")
print(describe_furniture(table),end="\n\n") 


# Should be "This piece of furniture is made of red leather"
print("Run 2")
print(describe_furniture(couch),end="\n\n")


# ### Classes and Methods
# ---
# 
# Calling `methods` on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, **for example**, only modifies that instance of a list, and not all lists globally. 
# 
# Methods can be defined in a class by creating functions within the class definition. These instance methods can take a parameter called `self` which represents the instance the method is being executed on. This allows to access attributes of the instance using dot notation, like `self.name`, which will access the name attribute of that specific instance of the class object. 
# 
# **Instance variables** are variables that contain different values for different instances. They are unique to each instance of a class and can be accessed and modified using object notation. 
# 
# **For example**, if there is a class `Person`, each instance of Person may have a different name, age, and address.

# Let's define a class called `Piglet` and add a method for it.

# In[3]:


class Piglet:
    
    def speak(self):
        print("oink oink")


# - The method for a class is defined with the `def` keyword, just like defining a function.
# 
# - This line is indented to the right inside the `Piglet` class, indicating that its a method of that class.
# 
# - The method is recieving a parameter called `self`, which represents the instance that the method is being executed on.

# In[4]:


hamlet = Piglet()

hamlet.speak()


# In this updated `speak()` method for the class **Piglet**, it's using the value of `self.name`, which is the attribute of the instance, to know which name to print.

# In[12]:


class Piglet:
    
    name = ""
    
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))


# In[13]:


hamlet = Piglet()
hamlet.name = "Hamlet"

hamlet.speak()


# In[14]:


petunia = Piglet()
petunia.name = "Petunia"

petunia.speak()


# Since methods are just functions that belong to a specific class, they can work as any other functions. So, they can receive more parameters and return values if needed.

# In[15]:


class Piglet():
    
    name = ""
    years = 0
    
    def speak(self):
        print("Oink! I am {}! Oink".format(self.name))
        
    def pig_years(self):
        return self.years * 18


# In[16]:


piggy = Piglet()
piggy.years = 2

print(piggy.pig_years())


# ### Constructors 
# ---
# 
# Instead of creating classes with empty or default values, the values can be set when creating the instance.
# 
# To do this, a special method called a **constructor** is used.
# 
# Below is an example of `Apple` class with a constructor method defined.

# In[17]:


class Apple:
    
    def __init__(self,color,flavor):
        
        self.color = color
        self.flavor = flavor


# When the name of the class is called, the constructor in that class is evoked. This constructor method is always named `__init__`. Special methods start and end with two underscore characters.
# 
# In the example above, the constructor method takes the self variable, which represents the instance, as well as `color` and `flavor` parameters. These parameters are then used by the constructor method to set the values for the attributes.
# 
# Now, the new instance of Apple class can be created and the attributes can be set in one go.

# In[18]:


jonagold = Apple('red', 'sweet')

print("Color of jonagold is {}".format(jonagold.color))


# When attempting to print the instance of an apple, a cryptic message is displayed.

# In[19]:


print(jonagold)


# This message indicates that the object is an instance of the `Apple` class and provides the memory location of the object in hexadecimal format. This method of printing an object is known as **default representation**.
# 
# The `__str__` special method allows us to define how an instance of an object will be printed when it's passed to the `print()` function. If an object doesn't have this special method defined, it will wind up using the default representation, which will print the position of the object in memory.
# 
# Here's the Apple class, with the `__str__` method:

# In[20]:


class Apple:
    
    def __init__(self,color,flavor):
        
        self.color = color
        self.flavor = flavor
        
    def __str__(self):
        return ("This apple is {} and its flavor is {}".format(self.color,self.flavor))


# Now, passing an Apple object to the print function returns a nice formatted string.

# In[21]:


jonagold = Apple('red','sweet')

print(jonagold)


# ### Inheritance
# ---
# 
# In Object-Oriented Programming, **Inheritance** is a mechanism that allows us to define a new class based on an existing class, inheriting all the attributes and behaviors of the parent class. Inheritance promotes the idea of code reusability, as the new class can reuse the code and attributes from the parent class, without having to redefine them.
# 
# The existing class is called the `parent class`, and the new class is called the `child class`. The child class can add or override attributes and methods of the parent class, or it can simply inherit them as they are. This helps to group together similar concepts and create a more organized class hierarchy.
# 
# 
# **For example**, let's create a custom `Fruit` class with `color` and `flavor` attributes.

# In[22]:


class Fruit:
    
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor


# Having defined a `Fruit` class with a constructor for `color` and `flavor` attributes, next we will define an `Apple` class along with a new `Grape` class, both of which will inherit properties and behaviors from the `Fruit` class.

# In[23]:


class Apple(Fruit):
    pass


class Grape(Fruit):
    pass


# In Python, parentheses is used in class declaration to mention the base class from which the defining class with inherit.
# 
# So, in this example, the code instructs both `Apple` and `Grape` class to inherit from the `Fruit` class. This means that both have the same constructor method which sets the color and flavor attributes.
# 
# Now, the instances of `Apple` and `Grape` classes can be created:

# In[24]:


first_fruit = Apple("green", "tart")
second_fruit = Grape('purple', 'sweet')

print(first_fruit.flavor)
print(second_fruit.color)


# With Inheritance, one can define common attributes and methods for all types of fruits in Object-Oriented Programming without having to repeatedly define them in each individual fruit class. It allows the grouping of similar concepts and reduces code duplication.
# 
# Additionally, one can specify unique attributes or methods that are applicable to a specific type of fruit.

# Let's look at another **example**, this time involving animals:

# In[25]:


class Animal:
    
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
        
    def speak(self):
        print("{}, I am {}! {}".format(self.sound,self.name,self.sound))
        
        
class Dog(Animal):
    pass


class Cat(Animal):
    pass


# We defined a parent class `Animal`, with two animal subclasses inheriting from that class: `Cat` and `Dog`.
# 
# The parent `Animal` class has a constructor class takes the name and sound the animal makes, assigning it to the instance when it's created. 
# 
# There is also the `speak()` method, which will print the name of the animal along with the sound it makes.
# 
# The `Cat` and `Dog` classes are defined, which inherit from the `Animal` class. Now, we create the instance and let the animals speak.

# In[26]:


doggo = Dog('Cookie','ruff ruff')
catto = Cat('Jeff', 'meow')

catto.speak()
doggo.speak()


# Upon calling the `speak()` method on each instance, the formatted string is printed, which includes the sound of the animal type, along with the name assigned with the instance.

# ### Object Composition
# ---
# 
# There can be situations during writing code where two different classes are related, but there is no inheritance going on. This is referred to as **composition** - where one class makes use of code contained in another class.
# 
# For example, imagine we have a `Package` class which represents a software package. It contains attributes about the software package, like `name`, `version`, and `size`. We also have a **Repository** class which represents all the packages for installation.
# 
# While there is no inheritance relationship between two classes, they are related. The `Repository` class will contain a dictionary or list of Packages that are contained in the repository.

# In[27]:


class Repository:
    
    def __init__(self):
        
        self.packages = {}
        
    def add_package(self,package):
        
            self.packages[package.name] = package.size
            
    def total_size(self):
        
        result = 0
        
        for package in self.packages.values():
                result += package
                
        return result
    
    def __str__(self):
        return "repo dict: {}".format(self.packages)


# In[28]:


class Package:
    
    def __init__(self,name,version,size):
        
        self.name = name
        self.version = version
        self.size = size
        
    def __str__(self):
        return "Name: {} | Version: {} | Size: {}".format(self.name,self.version,self.size)


# In the **constructor method**, we initialize the packages dictionary, which will contain the package objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every instance of the Repository class has its own dictionary.
# 
# We then define the `add_package` method, which takes a Package object as a parameter, and then adds it to our dictionary, using the package name attribute as the key.
# 
# Finally, we define a `total_size` method which computes the total size of all packages contained in our repository. This method iterates through the values in our repository dictionary and adds together the size attributes from each package object contained in the dictionary, returning the total at the end. 
# 
# In this example, we’re making use of Package attributes within our Repository class. We’re also calling the `values()` method on our packages dictionary instance. Composition allows us to use objects as attributes, as well as access all their attributes and methods.

# In[29]:


package1 = Package('Matlab2023','7.4',789)
package2 = Package('Spotify', '3.0.1', 340)
package3 = Package('VS Code', '7.1.1', 584)


# In[30]:


print(package1)


# In[31]:


# Creating an instance for Repository class
repo1 = Repository()


# In[32]:


# Using the 'add_package()' method to add packages
# to the instance of Repository

repo1.add_package(package1)
repo1.add_package(package2)
repo1.add_package(package3)

print(repo1)


# In[33]:


print("Total size for repository: {} MB".format(repo1.total_size()))


# ---
