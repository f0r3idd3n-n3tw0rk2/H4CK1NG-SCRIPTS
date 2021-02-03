#!/usr/bin/env python3

#1.) Import modules

import re



#2.) Define the variable



#filename = server_logfile.txt


#3.) Read a Log file and add the content to an array


#def load_server_logfile(filename):
#    print("[+] Loading Server Logfile")
#    with open(filename) as f:
#        content = f.readlines()
#    content = [x.strip() for x in content]
#    return content
#print(content.)


#def load_server_logfile(filename):
def load_server_logfile(filename):
    print("[+] Loading Logfile")
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content
#Alternative xss_teststrings.txt
    #xss_test_strings = open("xss_teststrings.txt").read().split("\n")

#Hauptfunktion
def main():
    print("[+] Starting Scanner")
    #Aufrufen load_xss_test_strings Funktion und einlesen der xss_teststrings.txt
    log_contents = load_server_logfile('server_logfile.txt')
    #Schleife zur Ausgabe der einzelnen Listenelemente
    for log_content in log_contents:
        #Debug Textausgabe
        print(log_content)
        #Leeres Dictionary erstellen
        log_list = {}
        #Schleife Dictionary erweitern mit den Parametern und den xss_test_strings
        for parameter in parameters:
            log_list[parameter] = log_list
            print(log_list)


        #Überprüfung ob der Teststring in der Response gefunden wird
        if xss_test_string in response.text:
            #Verwundbarkeit gefunden
            print("[!] XSS Vulnerability detected")
        else:
            #Keine Verwundbarkeit gefunden
            print("[+] All good. No XSS Vulnerability detected.")

if __name__ == '__main__':
    main()





#4.) search through the list/array and print only failed logins within 10 seconds






#5.) search through the list/array and print only failed logins within on same day and count it





#6.) search through the list/array and print only failed logins within on total and count it






#for element in answered_list:  # for each element from the list in the answer result
#    client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}  # create a dictionary with ip and mac
#    clients_list.append(client_dict)  # append the result to clients_list from client dict

#return (clients_list)




#create a function which is doing the printing of that list. Variable results_list
def print_result(results_list):
    print("Host-IP\t\t\tFailed Logins within 10 sec\n-------------------------------------")             #print a header line
    for host in results_list:
       print(host["host-ip"] + "\t\t" + host["failed_login"])                                #print clients only ip and mac















