#!/usr/bin/env sh

./lab5.py book.csv book.python.actual
diff book.expect book.python.actual

./lab5.pl book.csv book.perl.actual
diff book.expect book.perl.actual
