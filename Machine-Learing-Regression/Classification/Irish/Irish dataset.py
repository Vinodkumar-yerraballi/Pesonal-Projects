#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the standardliraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report


# In[2]:


#load the dataset
data=pd.read_csv('Iris.csv')
data.head().style.background_gradient(cmap='ocean')


# In[3]:


#Data information
data.info()


# In[4]:


#data describe
data.describe().style.background_gradient(cmap='winter_r')


# In[5]:


#Cehck the shape
data.shape


# In[6]:


data.columns


# In[7]:


#Remove the id column from the dataset
data.drop(['Id'],axis=1,inplace=True)


# In[8]:


species=data['Species'].value_counts()
plt.figure(figsize=(16,8))
plt.pie(species,labels=['Iris-setosa','Iris-versicolor','Iris-virginica'],explode=[0.05,0.07,0.08],colors=['red','yellow','green'],autopct="%1.2f%%")
plt.title("To visualize the Species in the dataset",fontsize=32)
plt.show()


# In[9]:


from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
df = AV.AutoViz('Iris.csv')
df


# In[10]:


data.columns


# # Modeling

# In[11]:


#divided the data into x and y
X=data.drop(['Species'],axis=1)
y=data['Species']


# In[12]:


#Divided the data into train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=42)


# In[13]:


#install the LogisticRegression
logistic=LogisticRegression()
#fit the train datset
logistic.fit(X_train,y_train)
#Prediction
logistic_pred=logistic.predict(X_test)


# In[14]:


#Check the accuracy score and train score
print(f'The accuracy_score test is {logistic.score(X_test,y_test)*100:.2f}')
print(f'The accuracy_score train is {logistic.score(X_train,y_train)*100:.2f}')
print(f'The accuracy_score is {accuracy_score(y_test,logistic_pred)*100:.2f}')


# # Classification_report and confusion_matrix

# In[15]:


#Classification_report 
print(classification_report(y_test,logistic_pred))
cn=confusion_matrix(y_test,logistic_pred)
sns.heatmap(cn,annot=True,cmap='winter_r',xticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'],yticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'])


# In[16]:


#install the decisiontreeclassifier
from sklearn.tree import DecisionTreeClassifier
#insall the treeclassifer
tree=DecisionTreeClassifier()
#fit the train dataset
tree.fit(X_train,y_train)
#Prediction
tree_pred=tree.predict(X_test)


# In[17]:


#Check the accuracy score and train score
print(f'The accuracy_score test is {tree.score(X_test,y_test)*100:.2f}')
print(f'The accuracy_score train is {tree.score(X_train,y_train)*100:.2f}')
print(f'The accuracy_score is {accuracy_score(y_test,tree_pred)*100:.2f}')


# In[18]:


#Classification_report 
print(classification_report(y_test,tree_pred))
cn=confusion_matrix(y_test,tree_pred)
sns.heatmap(cn,annot=True,cmap='Reds',xticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'],yticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'])


# In[19]:


#install the Randomforest classifier
from sklearn.ensemble import RandomForestClassifier
#install
random=RandomForestClassifier()
#fit the dataset
random.fit(X_train,y_train)
#Prediction
random_pred=random.predict(X_test)


# In[20]:


#Check the accuracy score and train score
print(f'The accuracy_score test is {random.score(X_test,y_test)*100:.2f}')
print(f'The accuracy_score train is {random.score(X_train,y_train)*100:.2f}')
print(f'The accuracy_score is {accuracy_score(y_test,random_pred)*100:.2f}')


# In[21]:


#Classification_report 
print(classification_report(y_test,random_pred))
cn=confusion_matrix(y_test,random_pred)
sns.heatmap(cn,annot=True,cmap='Reds',xticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'],yticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'])


# In[22]:


#install the Kneighborsclassifier from the sklearn
from sklearn.neighbors import KNeighborsClassifier
#Install the KNeighborsClassifier
knn = KNeighborsClassifier()
#And the fit the training dataset
knn.fit(X_train, y_train)
#prediction
knn_pred=knn.predict(X_test)


# In[23]:


#Check the test score and train score to the model
print(f'The KNeighborsClassifier model test score is {knn.score(X_test,y_test)*100:.2f}')
#Train score for the data
print(f'The KNeighborsClassifier model train scores is {knn.score(X_train,y_train)*100:.2f}')
#Check the accuracy_score to the model
print(f'The KNeighborsClassifier accuracy_score {accuracy_score(y_test,knn_pred)*100:.2f}')


# In[24]:


#Classification_report 
print(classification_report(y_test,knn_pred))
cn=confusion_matrix(y_test,knn_pred)
sns.heatmap(cn,annot=True,cmap='mako_r',xticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'],yticklabels=['Iris-setosa','Iris-versicolor','Iris-virginica'])


# In[ ]:




