#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min_count, max_count = 0, 0
    min_val, max_val = scores[0], scores[0]

    for i in range(len(scores)):
        if scores[i] < min_val:
            min_val = scores[i]
            min_count += 1
        if scores[i] > max_val:
            max_val = scores[i]
            max_count += 1

    return max_count, min_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
