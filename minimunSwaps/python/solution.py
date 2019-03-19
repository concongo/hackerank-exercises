#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    swapped = False
    i = 0
    k = 0

    while i < len(arr):
        while k < len(arr) and not swapped:

            if arr[i] > arr[k]:
                f = arr[i]
                s = arr[k]
                for l in range(k, len(arr)):
                    if arr[l] < s:
                        s = arr[l]
                        k = l
                arr[i] = s
                arr[k] = f
                swaps = swaps + 1
                swapped = True
            else:
                k = k + 1
        if not swapped:
            i = i + 1
            k = i
        else:
            i = 0
            k = 0
            swapped = False

    return swaps
        

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

