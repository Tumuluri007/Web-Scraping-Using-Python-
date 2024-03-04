#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests


# In[8]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')


# In[9]:


print(soup)


# In[34]:


table = soup.find('table', class_ = 'wikitable sortable')


# In[35]:


print(table)


# In[37]:


world_titiles = table.find_all('th')


# In[38]:


world_titiles


# In[40]:


word_table_titles = [title.text.strip() for title in world_titiles]


# In[41]:


print(word_table_titles)


# In[53]:


import pandas as pd


# In[89]:


df = pd.DataFrame(columns = word_table_titles )

df


# In[59]:


coloumm_data = table.find_all('tr')

print(coloumm_data)


# In[91]:


for row in coloumm_data[1:]:
   row_data =  row.find_all('td')
   individual_row_data = [data.text.strip() for data in row_data]
   print(individual_row_data)
   
   length = len(df)
   df.loc[length] = individual_row_data

       


# In[92]:


df


# In[97]:


df.to_csv(r'C:\Users\tumul\OneDrive\Desktop\web scraping\companies.csv', index = False)


# In[ ]:




