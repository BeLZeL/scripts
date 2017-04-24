#!/usr/bin/env perl

#$ cat file.xml
#<?xml version="1.0"?>
#<nodes>
#    <node1 name="name1" type="A" />
#    <node2 name="name2" type="B" />
#    <node3 name="name3" type="C" />
#</nodes>

use strict;
use warnings;

use XML::Simple; # load XML profiles

my %loaded_xml;

####################################
# MAIN

my $parser = XML::Simple->new( KeepRoot => 1 );
my $file_xml;

$file_xml = $parser->XMLin('file.xml');
%loaded_xml = %{ $file_xml->{nodes}{node2} };
$loaded_xml{extra_param} = "42";

print "$loaded_xml{name}|$loaded_xml{type}|$loaded_xml{extra_param}\n";

#$ ./xml.pl 
# name2|B|42
