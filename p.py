#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    arr_limit = 4
    hg_list   = []
    sumz      = []
    x         = 0
    y         = 1
    z         = 2
    for u in range(0,arr_limit):
        i = 0
        j = 1
        k = 2
        for n in range(0,arr_limit):
            hg_list.append([
                [
                arr[x][i],
                arr[x][j],
                arr[x][k]] 
                ,[
                arr[y][j]] 
                ,[arr[z][i],arr[z][j],arr[z][k]]])
            sumz.append(arr[x][i]+arr[x][j]+arr[x][k]+arr[y][j]+arr[z][i]+arr[z][j]+arr[z][k])
            i+=1
            j+=1
            k+=1
        x+=1
        y+=1
        z+=1

    return max(sumz)
    

        

if __name__ == '__main__':
    print(hourglassSum([
        [1, 1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0], 
        [1, 1, 1, 0, 0, 0], 
        [0, 0, 2, 4, 4, 0], 
        [0, 0, 0, 2, 0, 0], 
        [0, 0, 1, 2, 4, 0]]))
