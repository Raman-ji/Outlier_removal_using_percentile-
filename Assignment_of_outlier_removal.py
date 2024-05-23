#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv(r"C:\Users\uniqu\Downloads\archive\AB_NYC_2019.csv")


# In[3]:


df


# In[4]:


df.describe()


# In[7]:


percentile_1=df.price.quantile(0.01)


# In[8]:


percentile_999=df.price.quantile(0.999)


# In[14]:


df_no_outlier= df[(df.price>percentile_1) & (df.price<percentile_999)]


# In[15]:


df_no_outlier


# In[16]:


df_no_outlier.shape


# In[17]:


df_no_outlier.describe()


# In[ ]:




