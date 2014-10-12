#!/usr/bin/env python
#encoding: utf-8

import math


def main():

    P = int(input())
    
    R = float(input())
    R = R / 12.
    
    t = int(input())
    T = float(t) * 12.
    
    print "%.2f"  %  ( ( P * R * math.pow(1 + R, T) ) / ( math.pow(1 + R, T) - 1 ) )


#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

