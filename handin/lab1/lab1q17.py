#!/usr/bin/env python

import math

P = int(raw_input())

R = float(raw_input())
R = R / 12.

t = int(raw_input())
T = float(t) * 12.

print "%.2f"  %  ( ( P * R * math.pow(1 + R, T) ) / ( math.pow(1 + R, T) - 1 ) )
