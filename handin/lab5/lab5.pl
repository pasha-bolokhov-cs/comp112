#!/usr/bin/env perl
#


die "format: %0 <in-file> <out-file>\n" if ($#ARGV - 1 <= 2);

open(my $fin, "<", $ARGV[0]) ||
    die "$0: can't open \`$ARGV[0]\': $!\n";



