#!/usr/bin/env sh

for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17; do 
    for k in in${q}_*; do
	out=out${q}_${k##*_}.actual
	./lab1q${q}.py < $k > $out
	diff ${out%%.actual}.expect $out >/dev/null ||
	{ echo "'diff ${out%%.actual}.expect $out' failed" 1>&2; exit 1; }
    done
done



