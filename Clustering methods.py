#!/usr/bin/env python
# coding: utf-8

# In[1]:


#K-means method


# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import sklearn
from sklearn.preprocessing import scale
import sklearn.metrics as sm
from sklearn.metrics import confusion_matrix, classification_report


# In[34]:


from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets


# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure(figsize=(7,4))


# In[36]:


iris = datasets.load_iris()

x = scale(iris.data)
y = pd.DataFrame(iris.target)
variable_names = iris.feature_names
x[0:10]


# In[40]:


#Building and running model

clustering = KMeans(n_clusters=3, random_state=5)

clustering.fit(x)


# In[50]:


#Plotting model outputs

iris_df = pd.DataFrame(iris.data)
iris_df.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
y.columns = ['Targets']


# In[58]:



clustering.labels_


# In[65]:


color_theme = np.array(['darkgray', 'lightsalmon', 'powerblue'])

plt.subplot(1,2,1)

plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=iris.target, s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)

plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=clustering.labels_, s=50)
plt.title('KMeans Classification')


# In[67]:


relabel = np.choose(clustering.labels_, [2,0,1]).astype(np.float64)

plt.subplot(1,2,1)

plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=iris.target, s=50)
plt.title('Ground Truth Classification')

plt.subplot(1,2,2)

plt.scatter(x=iris_df.Petal_Length, y=iris_df.Petal_Width, c=relabel, s=50)
plt.title('KMeans Classification')


# In[68]:


# Evaluating cluster results
print(classification_report(y, relabel))


# In[ ]:




