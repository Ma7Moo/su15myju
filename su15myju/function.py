#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib as plt
from PIL import Image


# In[23]:


#X = np.random.randint(0, 255, (256,256))


# In[33]:


#X.shape[0]
resized = np.reshape(X,(X.shape[0],X.shape[1]))
im = Image.fromarray(resized)
im.show()


# In[7]:





# In[ ]:




