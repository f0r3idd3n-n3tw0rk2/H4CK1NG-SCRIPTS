#!/usr/bin/env python3

#1.) Import modules

import re
import sys
import time
import tqdm



class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'
    CGREEN = '\33[92m'


#2.) Define the variable
# use argument for input

print(bcolors.CGREEN,"Default Server Logfile must be in folder ->>>> server_logfile_test.txt")
print(bcolors.CGREEN,"Default Treshold ->>>> treshold -> integer")

log_filename = input("Please Enter the logfile to analyze\t:")
threshold = 5




#print("Server Logfile will be analyzed please wait....")
#time.sleep(3.5)    # Pause 5.5 seconds

#for i in tqdm.tqdm(range(200)):
#    time.sleep(0.01)
    # or other long operations




#3.) Read a Log file and add the content to an array


print("[+] Loading Server Logfile")
with open(log_filename) as f:
    content = f.readlines()
    content = [line.strip() for line in content]
    print(content)
return content






#get lines with login failures
#extract IP of this line
#remove duplicate items from list
#count how many failed login attempts for this ip
#print the result if it is above the treshold




















