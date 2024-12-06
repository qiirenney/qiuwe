# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:32:36 2024

@author: Qirana
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# List awal
arr = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
print(f"List Sebelum Disorting: {arr}")

# Sorting list
bubble_sort(arr)
print(f"List Yang Sudah Disorting: {arr}")
