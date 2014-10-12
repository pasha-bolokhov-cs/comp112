#!/usr/bin/env python
#encoding: utf-8


def main():
    
    sg = float(input())
    eg = float(input())
    
    days = int(input())
    
    print "%.2f" % (  ((eg - sg) * 0.01433  +  days * 0.0902) * 1.05  )


#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

