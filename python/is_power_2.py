#!/usr/bin/python
#
# is_power_2.py
#
# Write a function to return true if its integer argument is a power of 2, false otherwise.

for integer in range(1, 100):
    if not integer & (integer - 1):
        print str(integer) + "\tpower of 2"
    else:
        print str(integer) + "\tnot power of 2: "
