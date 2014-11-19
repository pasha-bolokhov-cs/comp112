#!/usr/bin/env sh

cat test-q1.data | 
while :; do
	read t1 t2 d
	code=$?
	if [ "x$code" != "x0" ]; then
		exit
	fi
	res=$( { echo "${t1}"; echo "${t2}"; } | ./lab4.py q1)
	if [ "x$res" != "x$d" ]; then
		echo "Mismatch: $t1 $t2 expect $d actual $res" 1>&2
	fi
done

