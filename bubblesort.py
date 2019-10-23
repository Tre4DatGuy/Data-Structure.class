# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Raymond Mitchell
#Objective:Implement a Sort Algorithm
#October 23, 2019
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[12, 200, 45, 1, 57, 23]
shortBubbleSort(alist)
print(alist


























