# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 18:07:21 2018

@author: damon
"""

#select sort
def select_smallest(list):
    length = len(list)
    smallest = list[0]
    smallest_index = 0
    for i in range(1,length):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index
def select_sort(list):
    res = []
    for i in range(len(list)):
        res.append(list.pop(select_smallest(list)))
    return res

a = [1,23,2,100,1,1,2,3,4,5]
res = select_sort(a)
print(res)

#bubble_sort
def bubble_sort(list):
    length = len(list)
    for i in range(0,length):
        replace = 0
        for j in range(0,length-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                replace = 1
        if replace == 0:
            return list
    return list
a = [1,23,2,100,1,1,2,3,4,5]
res = bubble_sort(a)
print(res)
#quick_sort
def quick_sort(list,start,end):
    if start < end:
        i,j = start,end
        pivot = list[i]
        while i < j:
            while i<j and list[j] >= pivot:
                j -= 1
            list[i] = list[j]
            while i<j and list[i] <= pivot:
                i +=1
            list[j] = list[i]
        list[i] = pivot
        quick_sort(list,start,i-1)
        quick_sort(list,i+1,end)
    return list
a = [1,23,2,100,1,1,2,3,4,5]
res = quick_sort(a,0,len(a)-1)
print(res)   
#bucket_sort
def bucket_sort(list):
    max_num = max(list)
    bucket_list = [0 for i in range(max_num+1)]
    res = []
    for i in list:
        bucket_list[i]+=1
    for i in range(0,max_num+1):
        if bucket_list[i] !=0:
            for j in range(0,bucket_list[i]):
                res.append(i)
    return res
a = [1,23,2,100,1,1,2,3,4,5]
res = bucket_sort(a)
print(res)
#merge_sort
def merge(a,b):
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            res.append(a.pop(0))
        elif a[0] > b[0]:
            res.append(b.pop(0))
    if len(a) > 0:
        res+=a
    elif len(b) > 0:
        res+=b
    return res  
def merge_sort(list):
    if len(list) == 1:
        return list
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    list = merge(left,right)
    return list
a = [1,23,2,100,1,1,2,3,4,5]
res = merge_sort(a)
print(res)
#insert_sort
def insert_sort(list):
    length = len(list)
    for i in range(1,length):
        if list[i] < list[i-1]:
            position = i
            cur_val = list[i]
            while position > 0 and list[position-1] > cur_val:
                list[position] = list[position-1]
                position-=1
            list[position] = cur_val
    return list
a = [1,23,2,100,1,1,2,3,4,5]
res = insert_sort(a)
print(res)
#shell sort
def shell_sort(list):
    d_s = len(list)//2
    while d_s >= 1:
        for i  in range(d_s,len(list)):
            position  = i
            cur_val = list[position]
            index = i%d_s
            while position > index and list[position-d_s] > cur_val:
                list[position] = list[position-d_s]
                position-=d_s
            list[position] = cur_val
        d_s = d_s//2
    return list
a = [1,23,2,100,1,1,2,3,4,5]
res = shell_sort(a)
print(res)

#heap sort
def adjust_heap(list,i,size):
    max = i
    lchild = 2*i+1
    rchild = 2*i+2
    if i < size:
        if lchild < size and list[lchild] > list[max]:
            max = lchild
        if rchild < size and list[rchild] > list[max]:
            max = rchild
        if max != i:
            list[max],list[i] = list[i],list[max]
            adjust_heap(list,max,size)
            
def build_heap(list,size):
    for i in range(size//2-1,-1,-1):
        adjust_heap(list,i,size)
def heap_sort(list):
    size = len(list)
    build_heap(list,size)
    for i in range(size-1,-1,-1):
        list[0],list[i] = list[i],list[0]
        adjust_heap(list,0,i)
    return list
a = [1,23,2,100,1,1,2,3,4,5]
res = heap_sort(a)
print(res)



                
                








