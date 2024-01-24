#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sales Analysis Project in Python


# # Introduction
# Welcome to the Sales Analysis project! In this project, we will be analyzing sales data to gain insights 
# into the performance of products, regions, and overall sales trends. The goal is to extract valuable information 
# that can aid in decision-making and strategy development for the business.
# 

# In[3]:


# Import necessary libraries
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt


# 
# ## Data Collection:
#    - Obtain the sales data from your source (CSV file, database, API, etc.).
#   

# In[4]:


df = pd.read_csv("D:\\Professionaal folders\\projects\\Diwali_sales\\Python_Diwali_Sales_Analysis-main\\Diwali Sales Data.csv", encoding="ISO-8859-1")
df.head()


# # Data Exploration:
# 
# - Step 1 = Display basic information about the dataset 
# - Step 2 = Drop unnecessary columns
# - Step 3 = Check for null values

# In[5]:


# Step 1 = Display basic information about the dataset 
df.info()
df.columns


# In[6]:


# Step 2
# Drop unnecessary columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[7]:


# Step 3 
# Check for null values
df.isnull().sum()


# In[8]:


df.dropna(inplace = True)


# In[9]:


df["Amount"] = df["Amount"].astype('int')


# In[11]:


df.columns


# In[12]:


df.rename(columns = {'Marital_Status':'Shaadi'})


# In[13]:


df.describe()


# In[14]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# Gender 

# In[17]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


# plotting a bar chart for gender vs total amount 

sales_gen = df.groupby(['Gender'],as_index= False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# # AGE

# In[22]:


ax = sns.countplot(data = df, x= 'Age Group',hue = "Gender")
for bars in ax.containers:
    ax.bar_label(bars)


# In[23]:


# total amount vs age group 
sales_age = df.groupby(["Age Group"],as_index = False )["Amount"].sum().sort_values(by = "Amount",ascending = False) 
sns.barplot(x= 'Age Group', y = 'Amount',data = sales_age)


# In[24]:


# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[26]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[27]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# # Occupation

# In[28]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# # Product Category

# In[37]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[38]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[39]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[40]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion:
# Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category

# In[ ]:




