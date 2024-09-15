#!/usr/bin/env python
# coding: utf-8

# # 1.Revese a string

# In[1]:


s="karthik"
a=s[::-1]
print(a)


# # 2.count the number vowels in a given string

# In[2]:


def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage
input_string = "Hello, Karteek Kunisetti!"
vowel_count = count_vowels(input_string)
print(f"Number of vowels: {vowel_count}")


# # 3.find length of string

# In[6]:


s = "Hello, Karteek Kunisetti!"
s_length=len(s)
print(f"Length of string is:{s_length}")


# # 4.count the no.of occurance of a character in a given string

# In[7]:


# Example usage
input_string = "Hello, Karteek Kunisetti!"
char_to_count = 'e'
occurrences = input_string.count(char_to_count)

print(f"Number of occurrences of '{char_to_count}': {occurrences}")


# # 5.convert sring to lower case

# In[8]:


# Example usage
input_string = "Hello, Karteek Kunisetti!"
lowercase_string = input_string.lower()

print(f"Lowercase string: {lowercase_string}")


# # 6.covert string to upper case

# In[9]:


# Example usage
input_string = "Hello, Karteek Kunisetti!"
uppercase_string = input_string.upper()

print(f"Lowercase string: {uppercase_string}")


# # 7.concatinate two strings

# In[18]:


# Example usage
string1 = "Hello, Karteek!"
string2 = " Welcome to the world of Python."

concatenated_string = ' ' .join([string1, string2])

print(f"Concatenated string using join(): {concatenated_string}")


# In[12]:


# Example usage
string1 = "Hello, Karteek!"
string2 = " Welcome to the world of Python."

concatenated_string = string1 + string2

print(f"Concatenated string: {concatenated_string}")


# # 8.count the number of words in a sentance

# In[19]:


# Example usage
input_sentence = "Hello, Karteek Kunisetti! Welcome to the world of Python."

# Split the sentence into words using spaces as delimiters
words = input_sentence.split()

# Count the number of words
word_count = len(words)

print(f"Number of words: {word_count}")


# # 9.convert a list of string to upper case

# In[27]:


# Example usage
string_list = ["hello", "karteek", "kunisetti", "python"]

# Convert each string in the list to uppercase
uppercase_list = [string.upper() 
for string in string_list]

print(f"List of strings in uppercase: {uppercase_list}")


# # 10.Determine the given string is pangram

# In[28]:


import string

def is_pangram(input_string):
    # Convert the input string to lowercase and remove spaces
    input_string = input_string.lower().replace(" ", "")
    
    # Create a set of all alphabet letters
    alphabet = set(string.ascii_lowercase)
    
    # Create a set of all letters in the input string
    input_letters = set(input_string)
    
    # Check if the input contains all the letters of the alphabet
    return alphabet.issubset(input_letters)

# Example usage
input_string = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_string):
    print(f"'{input_string}' is a pangram.")
else:
    print(f"'{input_string}' is not a pangram.")

