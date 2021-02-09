#!/usr/bin/env python3

#What should it do
# get lines with login failures
# extract IP of this line                           -> OK
# remove duplicate items from list
# count how many failed login attempts for this ip  -> OK
# print the result if it is above the treshold      -> OK

# 1.) Import modules for this python script

import re
import sys
import time
import tqdm
from re import match
from collections import Counter


# class Colors to mark the print lines with specified color
class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'
    CGREEN = '\33[92m'


# 2.) Define the variable
# enter the logfile and the treshold for the analyzing task
print(bcolors.CGREEN, "Server Logfile must be in folder ->>>> DEFAULT: server_logfile_test.txt")
print(bcolors.CGREEN, "Default Treshold ->>>> 5 Times Error Login")

print("Please Enter the logfile to analyze or type default\t:")
log_filename = input()
print("Please Enter the Threshold for failed Login attempts\t:")
threshold = input()
#threshold = 5
brute_force = 'Failed'


#Regular Expression for parsing the logfile
ip_myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
date_myregex = r''
failed_myregex = re.compile(r"\bFailed\b")
pattern_failed_myregex = r"Failed"



##################################################################
#if clause for the choice default logfile: server_logfile_test.txt
if log_filename == 'default':
    print("[+] Loading Server Logfile")
    print("[+] Using default Logfile in Folder")
    time.sleep(1.5)  # Pause 5.5 seconds
    #for i in tqdm.tqdm(range(200)):
    # time.sleep(0.01)
    default_logfile = 'server_logfile_test.txt'



#regex to search for IP-Address in the file
#ip_myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#open the filename, read through, make a list with all findings of IP adresses in variable log and count it
    with open(default_logfile) as f:
        log = f.read()
        my_iplist = re.findall(ip_myregex, log)
        ipcount = Counter(my_iplist)
        for k, v in ipcount.items():
            if str(v) >= threshold:
                print(bcolors.CRED, "IP Address " + "=> " + str(k) + " " + "Count " + "=> " + str(v))
                print(bcolors.CRED, "IP-Address\t:", str(k), "Bruteforce Attack", str(k), "is on Blacklist")
            else:
                print(bcolors.CGREEN, "IP Address " + "=> " + str(k) + " " + "Count " + "=> " + str(v))
                print(bcolors.CGREEN, "IP-Address\t:", str(k), "Threshold not reached")
#end of regex and IP



#regex to search for Line and Error in the file
#open the filename, read through, make a list with all findings of "Failed" in variable log and count it
    count = 0
    print("\nUsing for loop")

    with open(default_logfile) as fp:
        for line in fp:
            count += 1
            print("Line{}: {}".format(count, line.strip().split(" ")))





#########################################################
#else clause for the choice own logfile to parse through
else:
    print("[+] Using", log_filename, "Logfile in Folder")
    print("[+] Loading Server Logfile\t:" + log_filename)
    time.sleep(1.5)  # Pause 5.5 seconds
    # for i in tqdm.tqdm(range(200)):
    # time.sleep(0.01)

    # regex and IP






    # regex to search for Line and Error in the file
    # open the filename, read through, make a list with all findings of "Failed" in variable log and count it
    count = 0
    print("\nUsing for loop for Errors")

    with open(log_filename, "r") as fp:
        log_error = fp.readlines()
        #my_error_list = re.search(pattern_failed_myregex, log_error)
        login_failure_ips = []
        for item in log_error:
            if "pam_unix(sshd:auth): authentication failure;" in item:
                #print(item)
                login_failure_ips.append(item.strip().split(" "))
                date = print(item[2])
                print(login_failure_ips)

                ########copy-paste######
            with open(log_filename) as f:
                log = f.read()
                log_error = fp.readlines()
                my_iplist = re.findall(ip_myregex, log)
                ipcount = Counter(my_iplist)
        for items in item:
            for k, v in ipcount.items():
            #for items in item:
                if str(v) >= threshold:
                    print(bcolors.CRED, "IP Address " + "=> " + str(k) + " " + "Count " + "=> " + str(v))
                    print(bcolors.CRED, "IP-Address\t:", str(k), "Bruteforce Attack", str(k), "is on Blacklist")
                else:
                    print(bcolors.CGREEN, "IP Address " + "=> " + str(k) + " " + "Count " + "=> " + str(v))
                    print(bcolors.CGREEN, "IP-Address\t:", str(k), "Threshold not reached")
            #copy-paste##
            # end of regex and IP





























