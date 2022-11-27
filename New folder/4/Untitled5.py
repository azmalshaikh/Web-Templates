#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random


# In[6]:


matrix=[[2,6],[8,12],[15,5],[3,9],[11,8],[22,10],[18,30],[12,20],[12,14],[20,30]]
matrix=np.matrix(matrix)
matrix


# In[7]:


def dist_mat(numof_k):
    distance_matrix_old= np.zeros((matrix.shape[0],numof_k))
    k = np.random.randint(matrix.shape[0], size=numof_k)
    for i in range(len(k)):
        for j in range(matrix.shape[0]):
            distance_matrix_old[j,i] = np.sum(abs(matrix[j,0:]-matrix[k[i],:]))
    return(distance_matrix_old)


# In[8]:


x=dist_mat(3)
x


# In[9]:


def clusters(dist_mat):
    minimum=[]
    clust=[]
    for i in range(dist_mat.shape[1]):
         clust.append([])
    for i in range(dist_mat.shape[0]):
        for j in range(dist_mat.shape[1]):
            if min(dist_mat[i])==dist_mat[i,j]:
                minimum.append(min(dist_mat[i]))
                clust[j].append(dist_mat[i])
    return(clust,minimum)


# In[11]:


old_min_value=clusters(x)[1]


# In[12]:


def kmedoids(numof_k,n):
    distance_matrix_new= np.zeros((matrix.shape[0],numof_k))
    k = np.random.randint(matrix.shape[0], size=numof_k)
    list2=[i for i in range(matrix.shape[0]) if i not in k]
    for iteration in range(n):
        for i in range(len(k)):
            for j in range(len(list2)):
                k[i]=list2[j]
                for k_val in range(len(k)):
                    for value in range(10):
                        distance_matrix_new[value,k_val] = np.sum(abs(matrix[value,0:]-matrix[k[k_val],:]))
                        new_min_value=clusters(distance_matrix_new)[1]
                        if sum(new_min_value)- sum(old_min_value)<0:
                            cluster=clusters(distance_matrix_new)[0]
                        else:
                            cluster=clusters(x)[0]
    return(cluster)


# In[13]:


kmedoids(3,10)


# In[ ]:




