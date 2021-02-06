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
print(bcolors.CGREEN, "Default Treshold ->>>> treshold -> integer")

log_filename = input("Please Enter the logfile to analyze\t:")
threshold = 5


# print("Server Logfile will be analyzed please wait....")
# time.sleep(3.5)    # Pause 5.5 seconds

# for i in tqdm.tqdm(range(200)):
#    time.sleep(0.01)
# or other long operations





print("[+] Loading Server Logfile")

with open(log_filename) as f:
    lines = f.read().splitlines()

print(type(lines))
print(lines)


#content = [line.strip() for line in lines]
#print(lines)


d = {}

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