#!/usr/bin/env sh

Q="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17"

for q in ${Q}; do

    cat <<EOF




"""
Question ${q}
"""

def Q${q}():
EOF

    cat lab1q${q}.py | sed '0,/^def main/ d' | sed '/^# *$/,$ d'
done

