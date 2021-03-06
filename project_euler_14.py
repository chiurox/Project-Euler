#!/usr/bin/env python

import sys
import timeit

# PROJECT EULER
# PROBLEM 14:

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 10 terms.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting
# numbers finish at 1.

# Which starting number, under one million, produces the largest chain?

def longest_chain(n):
    longest_chain = 0
    counter = 0
    number_chainlength = {}
    temp_sequence_length = 0

    for i in range(2, int(n)):
        number = i
        counter += 1
        while number != 1:
            if number in number_chainlength:
                temp_sequence_length = number_chainlength[number] - 1
                break
            if number % 2 == 0:
                number = number/2
            else:
                number = 3*number + 1
            counter += 1
        number_chainlength[i] = counter + temp_sequence_length
        temp_sequence_length = 0

        if longest_chain < number_chainlength[i]:
            longest_chain = number_chainlength[i]
            largest_starting_number = i
        counter = 0

    print "Under %s," % n
    print "the largest starting number is: %s" % largest_starting_number
    print "with longest chain of: %s" % number_chainlength[largest_starting_number]
    return

if (__name__ == "__main__"):
    try:
        t = timeit.Timer(setup='from __main__ import longest_chain', stmt='longest_chain(sys.argv[1])')
        print t.timeit(1)
    except:
        print 'Usage: python file_name.py <n>'
    # My solution takes 3 seconds to compute the solution to this problem (number under 1 million)
    # On a Core 2 Duo 2.0GHz Asus Laptop
    # On a MacBook Retina 15 i7, it takes ~1.8s
