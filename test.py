#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import scipy.sparse as sps
"""Takes input from the Test data and formats it in a way analogous to that of the training set. i.e a matrix M of users as rows and movies as columns"""
#column headers for the dataset
data_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
item_cols = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL',
             'unknown', 'Action', 'Adventure', 'Animation', 'Childrens', 'Comedy', 'Crime',
             'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
             'Romance ', 'Sci-Fi', 'Thriller', 'War', 'Western']
user_cols = ['user id', 'age', 'gender', 'occupation', 'zip code']

#importing the data files onto dataframes
users = pd.read_csv('ml-100k/u.user', sep='|', names=user_cols, encoding='latin-1')
item = pd.read_csv('ml-100k/u.item', sep='|', names=item_cols, encoding='latin-1')
data = pd.read_csv('ml-100k/u1.test', sep='\t', names=data_cols, encoding='latin-1')

#==============================================================================
#  Creating the Adjacency matrix M with rows as users and columns as movies
#==============================================================================
df = pd.crosstab(data.user_id, data.movie_id, values=data.rating, aggfunc="mean")
df.fillna(value=0, inplace=True)
M = sps.coo_matrix((df))
del df
