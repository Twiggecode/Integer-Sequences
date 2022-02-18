#!/usr/bin/env bash
#: Bash Script to return 2 to the n'th.

#: TITLE:      powers-of-2.sh
#: DATE:       22/02/17
#: AUTHOR:     GitHub: itsf4llofstars
#: VERSION:    0.1.0
#: DESCRPTION: Calculates 2 raised to the power of n, a user given number.
#: OPTIONS:    -h, --help, -n <integer>

#: Display help text
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    clear
    cat <<EOF
Given a number this scripts calculates 2 raised to that number. This number can
entered on the command line via the option -n or if not given on the command line
the user will be polled for the number.

On 32 bit system 32 may be the higest number to be calculated, 64 on 64 bit systems.

This script has weak error checking. It will ensure the command line given number
is 0 or greater, and it will ensure the given number is 0 ro greater. It will not
ensure that a number is passed if a -n is sent on the command line. No checking is
done to ensure that an integer is passed.

$ man ./powers-of-2.1 man page not implimented. See docs below.

Calls:
$ ./powers-of-2.sh [option] <number>

options
    -h, --help  This help text.
    -n <number>, The users given number

Examples:
    $ ./powers-of-2.sh
    $ ./powers-of-2.sh -n 3
EOF
    exit 0
fi

#: Main Algorithm
clear

NTH=0
if [ "$1" == "-n" ] && [ "$2" -ge 0 ]; then
    NTH="$2"
elif [ "$1" == "-n" ] && [ "$2" -lt 0 ]; then
    printf "Please only enter a number 0 or greater.\n"
    exit 1
else
    printf "Enter your exponent: "
    read NTH
fi

if [ "$NTH" -lt 0 ]; then
    printf "Please only enter a number 0 or greater.\n"
    exit 1
fi

power_of_two=$((2 ** "$NTH"))

printf "The $NTH'th number in the sequence is $power_of_two\n"

exit 0

#: Documentation for man page creation.
#: Create man page by:
#: Filling in the sections below with your code and text. Don't touch the lines with the equals
#: sign. Run the pod2man command below these lines in the command prompt. The extension on the 2nd
#: script line should be 1.

#: $ pod2man powers-of-two.sh > powers-of-two.1

: <<'man_page_text'
=head1 NAME

    NAME <script_name.sh> [option]

=head1 SYNOPSIS

    SYNOPSIS

=head1 DESCRIPTION

    DESCRIPTION

=head1 EXAMPLES

    EXAMPLE calls

=head1 OVERVIEW

    OVERVIEW

=head1 DEFAULTS

    DEFAULTS

=head1 OPTIONS

    OPTIONS

man_page_text
