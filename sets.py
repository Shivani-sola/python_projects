#!/usr/bin/env python
# coding: utf-8

# # sets tasks

# In[6]:


#task-1`
set11 = {2,4,6,8,9}
print(set11)


# In[1]:


set1 = {1,2,3,4,5}
type(set1)


# In[5]:


#Tsak-2
s = {2,4,6,8,10,12,14,16,18,20}
t = {3,6,9,12,15,18,21}
w = set.union(s,t)
e = set.intersection(s,t)
s1 = set.difference(s,t)
print(w)
print(e)
print(s1)


# In[11]:


#Tsak-3
sett = {1,2,3,4,5,6,7,8,9,11,12,13,14}
sett.add(23)
sett.remove(5)
print(sett)
print( 1 in sett)


# In[21]:


#task-4
sets = {2,9,12,13,12,20,20,1,18,9,84,90,21}
sets1 = len(sets)
print(sets1)


# In[23]:


#task-5
lists = [2,9,12,13,12,20,20,1,18,9,84,90,21]
setss = set(lists)
dulicates = len(lists) - len(setss)
print(setss)
print(dulicates)


# In[ ]:




