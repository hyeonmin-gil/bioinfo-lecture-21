#!/usr/bin/python3

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

min_val = l[0]
max_val = l[0]

for i in l :
    if i > max_val:
        max_val = i
