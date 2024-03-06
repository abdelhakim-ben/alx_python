#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number>0 :
    print("{} is positve".format(number))
elif number<0 :
    print("{} is negetive".format(number))
else:
    print("{} is Zero".format(number))