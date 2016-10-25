#!/usr/bin/env perl
# aptitude install libdancer2-perl
# aptitude install libdancer-plugin-rest-perl

use strict;
use warnings;

use Dancer2;
use Dancer::Plugin::REST;
set port => 9091;
prepare_serializer_for_format;

####################################
# MAIN
#$ ./serv.pl
# [main:17436] debug @2016-10-25 19:37:51> Launch... in ./serv.pl l. 16
# >> Dancer2 v0.152000 server 17436 listening on http://0.0.0.0:9091

debug("Launch...");

####################################

#$ curl "http://localhost:9091/nothing"
# Nothing
get '/nothing' => sub {
    "Nothing\n";
};

#$ curl "http://localhost:9091/input/param1"
# Input=param1
get '/input/:id' => sub {
    "Input=".params->{id}."\n";
};

#$ curl "http://localhost:9091/input_output/param1/param2"                                                                          
# Input=param1 Output=param2                                                                                                                                   
get '/input_output/:id/:output' => sub {
    "Input=".params->{id}." Output=".params->{output}."\n";
};

#$ curl "http://localhost:9091/input_params/param1?type=test"                                                             
# Input=param1 type=test
get '/input_params/:id' => sub {
    "Input=".params->{id}." type=".params->{type}."\n";
};

dance;
