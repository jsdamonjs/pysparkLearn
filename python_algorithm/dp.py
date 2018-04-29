# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 19:48:33 2018

@author: lenovo
"""

def convert_a_to_b(a,b):
    len_a = len(a)
    len_b = len(b)
    d = [[0 for j in range(len_b+1)] for i in range(len_a+1)]
    for i in range(0,len_a+1):
        d[i][0] = i
    for j in range(0,len_b+1):
        d[0][j] = j
    for i in range(1,len_a+1):
        for j in range(1,len_b+1):
            if a[i-1] == b[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                insert_step = d[i][j-1]+1
                delete_step = d[i-1][j]+1
                replace_step = d[i-1][j-1]+1
                d[i][j] = min(min(insert_step,delete_step),replace_step)
    return d[len_a][len_b]

a = 'a'
b = 'b'
res = convert_a_to_b(a,b)
print (res)

def bag_0_1(volume,val_list,weight_list):
    num = len(val_list)
    d = [[0 for i in range(volume+1)] for j in range(num)]
    for i in range(num):
        d[i][0] = 0
    for i in range(volume+1):
        d[0][i] = val_list[0] if i >= weight_list[0] else 0
    for i in range(1,num):
        for j in range(1,volume+1):
            if weight_list[i] > j:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j],d[i-1][j-weight_list[i]]+val_list[i])
    return d[num-1][volume]

def bag_all(volume,val_list,weight_list):
    num = len(val_list)
    d = [[0 for i in range(volume+1)] for j in range(num)]
    for i in range(num):
        d[i][0] = 0
    for i in range(volume+1):
        d[0][i] = (i//weight_list[0])*val_list[0] if i >= weight_list[0] else 0
    for i in range(1,num):
        for j in range(1,volume+1):
            if weight_list[i] > j:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j],d[i][j-weight_list[i]]+val_list[i])
    return d[num-1][volume]
def bag_many(volume,val_list,weight_list,number_list):
    num = len(val_list)
    d = [[0 for i in range(volume+1)] for j in range(num)]
    for i in range(num):
        d[i][0] = 0
    for i in range(volume+1):
        count = min(number_list[0],i//weight_list[0])
        d[0][i] = count*val_list[0] if i >= weight_list[0] else 0
    for i in range(1,num):
        for j in range(1,volume+1):
            if weight_list[i] > j:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = d[i-1][j]
                count = min(number_list[i],j//weight_list[i])
                for k in range(0,count+1):
                    temp = max(d[i-1][j],d[i-1][j-weight_list[i]*k]+k*val_list[i])
                    if temp > d[i][j]:
                        d[i][j] = temp
    return d[num-1][volume]
value = [ 2 , 5 , 3 , 10 , 4]
weight = [ 1 , 3 , 2 , 6 , 2]
number = [1,1,1,1,10]
content = 12
res = bag_many(content,value,weight,number)
print (res)

def max(a,b):
    if a > b:
	return a
    else:
	return b   
