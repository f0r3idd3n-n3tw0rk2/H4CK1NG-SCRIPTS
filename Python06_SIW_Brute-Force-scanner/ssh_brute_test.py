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
            print("Line{}: {}".format(count, line.strip()))





#########################################################
#else clause for the choice own logfile to parse through
else:
    print("[+] Using", log_filename, "Logfile in Folder")
    print("[+] Loading Server Logfile\t:" + log_filename)
    time.sleep(1.5)  # Pause 5.5 seconds
    # for i in tqdm.tqdm(range(200)):
    # time.sleep(0.01)

    # regex and IP


#open the filename, read through, make a list with all findings of IP adresses in variable log and count it
    with open(log_filename) as f:
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

    with open(log_filename) as fp:
        log_error = fp.read()
        my_errorlist = re.findall(failed_myregex, log_error)
        for line in my_errorlist:
            count += 1
            print("Line{}: {}".format(count, line.strip()), log_error)














            #match_date = re.search(r'Mar$', line)
            #if match_date is None:
                #print("No Match")
            #else:
                #print(match_date)



    #with open(default_logfile) as f:
        #lines = f.read().splitlines()
        #print(lines[1])
        #for x in lines:
            #regex = r"('^\w\w\w\s\d\d$')"
    #^\w\w\w\w\d:\w\w\w\s\d\d$
           # match = re.search(regex, 'lines')
            #if match is None:
            #    print("No Match")
            #print(match)





    #print(type(lines))
    #print(lines[0])
    #print(lines[1])
    #print(lines[2])






        #values = {}
        #for parameter in values:
            #values[parameter] = lines

            #filtered_values = list(filter(lambda v: match ('^\w\w\w\s\d\d$', v), lines))
            #result = re.findall('^\w\w\w\s\d\d$', values)



    #print("Date\t:", str(date)), Regex: '\w\w\w\s\d\d$'
    #print("Time\t:", str(time))
    #print("IP-Adress\t:", str(IP))












    #with open(log_filename) as f:
       # lines = f.read().splitlines()

    #print(type(lines))
    #print(lines)


    #for x in lines:
        #values = str(lines)
        #filtered_values = list(filter(lambda v: match ('^\w\w\w\s\d\d$', v), values))
        #result = re.findall('^\w\w\w\s\d\d$', values)
        #print(filtered_values)









#def search(log_filename, brute_force):


    #for i in range(len(lines)):
        #if lines[i] == brute_force:
           # return True
        #return False

   # login_list = lines


    #if search(login_list, brute_force):
       # print("[!] Brute Force Detection")
    #else:
        #print("[+] All good. No Brute Force On Server.")


#search(brute_force, log_filename)















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
# extract IP of this line                           -> OK
# remove duplicate items from list
# count how many failed login attempts for this ip  -> OK
# print the result if it is above the treshold      -> OK
