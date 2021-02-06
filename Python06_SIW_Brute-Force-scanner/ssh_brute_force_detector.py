#!/usr/bin/env python3

#1.) Import modules

import re
import sys
import time
import tqdm



class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'


#2.) Define the variable
# use argument for input

print(bcolors.CBLUE,"Default Server Logfile must be in folder ->>>> server_logfile_test.txt")
print(bcolors.CRED,"Default Treshold ->>>> treshold -> integer")

log_filename = input("Please Enter the logfile to analyze\t:")





#print("Server Logfile will be analyzed please wait....")
#time.sleep(3.5)    # Pause 5.5 seconds

#for i in tqdm.tqdm(range(200)):
#    time.sleep(0.01)
    # or other long operations




#3.) Read a Log file and add the content to an array

def load_server_logfile(log_filename):
    print("[+] Loading Server Logfile")
    with open(log_filename) as f:
        content = f.readlines()
    content = [line.strip() for line in content]
    print(content)
    log = content
    #return content







#Hauptfunktion
def log(log):
    print("[+] Starting Parsing the logfile")
    #Aufrufen load_xss_test_strings Funktion und einlesen der xss_teststrings.txt
    log_contents = log
    #Schleife zur Ausgabe der einzelnen Listenelemente
    for log_content in log_contents:
        #Debug Textausgabe
        print(log_content)
        #Leeres Dictionary erstellen
        list = {}
        #Schleife Dictionary erweitern mit den Parametern und den xss_test_strings
        for parameter in list:
            list[parameter] = log_content
            print(list)
        response = list


        #Überprüfung ob der Teststring in der Response gefunden wird
        word01 = "Failed"
        if word01 in response:
            #Brute Force Detected
            print("[!] Brute Force Detection")
        else:
            #Keine Verwundbarkeit gefunden
            print("[+] All good. No Brute Force On Server.")

#if __name__ == '__main__':
#    main()


load_server_logfile(log_filename)
log(log)





#4.) search through the list/array and print only failed logins within 10 seconds






#5.) search through the list/array and print only failed logins within on same day and count it





#6.) search through the list/array and print only failed logins within on total and count it






#for element in answered_list:  # for each element from the list in the answer result
#    client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}  # create a dictionary with ip and mac
#    clients_list.append(client_dict)  # append the result to clients_list from client dict

#return (clients_list)




#create a function which is doing the printing of that list. Variable results_list
#def print_result(results_list):
    #print("Host-IP\t\t\tFailed Logins within 10 sec\n-------------------------------------")             #print a header line
    #for host in results_list:
      # print(host["host-ip"] + "\t\t" + host["failed_login"])                                #print clients only ip and mac















