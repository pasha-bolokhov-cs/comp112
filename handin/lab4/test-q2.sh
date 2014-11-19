#!/usr/bin/env sh

for n in $(cat primes-1000); do echo $n | ./lab4.py q2; done | grep -v True

