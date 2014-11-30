#!/usr/bin/env perl
#

# Check if we have proper arguments
die "format: %0 <in-file> <out-file>\n" if ($#ARGV + 1 < 2);

# Open input and output files
open(my $fin, "<", $ARGV[0]) ||
    die "$0: can't open \`$ARGV[0]\': $!\n";
open(my $fout, ">", $ARGV[1]) ||
    die "$0: can't open \`$ARGV[1]\': $!\n";

# Process the input file
my %records;
my %maxlengths;
while (<$fin>) {
    my %rec;
    chomp;
    @fields = split /,/;
    foreach $f (@fields) {
	# split each field into 'name' and 'value'
	@assign = split /=/, $f;
	$name = $assign[0];
	$value = $assign[1];

	# update the maximum length
	if ((!exists(maxlengths{$name})) || (length($name) > maxlengths{$name}))
	    maxlengths{$name} = length($name);
	if (length($value) > maxlengths{$name})
	    maxlengths{$value} = length($value);

	# check if found the name assignment
	if ($name eq "name") 
	    $line_name = $value;
	else
	    $rec{$name} = $value;
    }

    # update the dictionary
    if (exists(records{$line_name}))
	die "name \`$line_name\' occurs more than once\n";

    $records{$line_name} = %rec;
} # while (<$fin>)

# Close the input file
close($fin) || 
    die "$0: can't close \`$ARGV[1]\': $!\n";

# Sort the field names
$sorted_fields = sort(keys(%maxlengths));



