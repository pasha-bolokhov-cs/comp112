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




def Q2(F):
    """
    Question 2
    """
    C = ( F  -  32. ) * 5. / 9.
    
    return C




def Q3(s):
    """
    Question 3
    """
    return s * s




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
    targs = {"q1":  [fib, [int],                        ["!"]],
             "q2":  [Q2,  [float],                      ["!"]],
             "q3":  [Q3,  [float],                      ["!"]],
             "q4":  [Q4,  [float, float],               ["!"]],
             "q5":  [Q5,  [float, float],               ["!"]],
             "q6":  [Q6,  [float, float],               ["!"]],
             "q7":  [Q7,  [float],                      ["!"]],
             "q8":  [Q8,  [float],                      ["!"]]};

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
    
    # make a list
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

