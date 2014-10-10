#!/usr/bin/env python

sg = float(raw_input())
eg = float(raw_input())

days = int(raw_input())

print "%.2f" % (  ((eg - sg) * 0.01433  +  days * 0.0902) * 1.05  )

