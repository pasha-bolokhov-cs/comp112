#!/usr/bin/env python
#encoding: utf-8

import math, sys


#
# xrange() is replaced by range() in Python 3
#
if (sys.hexversion >= 0x300000):
    def xrange(stop):
        return range(stop)

    


def timediff(t1, t2):
    """
    Time difference
    """

    # 
    # First time is always before the second time,
    # check if need to switch to the next day
    #
    if (t2 <= t1):
        t2 += 2400

    # Extract minutes and hours from each time
    h1 = t1 / 100
    h2 = t2 / 100
    m1 = t1 % 100
    m2 = t2 % 100

    # Calculate the difference
    dh = h2 - h1
    dm = m2 - m1

    # Wrap the hour if needed
    if (dm < 0):
        dh -= 1
        dm += 60

    return "%d:%02d" % (dh, dm)




def divisible(n, d):
    """
    Determines if 'n' is divisible by 'd'
    """

    return ((n / d) * d == n)




def is_prime(n):
    """
    Determines if 'n' is a prime number
    """

    # Initial small numbers
    if (n in [1, 4, 6, 8, 9, 10]):
        return False
    if (n in [2, 3, 5, 7]):
        return True

    # Calculate the square root
    s = int(round(math.sqrt(float(n))))

    #
    # 'xrange' runs from '0' to 's-1'
    # the divisors range from '2' to '\sqrt{n} + 1'
    #
    for d in xrange(s):
        if (divisible(n, d + 2)):
            return False

    return True




def is_perfect(n):
    """
    Determines whether 'n' is a "perfect", "abundant" or a "deficient" number
    """

    # Initial small numbers
    if (n in [1, 2, 3, 4, 5]):
        return "deficient"

    sum = 0
    for d in xrange(n - 1):
        # 'd + 1' ranges from '1' to 'n - 1'
        if (divisible(n, d + 1)):
            sum += d + 1

    if (sum > n):
        return "abundant"
    if (sum == n):
        return "perfect"
    if (sum < n):
        return "deficient"




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

