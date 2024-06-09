# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:17:57 2024

@author: AhmedShafique
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

dataset = pd.read_csv('50_startups.csv')
print(dataset.head())

#%%

print(dataset.describe())

#%%

dataset.isnull().any()
#%%

c= dataset.corr()
print(c)