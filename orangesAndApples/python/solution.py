#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):

    apples_position = [(apple + a) for apple in apples]
    apples_position.sort()

    oranges_position = [(orange + b) for orange in oranges]
    oranges_position.sort()

    oranges_in_house = [orange for orange in oranges_position if orange >= s and orange <= t]
    apples_in_house = [apple for apple in apples_position if apple >= s and apple <= t]

    print(len(apples_in_house))
    print(len(oranges_in_house))
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
