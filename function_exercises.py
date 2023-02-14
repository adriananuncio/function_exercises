#!/usr/bin/env python
# coding: utf-8

# In[29]:


# 1.

def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False
    
is_two(2)
is_two('2')


# In[ ]:





# In[ ]:





# In[80]:


# 2

def is_vowel(x):
    if type(x) == str:
        if len(x) == 1:
            return x.lower() in list('aeiou')
        else: 
            return False
    else:
        return False


# In[16]:


is_vowel('a')


# In[25]:


# 3

def is_consonant(x):
    if type(x) == str:
        if len(x) == 1 and not is_vowel(x):
            return True
        else:
            return False
    else: 
        return False
            


# In[30]:


is_consonant('d')


# In[41]:


# 4

def cap_begining_consonant(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word


# In[44]:


cap_begining_consonant('hi')


# In[7]:


# 5. Define a function named calculate_tip.
## It should accept a tip percentage 
## (a number between 0 and 1) and the bill total, 
## and return the amount to tip.

bill_total = int(input('How much is your bill? '))

tip = float(input('What percent of your bill would you like to tip? '))

def calculate_tip(x):
    return x * tip

calculate_tip(bill_total)


# In[10]:


# 6. Define a function named apply_discount. 
## It should accept a original price, and a 
## discount percentage, and return the price 
## after the discount is applied.


def apply_discount(x):
    discount = 0.20
    return x - (x * discount)


# In[11]:


apply_discount(100)


# In[34]:


# 7. Define a function named handle_commas. 
## It should accept a string that is a number 
## that contains commas in it as input, and 
## return a number as output.

def handle_commas(x):
    my_number = x.replace(',','')
    return int(my_number)


# In[36]:


print(handle_commas('1,00,000,00'))


# In[58]:


# 8. Define a function named get_letter_grade. 
## It should accept a number and return the 
## letter grade associated with that number (A-F).
                    
                    
def get_letter_grade(grade):
    if grade >= 90 and x <= 100:
        return 'A'
    elif grade >= 80 and x < 90:
        return 'B'
    elif grade >= 70 and x < 80:
        return 'C'
    elif grade >= 60 and x < 70:
        return 'D'
    elif grade < 60:
        return 'F'
    
get_letter_grade(70)


# In[89]:


# 9. Define a function named remove_vowels 
## that accepts a string and returns a string 
## with all the vowels removed.

def remove_vowels(word):
    no_vowels = ''
    for x in word: 
        if is_vowel(x):
            continue
        else:
            no_vowels += x
    return no_vowels


# In[90]:


remove_vowels('hello')


# In[152]:


# 10. 

def normalize_name(name):
    new_name = ''
    for n in name:
        if n.isdigit() or n.isalpha() or n == ' ':
            new_name += n
    return new_name.strip().lower().replace(' ','_')


# In[154]:


normalize_name('   Adriana Nuncio   ')


# In[165]:


# 11.
import numpy
def cumulative_sum(some_list):
    return numpy.cumsum(some_list)


# In[166]:


cumulative_sum([1, 4, 5, 8])


# In[ ]:




