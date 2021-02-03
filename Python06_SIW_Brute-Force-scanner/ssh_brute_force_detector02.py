#!/usr/bin/env python3


import apache_log_parser

line_parser = apache_log_parser.make_parser("%v %h %l %u %t \"%r\" %>s %b")

filename = 'server_logfile_test.txt'


with open(filename) as fp:  # doctest: +SKIP
    for entry in parser.parse_lines(fp):
        print(str(entry.request_time), entry.request_line)