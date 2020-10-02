#!/usr/bin/python3


with open('50-хиляди-популярни-думи.txt') as f:
    list1 = [line.rstrip() for line in f]

with open('думи-без-имена-над-4-букви.txt') as f:
    list2 = [line.rstrip() for line in f]

intersection = list(set(list1).intersection(list2))

print(*intersection, sep = "\n") 


