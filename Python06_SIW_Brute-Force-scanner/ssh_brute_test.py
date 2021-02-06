#!/usr/bin/env python3

#define modules to load
import re
import sys
import argparse
import datetime
import apache_log_parser


#variables
logfile = "server_logfile_test.txt"
pp = pprint.PrettyPrinter(indent=4)

re.search(" Failed ", line)



#   Mar 18 13:50:30 bit_server sshd[22625]: Failed password for invalid user abridge from 45.15.16.37 port 18397 ssh2
#

#Standard function open()
#deliver a new file object logs and print the output
logs = open('server_logfile_test.txt', 'r')

serverlog = logs.read()


with open(logfile, "r") as f:
    line = f.readline()

    while line:
        if (re.search(" Failed ", line)):
            try:
                log_line_data = line_parser(line)






#try:
 # logs = open('server_logfile_test.txt', 'r')

  # serverlog = logs.read()

  #  content = [x.strip() for x in serverlog]
  #  list()
  #  for i in content:

   #     print(content)



    #with open('server_logfile_test.txt') as f:
        #for line in f:
            #print(line)

#except:
    #print('Can not read the logfile')


