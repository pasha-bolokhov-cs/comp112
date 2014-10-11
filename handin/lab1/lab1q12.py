#!/usr/bin/env python
#encoding: utf-8


def main():

    s = float(raw_input())
    e = float(raw_input())
    
    sf = float(raw_input())
    ef = float(raw_input())
    
    print (sf - ef) / (e - s)


#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

