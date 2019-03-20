#!/bin/python3

import math
import os
import random
import re
import sys


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp



# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ''' Final Solution based on enumarated array '''

    annotated = [*enumerate(arr)]
    annotated.sort(key = lambda it: it[1])
    count = 0
    i = 0
    while i < len(arr):
        if annotated[i][0] == i:
            i += 1
            continue
        swap(annotated, i, annotated[i][0])
        count += 1

    return count
        

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

