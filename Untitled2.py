#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd


# In[25]:


from bokeh.plotting import figure, output_file , show, output_notebook
output_notebook()


# In[26]:


def make_dashboard(x, gdp_change , unemploy, title, file_name):
    output_file(file_name)
    a = figure(title=title,x_axis_label = "year", y_axis_label = "%")
    a.line(x.squeeze(), gdp_change.squeeze(), line_width = 4, legend = "% unemploy")
    show(a)


# In[31]:


links = {'gdp':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}


# <h1> Question 1&2</h1>
# <p>Create a dataframe that contains the GDP data and display the first six rows of the dataframe</p>

# In[32]:


df_gdp = pd.read_csv(links["gdp"]) 
df_gdp.head(6)


# In[71]:


df_unempl = pd.read_csv(links["unemployment"])
df_unempl.head(6)


# <h2>Question 3. Display a dataframe where unemployment was greater than 8.5%</h2>

# In[72]:


df_unemploy85 = df_unempl[df_unempl["unemployment"]>8.5]
df_unemploy85.head(6)


# <h2> Question 4. Use Us the function make_dashboard to make a dashboard, then take a screen shot.</h2>

# In[73]:


x = df_gdp['date'] #column date
x.head(6)


# In[74]:


gdp_change= df_gdp["change-current"]
gdp_change.head(6)


# In[75]:


unemploy = df_unempl["unemployment"]#column unemployment
unemploy.head(6)


# In[76]:


title = "GDP & Unmployment" 
file_name = "index.html"


# In[77]:


make_dashboard(x=x, gdp_change=gdp_change, unemploy= unemploy, title=title, file_name=file_name)


# In[ ]:





# In[ ]:




