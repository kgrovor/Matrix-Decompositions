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
import errors
import data

start = time.time()
U,sigma,V,Y=SVD.svd_retained_energy(data.M.todense(),1)
end = time.time()
svd_time = end - start
print("SVD")
errors.calc_error(Y)
print("Runtime: ", svd_time," s")
print("\n\n")

start = time.time()
U,sigma,V,Y=SVD.svd_retained_energy(data.M.todense(),0.9)
end = time.time()
svdret_time = end - start
print("SVD with 90% retained energy")
errors.calc_error(Y)
print("Runtime: ", svd_time," s")
print("\n\n")

start = time.time()
C,U,R,Y=CUR.cur_without_repeat(data.M.todense(),1)
end = time.time()
cur_time = end - start
print("CUR without repetition")
errors.calc_error(Y)
print("Runtime: ", cur_time," s")
print("\n\n")

start = time.time()
C,U,R,Y=CUR.cur_with_repeat(data.M.todense(),90)
end = time.time()
curret_time = end - start
print("CUR with repetition")
errors.calc_error(Y)
print("Runtime: ", curret_time," s")
print("\n\n")

start = time.time()
Y=collaborative.user_user_collab()
end = time.time()
collab_time = end - start
print("User - User Collaborative")
errors.calc_error(Y)
print("Runtime: ", collab_time," s")
print("\n\n")

start = time.time()
Y=collaborative.item_item_collab()
end = time.time()
collab_time = end - start
print("Collaborative")
errors.calc_error(Y)
print("Runtime: ", collab_time," s")
print("\n\n")

#start = time.time()
#Y=collaborative.user_user_base()
#end = time.time()
#collabbase_time = end - start
#print("User - User Collaborative with Baseline Approach")
#errors.calc_error(Y)
#print("Runtime: ", collabbase_time," s")
#print("\n\n")

start = time.time()
Y=collaborative.item_item_base()
end = time.time()
collabbase_time = end - start
print("Collaborative with Baseline Approach")
errors.calc_error(Y)
print("Runtime: ", collabbase_time," s")

