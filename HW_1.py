#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[13]:


train_df = pd.read_csv(r'C:\Users\ka422490\Downloads\Spring 20\CAP-5610-Machine Learning\Assignments\H,W 1\titanic\train.csv')


# In[12]:


test_df = pd.read_csv(r'C:\Users\ka422490\Downloads\Spring 20\CAP-5610-Machine Learning\Assignments\H,W 1\titanic\test.csv')


# In[14]:


combine = [train_df, test_df]


# In[15]:


result = pd.concat(combine)


# In[16]:


result.head()


# In[17]:


type(result)


# In[18]:


result.dtypes


# In[19]:


cols = result.columns


# In[20]:


num_cols = result._get_numeric_data().columns


# In[21]:


num_cols


# In[22]:


list(set(cols) - set(num_cols))


# In[23]:


result.isnull().sum()


# In[24]:


result.describe()


# In[25]:


result.Sex.value_counts() 


# In[26]:


result.Name.value_counts() 


# In[27]:


result.Cabin.value_counts() 


# In[28]:


result.Cabin.count() 


# In[29]:


result.Ticket.value_counts() 


# In[30]:


result.Ticket.count() 


# In[31]:


result.Embarked.count() 


# In[32]:


result.Embarked.value_counts() 


# In[33]:


result.Fare.value_counts()


# In[ ]:




