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

    # Check if we have proper arguments
    if (len(sys.argv) - 1 < 2):
        sys.stderr.write("format: %s <in-file> <out-file>\n" % sys.argv[0])
        exit(1)

    # Open input and output files
    try:
        fin = open(sys.argv[1], "r")
    except IOError as e:
        sys.stderr.write("can't open `%s': %s\n" % (sys.argv[1], e.strerror))
        exit(2)
    try:
        fout = open(sys.argv[2], "w")
    except IOError as e:
        sys.stderr.write("can't open `%s': %s\n" % (sys.argv[2], e.strerror))
        exit(2)

    # Process the input file
    for line in fin:
        sys.stdout.write(line)


    # Close the files
    fout.close()
    fin.close()


#
# Call main() if the program is not being used as a module
#
if (__name__ == "__main__"):
    main()

