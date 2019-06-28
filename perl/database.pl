#!/usr/bin/perl
# aptitude install libdbi-perl libdbd-pg-perl

# ./database.pl name host user
# Query will return 2 columns.
# row : TESTER - TEST
# Query updates 1 lines
# END

use strict;
use warnings;
use DBI;

my $usage = <<EOU;
    Usage: $0 <db name> <db host> <db user>
EOU

my $db_name = $ARGV[0];
my $db_host = $ARGV[1];
my $db_user = $ARGV[2];

my $dbh = DBI->connect("dbi:Pg:dbname=$db_name;host=$db_host", $db_user)
    or die "$DBI::errstr";

#---------------------------------

my $req = <<EOReq;
SELECT user_id, account_id FROM ua_link
EOReq

my $sth = $dbh->prepare($req);
$sth->execute();
print "Query will return $sth->{NUM_OF_FIELDS} columns.\n";
while (my $hash = $sth->fetchrow_hashref())
{
    my $user    = $hash->{user_id};
    my $account = $hash->{account_id};
    print "row : $user - $account\n";
}
$sth->finish;

#---------------------------------

$req = <<EOReq;
UPDATE ua_link set column = 'FR' where user_id = 'TESTER'
EOReq

$sth = $dbh->prepare($req);
my $nb_updates = $sth->execute();
print "Query updates $nb_updates lines\n";
$sth->finish;

#---------------------------------

END {
    print "END\n";
    if ($dbh)
    {
        $dbh->disconnect;
    }
}
