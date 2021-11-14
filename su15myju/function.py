#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import matplotlib as plt
from ipywidgets import interact, fixed
from PIL import Image

"""
You should create a way to resize an image from an array X.
The use of widgets is optional but you can take a look to interact.
We should be able to install this package in Google Colab from your Git
repo.

"""
# there wasn't a specific approach given, for this reason, I used this one where the user can input his/her desired width, hieght.

def imshow(X,width,height):
    ImFromArr = Image.fromarray(X)
    resizeImage = ImFromArr.resize((width,height))
    resizeImage.show()
