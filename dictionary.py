#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Task-1
fav_book = {"title" : "A Life in Movies ","author" : "shubhra Gupta ","publicationyear":"2023"}
fav_book2 ={"title":"Human Anatomy","author": "Dr. Ashvini Kumar Dwivedi","publiscationyear":"2023"}
fav_book3 ={"title":"inner engineering ","author":"sadhguru","publicationyear":"2016"}
fav_book4 ={"title":"lifes amazing secrats","author":"garu gopal das","publicationyear":"2018"}
print(fav_book.items())
print(fav_book2.items())
print(fav_book3.items())
print(fav_book4.items())


# In[25]:


print(fav_book2.get('title'))
print(fav_book3.get('title'))
print(fav_book4.get('title'))
print(fav_book2.get('author'))
print(fav_book3.get('author'))
print(fav_book4.get('author'))
print(fav_book2.get('publicationyear'))
print(fav_book3.get('publicationyear'))
print(fav_book4.get('publicationyear'))


# In[26]:


fav_book.popitem()
print(fav_book)


# In[27]:


fav_book2.copy()


# In[28]:


fav_book.update(title = "a lifee in movies")
print(fav_book)


# In[29]:


fav_book3.pop("title")
print(fav_book3)


# In[30]:


#task-2
english_to_spanish = {
    "hello": "hola",
    "goodbye": "adiós",
    "cat": "gato",
    "dog": "perro",
    "apple": "manzana"
}
english_word = input("Enter an English word: ").lower()
english_to_spanish.get(english_word)


# In[31]:


#task-3
student_grades = {}
for _ in range(5):
        student_name = input("Enter student name: ")
        student_grade = float(input("Enter student grade: ")) 
        student_grades[student_name] = student_grade
        total_grades = sum(student_grades.values())
        average_grade = total_grades / len(student_grades)
print(f"{student_name}: {student_grade}")
print(f"{average_grade:.2f}")
print(student_grades)


# In[16]:


contact_new = {}
user_name = input("enter your name: ")
phn_number = input("enter your phn number: ")
keys = user_name
values = phn_number
contact_new.update({keys:values})
print(contact_new.items())


# In[33]:



fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple',
    'orange': 'orange',
    'kiwi': 'green'
}
print("Color of apple:", fruit_colors['apple'])
fruit_colors['pear'] = 'green'
all_fruits = list(fruit_colors.keys())
print(all_fruits)
removed_fruit = fruit_colors.pop('kiwi')
print( removed_fruit)
print(fruit_colors)


# In[ ]:





# In[ ]:




