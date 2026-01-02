#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('/home/vinod/Downloads/Python-3.10.3/data.csv')


# In[3]:


df.head(5)


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.drop(["Engine Fuel Type", "Market Category", "Vehicle Style", "Popularity", "Number of Doors",
"Vehicle Size"],axis=1,inplace=True)


# In[8]:


df.head(5)


# In[145]:


rename_cols = df.rename(columns={"Engine HP":"HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Tr","Driven_Wheels": "Drive_Mode","highway MPG": "MPG_H", "city mpg": "MPG_C" })


# In[146]:


df1=rename_cols


# In[147]:


df1.head(5)


# In[96]:


df1.count()


# In[97]:


df1[df1.duplicated()].sum()


# In[98]:


df1.drop_duplicates(inplace=True)


# In[99]:


df1.head(5)


#  df1.count()

# In[100]:


df.isnull().sum()


# In[101]:


df1.dropna(inplace=True)


# In[102]:


df1.head(5)


# In[103]:


df1.isnull().sum()


# In[104]:


df1.describe()


# In[105]:


sns.boxplot(x=df1['MSRP'])


# In[106]:


sns.boxplot(x=df1['HP'])


# In[107]:


sns.boxplot(x=df1['Cylinders'])


# In[108]:


df1.head(5)


# In[109]:


df1.columns


# In[114]:


l=df1.loc[:,["Year","Cylinders","HP","MPG_H","MPG_C","MSRP"]]


# In[115]:


l


# In[116]:


Q1=df.MSRP.quantile(.25)
Q3=df.MSRP.quantile(.75)
IQR=Q3-Q1


# In[117]:


IQR


# In[118]:


lower_limit=Q1-1.5*IQR
upper_limit=Q3+1.5*IQR


# In[119]:


lower_limit,upper_limit


# In[120]:


df2=df[(df1.MSRP<lower_limit)|(df1.MSRP>upper_limit)]


# In[121]:


df2


# In[122]:


from scipy import stats


# In[123]:


z_scores=np.abs(stats.zscore(l))


# In[124]:


z_scores


# In[125]:


zscores=stats.zscore(l)


# In[126]:


zscores


# In[127]:


df.head(5)


# In[128]:


for i in df.columns:
    print("the car %s brand in column" %i)
df['Make'].value_counts()


# In[129]:


df.columns


# In[130]:


sns.distplot(df1.HP,hist=True,color='r')


# In[131]:


l


# In[138]:


c=0
plt.figure(figsize=(15,10))
for i in l:
    l.plot(xlabel='Density',ylabel='Year')
    l.plot(xlabel='Density',ylabel='HP')
    l.plot(xlabel='Density',ylabel='MPG_H')
    l.plot(xlabel='Density',ylabel='MPG_C')
    l.plot(xlabel='Density',ylabel='MSRP')
plt.show()


# In[140]:


plt.figure(figsize = (12,8))
df1.plot(x='Make',kind='bar',ax=None)


plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make')


# In[148]:


df1.head(2)


# In[151]:


plt.figure(figsize=(15,5))
sns.countplot(x='Tr',data=df1,hue='Drive_Mode')


# In[153]:


fig, ax = plt.subplots(figsize=(10,6))
x='HP'
y='MSRP'
plt.scatter(x,y,data=df1)


# In[154]:


sns.jointplot(x='MPG_H',y='MPG_C',data=df1)


# In[159]:


from numpy import median
sns.barplot(x='Cylinders',y='MSRP',data=df1,estimator=median)


# In[161]:


sns.barplot(x='MSRP',y='Tr',data=df1)


# In[164]:


plt.figure(num=None, figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
sns.barplot(x='MSRP',y='Tr',hue='Drive_Mode',data=df1)


# In[165]:


sns.pairplot(data=df)


# In[166]:


cor=df1.corr()


# In[167]:


cor


# In[171]:


#set cmap = 'BrBG', annot = True - to get the same graph as shown below 
# set size of graph = (12,8)
plt.figure(figsize=(12,8))
sns.heatmap(cor,annot=True,cmap='BrBG')


# In[ ]:




