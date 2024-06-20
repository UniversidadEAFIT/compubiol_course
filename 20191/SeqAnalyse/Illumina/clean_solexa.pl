#!/usr/bin/perl 
#===============================================================================
#         FILE:  clean_solexa_se.pl
#  DESCRIPTION: run clean_solexa_se.pl -h or perldoc
#
#      OPTIONS: run clean_solexa_se.pl -h or perldoc
#       AUTHOR:  Gustavo Gilson Lacerda Costa, glacerda@lge.ibi.unicamp.br
#      COMPANY:  State University of Campinas, Institute of Biology, Laboratory of Genomics and Expression
#      VERSION:  1.0
#      CREATED:  02/19/2010 15:28:52 AM
#===============================================================================
use strict;
use warnings;
use Getopt::Long qw(:config no_ignore_case bundling);
use Pod::Usage;


my $file="";
my $nfilter=1;
my $minqual=0;
my $trimbegin=0;
my $trimend=0;
my $prefix = "out";
my $verbose=1;
my $help=0;

my $result = GetOptions(
	"file|f=s" => \$file, #file containing both mates interleaved (if used, file1 and file2 are ignored)
	"nfilter|n!" => \$nfilter, #Discard both mates when one (or both) of them have at least one N in the sequence
	"minqualitythreshold|q:f" => \$minqual, #Discard both mates when one (or both) of them have average quality less than minqualthreshold
	"trimbegin|b:i" => \$trimbegin, #if used, all reads are trimmed starting at trimbegin position
	"trimend|e:i" => \$trimend, #if used, all reads are trimmed ending at trimend position
        "prefix|p:s" => \$prefix, #prefix to output files (Default: out)
	"verbose|v!"   => \$verbose,   #toggles verbosity
        "help|h!"      => \$help       #displays help
)  or pod2usage( -verbose => 2, -output => ">&STDOUT" ) && exit;

if ($help) {
	pod2usage( -verbose => 2, -output => ">&STDOUT" ) && exit;
}

my $mode=paramOk();

if ( !$mode ) {
	pod2usage( -verbose => 2, -output => ">&STDOUT" ) && exit;
} else {
	open(F,"<$file") || die "Could not open $file\n";
}

open(S,">$prefix.single");
open(D,">$prefix.discarded");
my $count=0;

while (my ($hs1,$s1,$hq1,$q1) = getRead($mode)) {
	if ($verbose) {
		$count++;
		if (($count%1000000)==0) {
			print STDERR "Processed $count reads...\n";
		}
	}
        if (($trimbegin)||($trimend)) {
                chomp $s1; 
                chomp $q1;
                my $len=length $s1;

                if ($trimbegin<1) { $trimbegin = 1 }
                if ($trimend > $len) { $trimend = $len }

                my $start = $trimbegin - 1;
                my $end = $trimend - $trimbegin + 1;
                $s1 = substr($s1, $start, $end) . "\n";
                $q1 = substr($q1, $start, $end) . "\n";
        }

	my ($mate1_nfilter_ok,$mate1_qualfilter_ok,$mate1_ok)=(1,1,1);
	if ($nfilter) {
		if ($s1 =~ /N/) {
			$mate1_nfilter_ok=0;
		}
	}

	if ($minqual) {
		if (avgqual($q1)<$minqual) {
			$mate1_qualfilter_ok=0;
		}
	}
	if (!($mate1_nfilter_ok && $mate1_qualfilter_ok)) {
		$mate1_ok=0;
	}

	if ($mate1_ok) {
		print S $hs1,$s1,$hq1,$q1;
	} else {
		print D $hs1,$s1,$hq1,$q1;
	}
}


if ($verbose) {
	print STDERR "Processed $count reads...\n";
	print STDERR "Finished.\n";
}

close(S);
close(D);
close(F) if (-f $file);


sub avgqual {
	my $q = shift;
	chomp $q;
        my @phred= map {ord($_)-64} split //,$q;
	my $sum=0;
        for (my $i=0;$i<=$#phred;$i++) {
                $sum +=$phred[$i];
        }
	my $avg=$sum/($#phred+1);
	return $avg;
}


sub getRead {
	my $hs1=<F> || return;
	my $s1=<F> || return;
	my $hq1=<F> || return;
	my $q1=<F> || return;
	return ($hs1,$s1,$hq1,$q1);
}

sub paramOk {
    #Checks if all required parameters were provided and if the files exist. OK=2 => 2 input files OK=1 => 1 interleaved input file
    my $ok = 0;
    if (-f $file) {

	$ok=1;
	return $ok;
    } else {    
	return $ok;
    }
}



=head1 NAME

 clean_solexa_se.pl

=head1 SYNOPSIS

 Use:
 clean_solexa_se.pl [--file path] [--[no]nfilter] [--minqualthreshold int]  [--trimbegin int] [--trimend int] [--prefix string] [--[no]verbose]]

 Examples:
 clean_solexa.pl
 	--file s_1_1_sequences.fastq
	--nfilter
 	--minqualthreshold 20
	--prefix myrun

=head1 DESCRIPTION

 clean_solexa_se.pl is a script to automate the sequencing cleaning of Illumina sequencing data. Some sequencing runs benefit from agressively trimming reads prior to de novo assem bly (or  mapping). clean_solexa.pl can discard reads containing uncalled bases (Ns) and low quality reads. It can also be configured to trim all reads at a a fixed psoition. This script works with single end sequencing runs.

=head1 OPTIONS

 Arguments:
 --file             | -f  fastafile Path to fastq file containing both mates interleaved
 --minqualthreshold | -q  int       Minimum quality for a read to be kept
 --trimbegin        | -b  int       Trim all reads starting at trimbegin (Default: no trim)
 --trimend          | -e  int       Trim all reads ending at trimend (Default: no trim)
 --prefix           | -p string     Prefix to output files (Default: out)
 Switches:
 --[no]nfilter      | -n  string    Discard both mates when at least one of them have uncalled bases (Default: on)
 --[no]verbose      | -v  Enables or disables verbosity
 --help             | -h  Displays help message

=head1 AUTHOR

 Gustavo Gilson Lacerda Costa, < glacerda@lge.ibi.unicamp.br >.

=head1 BUGS

 Probable many.

=cut