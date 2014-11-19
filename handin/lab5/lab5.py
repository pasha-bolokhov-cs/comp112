#!/usr/bin/env python
#encoding: utf-8

import sys


#
# xrange() is replaced by range() in Python 3
#
if (sys.hexversion >= 0x300000):
    def xrange(stop):
        return range(stop)



def main():
    """
    Main function
    """
    #
    # map of functions, number and types of their arguments,
    # and output formats for its return values
    #
    targs = {"q1":  [timediff,   [int, int],                   ["!"]],
             "q2":  [is_prime,   [int],                        ["!"]],
             "q3":  [is_perfect, [int],                        ["!"]]};

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
        value = sys.stdin.readline().rstrip('\n')
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
            sys.stdout.write(str(results[r]) + "\n")               # no formatting is needed
        else:
            sys.stdout.write(str(formats[r] % results[r]) + "\n")




#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

