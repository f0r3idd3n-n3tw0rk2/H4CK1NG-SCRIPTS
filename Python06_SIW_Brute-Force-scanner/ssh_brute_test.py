#!/usr/bin/env python3


import re
import sys
import argparse
from collections import Counter





#   Mar 18 13:50:30 bit_server sshd[22625]: Failed password for invalid user abridge from 45.15.16.37 port 18397 ssh2
#

#Standard function open()
#deliver a new file object logs and print the output

try:
    logs = open('server_logfile_test.txt', 'r')

    serverlog = logs.read()

    content = [x.strip() for x in serverlog]
    for i in content:
        print(content)

except:
    print('Can not read the logfile')


