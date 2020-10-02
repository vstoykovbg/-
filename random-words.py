#!/usr/bin/python3

import random
import sys

filename = "популярни-думи.txt"

if len(sys.argv) > 2:
    print("Too many arguments.")
    quit()
elif len(sys.argv) == 2:
    filename = sys.argv[1]


with open(filename) as f:
    mywordlist = [line.rstrip() for line in f]

secure_random = random.SystemRandom()

for counter in range(20):
    print (secure_random.choice(mywordlist))



