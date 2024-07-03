#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)


# In[43]:


df = pd.read_csv("credit_card_recommendation.csv")
df.head(30)


# In[29]:


df.index


# In[24]:


df['Need_Credit_Card'].isnull().sum()


# In[27]:


df.isna().sum()


# In[6]:


df.info()


# In[21]:


df['Need_Credit_Card'].isnull().any()


# In[44]:


df.loc[df['Has_Credit'].isna(), 'Need_Credit_Card']


# In[46]:


df.loc[df['Has_Credit'].isna(), 'Need_Credit_Card'].sum()


# In[47]:


df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit'] = df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit'].fillna('Yes')


# In[49]:


df.loc[df['Has_Credit'] == 'Yes', 'Need_Credit_Card'].sum()


# In[51]:


df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit']


# In[53]:


df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit'].value_counts()


# In[56]:


df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit'].value_counts()[1]/(df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit'].value_counts()[0]+df.loc[df['Need_Credit_Card'] == 1, 'Has_Credit'].value_counts()[1])

