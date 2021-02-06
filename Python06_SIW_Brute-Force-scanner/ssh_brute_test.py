#!/usr/bin/env python3

# 1.) Import modules

import re
import sys
import time
import tqdm
from re import match


# class Colors
class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'
    CGREEN = '\33[92m'


# 2.) Define the variable
# use argument for input

print(bcolors.CGREEN, "Default Server Logfile must be in folder ->>>> server_logfile_test.txt")
print(bcolors.CGREEN, "Default Treshold ->>>> 5x Error Login")

print("Please Enter the logfile to analyze or type default\t:")
log_filename = input()
threshold = 5
brute_force = 'Failed'


# print("Server Logfile will be analyzed please wait....")
# time.sleep(3.5)    # Pause 5.5 seconds

# for i in tqdm.tqdm(range(200)):
#    time.sleep(0.01)
# or other long operations

if log_filename == 'default':
    print("[+] Loading Server Logfile")
    print("[+] Using default Logfile in Folder")
    time.sleep(1.5)  # Pause 5.5 seconds
    default_logfile = 'server_logfile_test.txt'
    with open(default_logfile) as f:
        lines = f.read().splitlines()

    print(type(lines))
    print(lines)

    for x in lines:
        r = re.compile('^\w\w\w\s\d\d$')
        newlist = list(filter(r.match, lines))
        print(newlist)




        #values = {}
        #for parameter in values:
            #values[parameter] = lines

            #filtered_values = list(filter(lambda v: match ('^\w\w\w\s\d\d$', v), lines))
            #result = re.findall('^\w\w\w\s\d\d$', values)



    #print("Date\t:", str(date)), Regex: '\w\w\w\s\d\d$'
    #print("Time\t:", str(time))
    #print("IP-Adress\t:", str(IP))


else:
    print("[+] Loading Server Logfile\t:" + log_filename)
    time.sleep(1.5)  # Pause 5.5 seconds
    with open(log_filename) as f:
        lines = f.read().splitlines()

    print(type(lines))
    print(lines)


    for x in lines:
        values = str(lines)
        filtered_values = list(filter(lambda v: match ('^\w\w\w\s\d\d$', v), values))
        result = re.findall('^\w\w\w\s\d\d$', values)
        print(filtered_values)









def search(log_filename, brute_force):


    for i in range(len(lines)):
        if lines[i] == brute_force:
            return True
        return False

    login_list = lines


    if search(login_list, brute_force):
        print("[!] Brute Force Detection")
    else:
        print("[+] All good. No Brute Force On Server.")


search(brute_force, log_filename)















# i = "root"
# for i in lines:
#    print("[!] Brute Force Detection")

# else:
# Keine Verwundbarkeit gefunden
#    print("[+] All good. No Brute Force On Server.")


# if match:
# Brute Force Detected
# print("[!] Brute Force Detection")
# else:
# Keine Verwundbarkeit gefunden
# print("[+] All good. No Brute Force On Server.")


# get lines with login failures
# extract IP of this line
# remove duplicate items from list
# count how many failed login attempts for this ip
# print the result if it is above the treshold
