#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pyspark.sql import SparkSession


# In[4]:


spark = SparkSession.builder.getOrCreate()


# In[16]:


csv = spark.read.option('delimiter',';').option('header',True).csv('./teste.csv')


# In[17]:


csv.show()

