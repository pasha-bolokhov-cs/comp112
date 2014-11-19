#!/usr/bin/env sh

for n in $(cat test-q2.primes); do echo $n | ./lab4.py q2; done | grep -v True

