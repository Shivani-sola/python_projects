#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task-1
def add(a,b):
    print(a+b)
add(10,20)    #using posistional arguments.


# In[6]:


def add1(b,a):
    print(a+b)
add1(b=30,a=50)   #using keyword arguments. 


# In[10]:


def add2(*n):
    print(sum(n))
add2(1,2,2,3,4)


# In[13]:


add=lambda a,b,d: a+b+d
add(12,13,14)     #using lambda function.


# In[18]:


#task-2
def mul(a,b):
    print(a*b)
mul(10,20)   


# In[15]:


def mul1(b,a):
    print(a+b)
mul1(b=30,a=50)


# In[19]:


add=lambda a,b,d: a*b*d
add(12,13,14)     #using lambda function.


# In[2]:


#task-3
def calculate_average(numbers):
    if not numbers:
        return None  
    total = sum(numbers)
    average = total / len(numbers)
    return average
numbers_list = [10, 20, 30, 40, 50]
result = calculate_average(numbers_list)
print(f"The average is: {result}")


# In[3]:


#task-4
def is_even(number):
    return number % 2 == 0
num = int(input("enter a number:: "))
result = is_even(num)

if result:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# In[5]:


#task-5
def reverse_string(input_string):
    return input_string[::-1]
original_string = str(input("enter a string to reverse:: "))
reversed_string = reverse_string(original_string)
print(original_string)
print(reversed_string)


# In[12]:


#task-6
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count
user_input = input("Enter a string: ")
result = count_vowels(user_input)
print(f"Number of vowels in '{user_input}': {result}")


# In[19]:


#task-7
def find_max(*n):
    print(max(n))
find_max(1,2,3,11,23,45,23)    


# In[21]:


#task-8
def find_min(*n):
    print(min(n))
find_min(1,2,3,11,23,45,23)    


# In[27]:


#task-9
list1 = [23,34,56,78]
def fun(n):
    print(sum(n))
fun(list1)


# In[ ]:





# In[ ]:




