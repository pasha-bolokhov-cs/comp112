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
my $line_name;
while (<$fin>) {
    my %rec;
    chomp;
    @fields = split /,/;
    foreach $f (@fields) {
	# split each field into 'name' and 'value'
	@assign = split /=/, $f;
	$name = $assign[0];
	$name =~ s/^\s+|\s+$//g;
	$value = $assign[1];
	$value =~ s/^\s+|\s+$//g;

	# update the maximum length
	if ((!exists $maxlengths{$name}) || (length($name) > $maxlengths{$name})) {
	    $maxlengths{$name} = length($name);
	}
	if (length($value) > $maxlengths{$name}) {
	    $maxlengths{$name} = length($value);
	}

	# check if found the name assignment
	if ($name eq "name") {
	    $line_name = $value;
	} else {
	    $rec{$name} = $value;
	}
    }

    # update the dictionary
    if (exists $records{$line_name}) {
	die "name \`$line_name\' occurs more than once\n";
    }

    $records{$line_name} = %rec;
} # while (<$fin>)

# Close the input file
close($fin) || 
    die "$0: can't close \`$ARGV[0]\': $!\n";

# Sort the field names
@sorted_fields = sort(keys(%maxlengths));

# Print the header
$line = sprintf("%" . $maxlengths{"name"} . "s  ", "name");

foreach $n (@sorted_fields) {
    if (($n ne "name") && ($n ne "address")) {
	$line .= sprintf("%" . $maxlengths{$n} . "s  ", $n);
    }
}
$line .= sprintf("%" . $maxlengths{"address"} . "s\n", "address");
print $line;

# Sort the dictionary
@sorted_records = sort(keys(%records));
foreach $name (@sorted_records) {
    $line = sprintf("%" . $maxlengths{"name"} . "s  ", $name);
    foreach $f (@sorted_fields) {
	if (($f ne "name") && ($f ne "address")) {
	    print "checking record $f for name $name: $records{$name}{$f}\n";
	    $line .= sprintf("%" . $maxlengths{$f} . "s  ",
			     (exists $records{$name}{$f}) ?
			      $records{$name}{$f} : "");
	}
    }

    # address may not be present
    $line .= sprintf("%" . $maxlengths{"address"} . "s\n",
		     (exists $records{$name}{"address"}) ?
		     $records{$name}{"address"} : "");

    print $line;
}

# Close the output file
close($fout) || 
    die "$0: can't close \`$ARGV[1]\': $!\n";
