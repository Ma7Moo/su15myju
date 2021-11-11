#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from distutils.core import setup
from setuptools import find_packages
# I will use the given templates data 
setup(name='idem_id',
      version='0.1',
      author='DSSS',
      author_email='name@fau.de',
      packages=find_packages(),
      install_requires=['numpy','pillow','ipywidgets'])

