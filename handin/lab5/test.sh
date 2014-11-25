#!/usr/bin/env sh

./lab5.py book.csv book.actual
diff book.expect book.actual
