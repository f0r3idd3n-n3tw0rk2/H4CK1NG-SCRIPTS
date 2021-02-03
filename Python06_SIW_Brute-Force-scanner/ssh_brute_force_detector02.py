#!/usr/bin/env python3


from apachelogs import LogParser






with open('server_logfile_test.txt') as fp:  # doctest: +SKIP
    for entry in parser.parse_lines(fp):
        print(str(entry.request_time), entry.request_line)