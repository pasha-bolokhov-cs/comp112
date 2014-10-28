#!/usr/bin/env python
#encoding: utf-8

import math, sys


#
# xrange() is replaced by range() in Python 3
#
if (sys.hexversion >= 0x300000):
    def xrange(stop):
        return range(stop)

    

def fib(n):
    """
    Fibonacci
    """

    prev = 0
    curr = 1

    # won't work in python3
    for k in xrange(n-1):
        prev, curr = curr, curr + prev

    return curr




def mergesort(L1, L2):
    """
    Merge Sort algorithm
    Assume that the lists are sorted
    """
    res = []
    h1 = 0
    h2 = 0
    l1 = len(L1)
    l2 = len(L2)

    # run until one of the pointers hits the end
    while (h1 < l1) and (h2 < l2):
        if (L1[h1] <= L2[h2]):
            res.append(L1[h1])
            h1 += 1
        else:
            res.append(L2[h2])
            h2 += 1
    
    # check if one of the lists wasn't completed
    if (h1 < l1):
        res.extend(L1[h1:])
    elif (h2 < l2):
        res.extend(L2[h2:])

    return res




def triangle(h):
    """
    Print a triangle of height 'h'
    """

    if (h <= 0):
        return

    for k in xrange(h):
        # print 'k + 1' asterisks
        for m in xrange(k + 1):
            print "*",
        
        # do the linefeed
        print




def Q4(l, w):
    """
    Question 4
    """
    return l * w




def Q5(h, b):
    """
    Question 5
    """
    return h * b / 2.




def Q6(a, b):
    """
    Question 6
    """
    return math.sqrt(a * a  +  b * b)




def Q7(r):
    """
    Question 7
    """
    return 2. * math.pi * r




def Q8(r):
    """
    Question 8
    """
    return math.pi * r * r




def main():
    """
    Main function
    """
    #
    # map of functions, number and types of their arguments,
    # and output formats for its return values
    #
    targs = {"q1":  [fib,        [int],                        ["!"]],
             "q2":  [mergesort,  [list, list],                 ["!"]],
             "q3":  [triangle,   [int],                        []],
             "q4":  [Q4,         [float, float],               ["!"]],
             "q5":  [Q5,         [float, float],               ["!"]],
             "q6":  [Q6,         [float, float],               ["!"]],
             "q7":  [Q7,         [float],                      ["!"]],
             "q8":  [Q8,         [float],                      ["!"]]};

    # get a function name from 'argv'
    if len(sys.argv) - 1 == 0:
        sys.stderr.write("Need to supply a question, e.g. \"q1\", \"q2\", ...\n")
        exit(1)
    request = sys.argv[1]

    if request not in targs:
        sys.stderr.write("Unrecognized function: `%s'\n" % request)
        exit(1)

    # find the function and its arguments
    quest = targs[request][0]
    types = targs[request][1]
    nargs = len(types)
    formats = targs[request][2]
    nres = len(formats)
    args = []

    # get the input and convert if necessary
    for a in types:
        value = input()
        args.append(a(value))
    
    # call the actual function
    returns = quest(*args)

    #
    # if a function returns a single value
    # we convert it to a list anyway
    #
    if type(returns) != type(()):
        results = [returns]
    else:
        results = list(returns)

    # print out all results in the correct format
    for r in xrange(len(formats)):
        if formats[r] == "!":
            print(results[r])                         # no formatting is needed
        else:
            print(formats[r] % results[r])




#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

