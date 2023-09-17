# -*- coding: utf-8 -*-
"""Data By Density and Objects .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17PubemUuKUiW3Bp14dw7WDoQr9SgB3Rs
"""

from seaborn.categorical import color_palette
from IPython.utils.text import indent
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv('ProductionTail.csv')
plt.scatter(df['producer_timestamp'],df['classification'],cmap='viridis',alpha=0.7)
plt.colorbar(label='Color Scale')
plt.xlabel('Time Scale in Seconds')
plt.ylabel('Objects in the Camera')
plt.title('Bubble Graph with Colored Bubbles')
plt.show()