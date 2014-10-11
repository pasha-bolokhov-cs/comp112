#!/usr/bin/env python
#encoding: utf-8


def main():
    
    h = float(raw_input())
    w = float(raw_input())
    index = w / ( h * h )
    
    print "%.1f"   %   index


#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

