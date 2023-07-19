# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:53:22 2019

@author: sukrit
"""

m = [[22,45,3,5],
     [66,8,88,34],
     [99,3,8,84],
     [2,1,2,23]]

for i in range(0,len(m),2):
    for j in range(0,len(m[i]),2):
        print(i,j)
        max_ = m[i][j]
        min_ = m[i][j]
        sum_ = 0
        for ii in range(i,i+2):
            for jj in range(j,j+2):
                print(m[ii][jj])
                if m[ii][jj] > max_:
                    max_ = m[ii][jj]
                if m[ii][jj] < min_:
                    min_ = m[ii][jj]
                sum_ += m[ii][jj]  
        print(max_,min_,sum_)
        print("----")
        
        
sums = [0,0,0,0]
for i in range(len(m)):
    for j in range(len(m[i])):
        sums[j] += m[i][j]
        
print(sums)
        
