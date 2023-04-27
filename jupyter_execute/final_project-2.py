#!/usr/bin/env python
# coding: utf-8

# # Final Project - Word Cloud
# ---

# ### 1. Introduction
# 
# In this project, we will create a **word cloud** from a given text by processing the text, removing punctuation, ignoring cases, counting the frequencies, and ignoring uninteresting or irrelevant words. The project will generate a dictionary containing the word frequencies, which the word cloud module will use to generate an image.
# 
# Real-world data processing and visualization applications, such as analyzing customer reviews, news articles, or social media posts, inspired the project task. Completing this project provides valuable experience in processing textual data and generating visual representations of the processed data.
# 
# Beginners can use the project and provide the input text by copying and pasting from a website or using a file containing the text. The project includes both pre-written code and code that had to be completed by the learner, allowing them to understand and modify the code to suit their needs.
# 
# Overall, this project provides a hands-on experience of working with textual data and generating visualizations, which can be valuable in various fields, including data analysis, natural language processing, and data journalism.

# ### 2. Provided Materials
# 
# To begin, you will need to install and import the necessary packages and libraries for the word cloud script and the uploader widget. Running code cells will perform all the necessary installations and imports, but it may take some time to complete. Once you see the final line of output, the code execution is complete, and you can proceed with the instructions for the project.

# In[1]:


# Here are all the installations and imports needed to generate the word cloud

get_ipython().run_line_magic('pip', 'install wordcloud')
get_ipython().run_line_magic('pip', 'install fileupload')
get_ipython().run_line_magic('pip', 'install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')


# In[2]:


import wordcloud
import numpy as np 
from matplotlib import pyplot as plt 
from IPython.display import display 
import fileupload
import io 
import sys


# To upload the text file, run the following cell that contains all the code for a custom uploader widget.
# 
# Once the cell is run, a `Browse` buttion should appear below it. Clicking this button will open a nagivation window that allows locating the saved text file.

# In[3]:


def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)


# ### 3. Writing the function
# 
# The function takes a `sentence` as input, cleans it by removing punctuations and uninteresting words, and then counts the frequency of each word. The frequency count is stored in a dictionary, which is then used to generate a word cloud image. The output is a Numpy array representing the image.
# 
# The function iterates through the words in the text, removes punctuation, ignores word cases (lower-case and upper-case are treated similarly) and words that do not contain all alphabets, and counts the frequency of each remaining word. 
# 
# Additionally, the function ignores boring words such as "and" or "the".

# In[4]:


def generate_from_frequencies(sentence):
    """ 
    Process the input sentence to generate a word cloud

    Parameters:
        sentence (str): A string containing the input sentence

    Returns:
        cloud (numpy.ndarry): A Numpy array representing the word cloud image
        generate from the input sentence
    """
    final_text = []
    the_dictionary = {}

    argument1 = sentence.split()
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~--'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of","us","so","and", "or", "an", "as", "i", "me", "my", "up", "oh"     "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",     "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was","we","were", "be", "been","for", "being",     "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",     "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just","in","on","you"]
    
    # Running through the text and processing it
    # to remove punctuations and uninteresting words
    for word in argument1:

        text = ""
        word_in_lower = word.lower()
        
        for letter in word_in_lower:

            if letter not in punctuations and letter.isalpha():
                text = text + letter
            else:
                text = text + ""
        
        final_text.append(text)

    # The processed text has been stored in
    # final_text (list)


    # Running through the final_text list and
    # updating the dictionary with word frequency
    for word in final_text:
        if word not in uninteresting_words:
            
            if word not in the_dictionary:
                count = 1
                the_dictionary[word] = count
            
            else:
                freq = the_dictionary[word]
                the_dictionary[word] = freq + 1

    # Producing Numpy Array
    cloud = wordcloud.WordCloud(width=1000,height=1000,collocations=False)
    cloud.generate_from_frequencies(the_dictionary)
    return cloud.to_array()


# ### 4. Generating the Word Cloud
# 
# The code in the cell below generates the word cloud image from the text that is stored in the `file_contents` variable using the `generate_from_frequencies()` function.
# 
# The resulting image is then displayed using the `plt.show()` and `plt.imshow()` functions with the addition of setting the figure size and turning off the axis label.
# 
# Finally, a title is printed above the image.

# In[5]:


_upload()


# In[6]:


myimage = generate_from_frequencies(file_contents)
plt.figure(figsize=(20,10))
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')

print("Run 1")
print("The Beatles - Lucy in the Sky With Diamonds")

plt.show()


# In[7]:


_upload()


# In[8]:


newimage = generate_from_frequencies(file_contents)
plt.figure(figsize=(20,10))
plt.imshow(newimage, interpolation = 'nearest')
plt.axis('off')

print("Run 2")
print("Chapter 1 - Problems of Philosophy by Bertrand Russell")

plt.show()


# In[9]:


_upload()


# In[10]:


another_image = generate_from_frequencies(file_contents)
plt.figure(figsize=(20,10))
plt.imshow(another_image, interpolation = 'nearest')
plt.axis('off')

print("Run 3")
print("Do not go gentle into that good night - Dylan Thomas")

plt.show()


# ---
