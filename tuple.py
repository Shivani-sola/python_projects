#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Task--1
fav_fruits = ('watermelon','kiwi','graps','mulberry')
print(fav_fruits[0])
print(fav_fruits[1])
print(fav_fruits[2])
print(fav_fruits[3])
print(type(fav_fruits))
print(fav_fruits)


# In[11]:


#task--2
tuplee1 =(1,2,3,4,5)
tuplee2 =(6,7,8,9,10)
tuplee3 = tuplee1 + tuplee2
print(tuplee3)
print(len(tuplee3))


# In[25]:


#task--3
tuplees = (1,2,3,4,5,6,7,8,78)
m = set(tuplees)
print(m)
max_value = max(m)
min_value = min(m)
print(max_value)
print(min_value)


# In[29]:


#task--4
lists = (1,2,3,4,5,6)
lists[1]= 12
print(lists)
# tuple is immutable because if we create a tuple we cannot modifiy the tuple,so elements are not removed or added to the existing list.


# In[50]:


tupless1 = (1,22,33,44,53,65,76,88,92,10)
print(tupless1[2:7])


# In[6]:


frnds_fav_movies =('wish','barbie','the marvels','freelancer')
my_fav_movies ={'freelancer','evil dead rise','harry potter'}
common_elements = set(frnds_fav_movies).intersection(my_fav_movies)
print(common_elements)


# In[ ]:




