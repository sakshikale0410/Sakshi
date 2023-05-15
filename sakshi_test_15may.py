#!/usr/bin/env python
# coding: utf-8

# # Machine learning -FST-5
# Grading Test -15-05-2023
# 
# Note : Read all the questions carefully before answering.
# 
# Save your jupyter notebook with ur name_date pattern ( shilpa_may15) and upload on github,and submit
# the github link in the google form provided.

# ## PART A ( Multiple choice 6*1 = 6)

# 1.A Lambda Function is a ________function
# 
# a)Small function
# 
# b)Anonymous function
# 
# c)Default function
# 
# d)All of the above
# 
# 

# 1] ANSWER= b)Anonymous function

# 2.Why would you use the pass statement ?
# 
# a) Python has the syntactical requirement that code blocks cannot be empty.
# 
# b)Ignoring (all or) a certain type of Exception
# 
# c)Testing that code runs properly for a few test values, without caring about the results
# 
# d) All of the above

# 2]ANSWER=a) Python has the syntactical requirement that code blocks cannot be empty.

# 3.What is MRO in Python?
# 
# a)Machine learning repository
# 
# b)defines the order in which the base classes are searched when executing a method.
# 
# c)Method over riding
# 
# d)Method overloading

# 3]ANSWER=d)Method overloading

# 4.What is self in Python?
# 
# a)You can access the attributes and methods of the class in python
# 
# b)Represents the instance of the class
# 
# c)Binds the attributes with the given argument
# 
# d) All of the above
# 

# In[ ]:


4]ANSWER=d) All of the above


# 5.What is __init__?
# 
# a)Object of every class
# 
# b)Constructor method in python
# 
# c)Only few classes in python have init methods
# 
# d)None of the above

# 5]ANSWER=b)Constructor method in python

# 6.What does * indicate in regular expression?
# 
# a)One or more occurrences
# 
# b)Zero or more occurrences
# 
# c)Zero or one occurrences
# 
# d)Exactly the specified number of occurrences
# 

# In[ ]:


6]ANSWER=b)Zero or more occurrences


# ## PART B ( Answer in a line 10*2  = 20)
# 

# 6.What is break and continue in python? Explain with example

# In[36]:


#BREAK =TO BREAK THE LOOP
num=0
while num <= 10:
    print (num)
    num += 1
    if num == 3:
        break
    
  


# In[38]:


#continue -it will skip given current step
for i in range(0, 10):
    if i == 5:
        continue
    print(i)


# 7.What are Dict and List comprehensions? Give atleast one example(code)

# In[121]:


#lisl
list=[]
for s in range(1,6):
    list.append(s+2)
print(list)


# In[ ]:





# 8.How do you create a class in Python?

# In[71]:


class student:
    def __init__(self):
        marks=50
        print(f'your score is {marks}')
sakshi=student()
        


# 9.What is inheritance ?Give  one example
# here parent class has 1 child class
# child class can access all the methods from parent class except private function or methods

# In[73]:


class college:
    def __init__(self):
        print('good afternoon students')
        
class student(college):
    pass

sakshi=student()
        


# 10.What is polymorphism? Give one example

# In[29]:





# 11.Difference between multilevel and multiple inheritance?

# In[80]:


#multiple=two parents single child

class college:
    def __init__(self):
        print('we build education')
        
class staff:
     def __init__(self):
            print('we teach students')

class student(college,staff):
    pass

stm=student()



# In[91]:


#multilevel =grandfather ,father,child
class college:
    def __init__(self):
        print('we build education')
class staff(college):
     def abc(self):
            print('we teach students')
class student(staff):
    pass

stm=student()
sta=staff()
stm.abc()


# 12.Create a 1D,2D and 3D array?

# In[107]:


#1d array
a=np.array([1,2,3])
print(a)
print(a.ndim)


#2d array
b=np.array([[1,2],[12,32]])
print(b)
print(b.ndim)



#3d array
c= np.array([[[12,43,54], [45,76,23]], [[23,76,89], [36,47,28]]])
print(c)
print(c.ndim)



# 13.How will you reverse the numpy array using one line of code?
# 
# 

# In[120]:


import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr[::-1])


# 14.What advantages do NumPy arrays offer over  Python lists?
# 

# In[54]:


li=[12,34,23,43]
import numpy as np
a=list/2
print(a)
#you can't divide list 


# In[53]:


b=np.array([12,34,24])
print(b/2)   #but here ypu can divide each number ,therefore we use array over list


# 15.python3 code to print the below pattern
# 
# *
# **
# ***

# In[67]:


n= 3
for i in range(n):
    print("  ",end = " ")# rows
    for j in range(i+1):    # columns
        print("*",end = " ")
        
    print()


# ## PART C (Exploratory data analysis)

# 16.Draw insights from the dataset provided using suitable visualization libraries.(6*4 = 24)

# 1.Load the "Diamonds dataset " from seaborn library
# 
# Dataset desciption:
# (carat: weight of the diamond
# cut: (Fair, Good, Very Good, Premium, Ideal) ordinal
# color: J (worst) to D (best) ordinal
# clarity: [I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best)]
# depth: z / (mean(x,y)) = 2*z / (x+y) in percentage
# table: percentage of width on the top relative to width
# price: given in US Dollars
# x: length in mm
# y: width in mm
# z: depth in mm)
# 
# 2.Which column has highest correlation with the target variable?(Graphs)
# 
# 3.Find the outliers in each column?Use suitable graphs
# 
# 4.what is the count of premium diamonds in the dataset?
# 
# 5.What is the average price of diamonds?
# 
# 6.Create a new column called "size = x*y*z

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[6]:


dm=pd.read_csv(r"C:\Users\Sankalp Kale\Downloads\diamonds.csv.zip")
dm.head()


# 2.Which column has highest correlation with the target variable?(Graphs)

# In[7]:


dm.corr()


# In[31]:


corr = dm.corr()
sns.heatmap(corr)


# 3].Find the outliers in each column?Use suitable graphs

# In[8]:


dm.describe()


# In[17]:


#sns.boxplot(x = 'carat', y = 'depth',data = dm)
sns.boxplot(x =dm['carat'])
plt.show()
sns.boxplot(x =dm['depth'])
plt.show()
sns.boxplot(x =dm['table'])
plt.show()
sns.boxplot(x =dm['price'])
plt.show()
sns.boxplot(x =dm['x'])
plt.show()
sns.boxplot(x =dm['y'])
plt.show()
sns.boxplot(x =dm['z'])
plt.show()


# 4.what is the count of premium diamonds in the dataset?

# In[21]:


dm['cut'].value_counts()


# In[ ]:


get_ipython().run_line_magic('pinfo', 'diamonds')


# In[25]:


a=dm['price'].sum()


# In[24]:


b=len(dm['price'])


# In[28]:


avg=round(a/b)
avg


# Create a new column called "size = xyz"

# In[30]:


dm['size']=dm['x']*dm['y']*dm['z']
dm.head()

