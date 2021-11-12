#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib as plt
from PIL import Image




#X.shape[0]
resized = np.reshape(X,(X.shape[0],X.shape[1]))
im = Image.fromarray(resized)
im.show()


# In[7]:





# In[ ]:




