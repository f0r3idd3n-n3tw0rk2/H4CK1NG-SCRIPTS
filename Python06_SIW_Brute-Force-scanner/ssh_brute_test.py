#!/usr/bin/env python3

# 1.) Import modules

import re
import sys
import time
import tqdm


class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'
    CGREEN = '\33[92m'


# 2.) Define the variable
# use argument for input

print(bcolors.CGREEN, "Default Server Logfile must be in folder ->>>> server_logfile_test.txt")
print(bcolors.CGREEN, "Default Treshold ->>>> 5x Error Login")

print("Please Enter the logfile to analyze\t:")
log_filename = input()
threshold = 5


# print("Server Logfile will be analyzed please wait....")
# time.sleep(3.5)    # Pause 5.5 seconds

# for i in tqdm.tqdm(range(200)):
#    time.sleep(0.01)
# or other long operations





if log_filename == None:
    print("[+] Loading Server Logfile")
    print("[+] Using default Logfile in Folder")
    default_logfile = 'server_logfile_test.txt'
    with open(default_logfile) as f:
        lines = f.read().splitlines()

    print(type(lines))
    print(lines)


else:
    print("[+] Loading Server Logfile")
    print("[+] Loading Server Logfile" + log_filename)
    with open(log_filename) as f:
        lines = f.read().splitlines()

    print(type(lines))
    print(lines)







i = "Failed"
for i in lines:
    print("[!] Brute Force Detection")

else:
    #Keine Verwundbarkeit gefunden
    print("[+] All good. No Brute Force On Server.")






#if match:
    # Brute Force Detected
    #print("[!] Brute Force Detection")
#else:
    # Keine Verwundbarkeit gefunden
    #print("[+] All good. No Brute Force On Server.")


# get lines with login failures
# extract IP of this line
# remove duplicate items from list
# count how many failed login attempts for this ip
# print the result if it is above the treshold