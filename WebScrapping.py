#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install autoscraper')


# In[2]:


from autoscraper import AutoScraper


# In[3]:



justdial_url = 'https://www.justdial.com/Hyderabad/Mechanics/nct-10222543'

wanted_list = ["Viayawada Highway Hayat Nagar"]


# In[4]:


scraper = AutoScraper()
result = scraper.build(justdial_url, wanted_list)
print(result)


# In[5]:





# In[6]:




