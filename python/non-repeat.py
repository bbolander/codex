#!/usr/bin/python
#
#   Find the first non-repeating character in a string.
#
#
###############################################################################

import operator

s1 = 'abcdefghijklmnopqrstuvwxyz'   # No repeating characters.
s2 = 'aaaaaaaaaaaaaaaaaaaaaaaaaa'   # Only repeating characters.
s3 = 'aaaaaaaaaaaaaaaaazaaaaaaaa'   # One non-repeating character
s4 = 'aaaakaaaabbaaaaaazaaaaaaaa'   # Two non-repeating character
s5 = 'aaaaaaaaaaaaaaaaaaaaaaaaak'   # One non-repeating character at the end.
s6 = 'kaaaaaaaaaaaaaaaaaaaaaaaaa'   # One non-repeating character at the beginning.
s7 = 'kaaaaaaaaaaaaaaaaaakaaaaaa'   # One repitition non-consecutive, no non-repeats

def nonrepeat(string):
    chars = dict()      # Count of each individual character. Character is key count is value.

    index = 0

    for c in string:
        if chars.has_key(c):
            chars[c] += 1
        else:
            chars[c] = 1

    #for c in chars:
    #    print c + ": " + str(chars[c]),

    #print

    for c in string:
        if chars[c] == 1:
            return c

    return "No non-repeating characters"

def nonrepeat2(string):
    chars = dict()      # Character is key value is an array [count, index]

    index = 0

    for c in string:
        if chars.has_key(c):
            chars[c][0] += 1
        else:
            chars[c] = [1, index]

        index += 1

    #for c in chars:
    #   print c + ": " + str(chars[c]),

    #print "chars.items(): " + str(chars.items())

    sorted_chars = sorted(chars.items(), key=operator.itemgetter(1))

    #if sorted_chars != None:
    #    print "Sorted chars: " + str(sorted_chars)

    if sorted_chars[0][1][0] == 1:
        return sorted_chars[0][0]
    else:
        return "No non-repeating characters"

print "First non-repeat in " + s1 + " is " + nonrepeat(s1)
print "First non-repeat in " + s2 + " is " + nonrepeat(s2)
print "First non-repeat in " + s3 + " is " + nonrepeat(s3)
print "First non-repeat in " + s4 + " is " + nonrepeat(s4)
print "First non-repeat in " + s5 + " is " + nonrepeat(s5)
print "First non-repeat in " + s6 + " is " + nonrepeat(s6)
print "First non-repeat in " + s7 + " is " + nonrepeat(s7)
print
print "nonrepeat2"
print "First non-repeat in " + s1 + " is " + nonrepeat2(s1)
print "First non-repeat in " + s2 + " is " + nonrepeat2(s2)
print "First non-repeat in " + s3 + " is " + nonrepeat2(s3)
print "First non-repeat in " + s4 + " is " + nonrepeat2(s4)
print "First non-repeat in " + s5 + " is " + nonrepeat2(s5)
print "First non-repeat in " + s6 + " is " + nonrepeat2(s6)
print "First non-repeat in " + s7 + " is " + nonrepeat2(s7)