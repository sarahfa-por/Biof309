#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def clearnulls(dataframe, col):
    """first creates series of boolians indicating if rows in indicated column are null then drops from dataframe rows where 
    null is true in that column"""
    col_null = dataframe[col].isnull()
    return dataframe.drop(dataframe[col_null].index)

