#!/usr/bin/env python
#encoding: utf-8

def main():
    
    F = float(raw_input())
    
    C = ( F  -  32. ) * 5. / 9.
    
    print C


#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

