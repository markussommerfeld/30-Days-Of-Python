# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:18:31 2024

@author: marku
"""

"""

    Read the hacker_news.csv file from data directory
    Get the first five rows
    Get the last five rows
    Get the title column as pandas series
    Count the number of rows and columns
        Filter the titles which contain python
        Filter the titles which contain JavaScript
        Explore the data and make sense of it
"""

import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np
import re
#1 done
# df = pd.read_csv('C:/GitHub/30-Days-Of-Python/data/weight-height.csv')
df = pd.read_csv('C:/GitHub/30-Days-Of-Python/data/hacker_news.csv')


#2 done
print(df.head())

#3 done
print(df.tail())

#4 done
print(df.columns)

#5 done
print(df.shape)

Python_list = []
Java_list = []
for j in df['title']:
    # if 'python' in j:
    if   re.search(r'\bpython\b', j, re.I):
        Python_list.append(j)
    if   re.search(r'\bJavaScript\b | \bJava Script\b' , j, re.I):
        Java_list.append(j)
        
print('Java:',len(Java_list), '; Python:', len(Python_list))