#!/usr/bin/perl
# Read line by line

# Input
# 14:54:20.336 INFO   FUNCTION@59:<node type="Update">...</node>

# Output :
# 15:49:52 -> new
# 15:50:00 -> update
# 15:50:00 -> update
# 15:50:10 -> cancel
# [...]

use strict;
use warnings;
use XML::LibXML;

# Forcer le flush STDOUT si on fait un tailf par exemple
BEGIN { $| = 1 }

my $parser  = XML::LibXML->new();

while (my $line = <STDIN>)
{
    if ($line =~ /^(\d{2}:\d{2}:\d{2})\.\d{3}.+FUNCTION\@(73|59):\s+(.*)/)
    {
        my $logtime = $1;
        my $xml  = $3;
        my $doc  = $parser->parse_string($xml);
        print "$logtime -> $order_action " . lc($doc->findvalue('/node/@type'). "\n"; 
    }
    # [...]
}
