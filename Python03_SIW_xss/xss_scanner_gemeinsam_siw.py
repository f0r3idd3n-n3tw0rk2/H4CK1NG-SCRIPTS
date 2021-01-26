#!/usr/bin/env python3

#Import sys Modul für das Einlesen der mitgegebenen Argumente
import sys
#Import requests Modul für das senden der Requests an den Server
import requests

#Variablen definieren
url = sys.argv[1]
parameters = sys.argv[2].split(",")

#Debug Textausgabe
#print(url)
#print(parameters)

#Funktionsdefinition

#Einlesen der xss_teststrings.txt
def load_xss_test_strings(filename):
    print("[+] Loading XSS Test-Strings")
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
    xss_test_strings = load_xss_test_strings('xss_teststrings.txt')
    #Schleife zur Ausgabe der einzelnen Listenelemente
    for xss_test_string in xss_test_strings:
        #Debug Textausgabe
        #print(xss_test_string)
        #Leeres Dictionary erstellen
        payload = {}
        #Schleife Dictionary erweitern mit den Parametern und den xss_test_strings
        for parameter in parameters:
            payload[parameter] = xss_test_string
            #print(payload)
        #Request erstellen mit dem aktuellen Dictionary aus der vorherigen For-Schlaufe
        response = requests.post(url, payload)

        #Überprüfung ob der Teststring in der Response gefunden wird
        if xss_test_string in response.text:
            #Verwundbarkeit gefunden
            print("[!] XSS Vulnerability detected")
        else:
            #Keine Verwundbarkeit gefunden
            print("[+] All good. No XSS Vulnerability detected.")

if __name__ == '__main__':
    main()
