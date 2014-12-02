#!/usr/bin/env sh

./lab5.py book.csv book.actual
diff book.expect book.actual

./lab5.pl book.csv book.perl.actual
diff book.expect book.perl.actual
