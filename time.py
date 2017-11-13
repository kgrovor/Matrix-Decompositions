#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:26:54 2017
"""
import time
import SVD
import data
import CUR
import collaborative

start = time.time()
SVD.svd_retained_energy(1)
end = time.time()
svd_time = end - start
print("\n SVD Runtime is: ", svd_time)

start = time.time()
SVD.svd_retained_energy(0.9)
end = time.time()
svdret_time = end - start
print("\n SVD retained energy runtime is: ", svd_time)

start = time.time()
CUR.cur(data.M.todense(),1)
end = time.time()
cur_time = end - start
print("\n CUR runtime is: ", cur_time)

start = time.time()
CUR.cur(data.M.todense(),90)
end = time.time()
curret_time = end - start
print("\n CUR retained energy runtime is: ", curret_time)

start = time.time()
collaborative.item_item_collab()
end = time.time()
collab_time = end - start
print("\n Collaborative ranking runtime is: ", collab_time)

start = time.time()
collaborative.item_item_base()
end = time.time()
collabbase_time = end - start
print("\n Collaborative baseline ranking runtime is: ", collabbase_time)

