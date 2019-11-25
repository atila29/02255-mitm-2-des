#!/usr/bin/env python
# coding: utf-8

# In[2]:


import des


# In[3]:


from des import DesKey


# In[5]:


key0 = DesKey(b"000000000000000000000000")      
key1 = DesKey(b"111111111111111111111111") 


# In[8]:


key0.is_single() 


# In[10]:


encMSG0 = key0.encrypt(b"blablabla", padding=True)
encMSG1 = key1.encrypt(encMSG0)


# In[11]:


encMSG1


# In[12]:


encMSG0


# In[13]:


encMSG1


# In[ ]:




