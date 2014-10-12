#!/usr/bin/env sh

>out.actual

for q in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17; do 
	for k in in${q}_*; do
		./lab1q${q}.py < $k >> out.actual
	done
done
diff out.expect out.actual


