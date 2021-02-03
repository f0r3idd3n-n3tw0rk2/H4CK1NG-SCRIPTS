#!/usr/bin/env python3

#1.) Import modules





#2.) Define the variable






#3.) Read a Log file and add the content to an array


def load_server_logfile(filename):
    print("[+] Loading Server Logfile")
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content




#with open("Data.log", "r") as ins:

#    array = []

#    for line in ins:

#        array.append(line)






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















if xss_test_script not in line:
    print(bcolors.CBLUE,
          "\r\n[---------------------------------------------------------------------------]",
          "\r\n")
    print(bcolors.CBLUE, "\r\n[---------------------------]", "\r\n[Form_Field:]", input_type,
          "\r\n[---------------------------]")
    print(bcolors.CBLUE, "\r\n[+++++]", "Webpage has no XSS Vulnerability", "[+++++]")
else:
    print(bcolors.CRED,
          "\r\n[---------------------------------------------------------------------------]",
          "\r\n")
    print(bcolors.CRED, "\r\n[---------------------------]", "\r\n[Form_Field:]", input_type,
          "\r\n[---------------------------]")
    print(bcolors.CRED, "\r\n[-----]", "Webpage has an XSS Vulnerability", "[-----]", "\r\n")