import random as rand
import numpy as np
import time



array = [int(15*rand.random()) for i in range(5)]

def merge_sort(A):
    if len(A) <= 1: return A
    
    middle = len(A)//2
    
    left = merge_sort(A[:middle])
    right = merge_sort(A[middle:])
    
    return merge(left, right)


def merge(A, B):
    a = 0
    b = 0
    
    C = []
    
    while (a < len(A)) and (b < len(B)):
        if A[a] < B[b]:
            C.append(A[a])
            a += 1
        else:
            C.append(B[b])
            b += 1
            
       
    while a < len(A):
        C.append(A[a])
        a += 1
        
    while b < len(B):
        C.append(B[b])
        b += 1
                        
    return C



def selection_sort(arr):
    for i in range(len(arr)):    
        min_idx = i
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        first = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = first
       
    return arr



def insertion_sort2(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                small = arr[i]
                for k in range(i, j, -1):
                    arr[k] = arr[k-1]
                arr[j] = small
                break
                    
    return arr



def insertion_sort(arr):
    for i in range(1, len(arr)):
        item = arr[i]
        j = i-1
        while j>=0 and (item < arr[j]):
            arr[j+1] = arr[j]
            j-=1
            
        arr[j+1] = item
            
    return arr
    

    
def test(arr):
    start = time.perf_counter()
    a1 = merge_sort(arr.copy())
    print((time.perf_counter()-start)*(1e5))
    
    
    start = time.perf_counter()
    a2 = selection_sort(arr.copy())
    print((time.perf_counter()-start)*(1e5))
    assert len(a1) == len(a2)
    
    for s in zip(a1, a2):
        assert s[0] == s[1]
        

    start = time.perf_counter()
    a2 = insertion_sort(arr.copy())
    print((time.perf_counter()-start)*(1e5))
    assert len(a1) == len(a2)
    
    for s in zip(a1, a2):
        assert s[0] == s[1]        


    return True



test(array)