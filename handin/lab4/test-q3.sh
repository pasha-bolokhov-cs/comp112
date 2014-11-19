#!/usr/bin/env sh

for n in $(cat test-q3.deficient); do echo $n | ./lab4.py q3; done | grep -v deficient
for n in $(cat test-q3.perfect); do echo $n | ./lab4.py q3; done | grep -v perfect
for n in $(cat test-q3.abundant); do echo $n | ./lab4.py q3; done | grep -v abundant

