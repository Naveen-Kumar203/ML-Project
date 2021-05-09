#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_csv("netflix.csv")


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.drop("cast",axis=1,inplace=True)
df.drop("director",axis=1,inplace=True)
df.drop("show_id",axis=1,inplace=True)
df.drop("description",axis=1,inplace=True)


# In[9]:


df.info()


# In[10]:


df["country"] = df["country"].fillna(df["country"].mode())


# In[11]:


df["rating"]=df["rating"].fillna(df["rating"].mode()[0])


# In[12]:


df[df.date_added.isna()]


# In[13]:


df=df[df["date_added"].notna()]


# In[14]:


df.isna().sum()


# In[15]:


df["country"]=df["country"].fillna(df["country"].mode()[0])


# In[16]:


df.isna().sum()


# In[17]:


df["date_added"]=pd.DatetimeIndex(df.date_added)
df["year"]=pd.DatetimeIndex(df["date_added"]).year
df["month"]=pd.DatetimeIndex(df["date_added"]).month


# In[18]:


df["types"]=df["type"].map({"TV Show":0,"Movie":1})


# In[19]:


df["rating"].unique()


# In[20]:


ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}


# In[21]:


df["ratings_ages"]=df["rating"].replace(ratings_ages)


# In[23]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


df["type"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.title("%AGE OF MOVIES AND TV SHOWS")
plt.legend()
plt.show()


# In[25]:


countries=pd.crosstab(df["country"],["type"]).sort_values(by="type",ascending=False)
countries.head(10).plot(kind="bar")
plt.legend()
plt.title("COUNTRY WITH HIGHEST NUMBER OF SHOWS")
plt.show()


# In[26]:


df.groupby(df["types"])["country"].value_counts()[0].head(10).plot(kind="barh",color="red")
plt.title("Number of TV-SHOWS AVAILABLE IN COUNTRY")
plt.show()


# In[27]:


df.groupby(df["types"])["country"].value_counts()[1].head(10).plot(kind="barh",color="red")
plt.title("Number of MOVIES AVAILABLE IN COUNTRY")
plt.show()


# In[28]:


df.groupby(by=df["types"])["year"].value_counts()[0].plot(kind="bar",color="black")
plt.title("NUMBER OF TV SHOWS ADDED IN NETFLIX")
plt.show()


# In[29]:


df.groupby(by=df["types"])["year"].value_counts()[1].plot(kind="bar",color="black")
plt.title("NUMBER OF MOVIES ADDED IN NETFLIX")
plt.show()


# In[30]:


pd.crosstab(df["type"],df["ratings_ages"]).plot(kind="bar")
plt.title("WHAT TYPE OF CONTENT IS MOST")
plt.show()


# In[31]:


x=df.groupby(df["types"])["duration"].value_counts()[0]
x.head(10).plot(kind="bar")
plt.title("DURATION OF TV-SHOWS")
plt.show()


# In[32]:


x=df.groupby(df["types"])["duration"].value_counts()[1]
x.head(10).plot(kind="bar")
plt.title("DURATION OF MOVIES")
plt.show()


# In[33]:


sns.boxplot(x="ratings_ages",y="year",data=df)


# In[34]:


sns.countplot(x="ratings_ages",data=df)
plt.title("NUMBER OF RATINGS ")
plt.show()


# In[35]:


pd.crosstab(df["year"],df["ratings_ages"]).sort_values(by="year",ascending=False).plot(kind="bar")
plt.title("RATINGS BASED ON YEAR")
plt.show()


#  ### Listed in Genre

# In[38]:


df["listed_in"].value_counts().head(10).plot(kind="bar",color="red")
plt.title("MOST NUMBER OF GENRES IN NETFLIX ")
plt.show()


# In[39]:


df.groupby(df["listed_in"])["year"].value_counts().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("WHICH GENRE IS MOST ADDED")
plt.show()


# In[42]:


df.groupby(by=df["types"])["listed_in"].value_counts()[1].head(10).plot(kind="bar",color="skyblue")
plt.title("TOP 10 GENRES IN MOVIES")
plt.show()


# In[45]:


df.groupby(by=df["types"])["listed_in"].value_counts()[0].head(10).plot(kind="bar",color="green")
plt.title("TOP 10 GENRES IN TV-SHOWS")
plt.show()


# In[ ]:




