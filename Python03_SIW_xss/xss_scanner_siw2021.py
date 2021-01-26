#!/usr/bin/env python3

#import bibliothek
import sys
import requests


#print(sys.argv)


url = sys.argv[1]
parameters = sys.argv[2].split(",")



#url = "http://167.71.54.69/"


def load_xss_test_strings(filename):
    print("|+] Starting Scanner")
    with open(filename) as f:
        content = f.readline()
    content = [x.strip() for x in content]
    return content




def main():
    print("|+] Starting Scanner")

    xss_test_strings = load_xss_test_strings('./xss_test_string.txt')

    for xss_test_string in xss_test_strings:
        data = {}

        for parameter in parameters:
            data[parameter] = xss_test_string


        print(xss_test_string)
        data = {'first': xss_test_string, 'last': xss_test_string}
        response = requests.post(url, data)

        print("Test String:")
        print(xss_test_string)

        print("Response:")
        print(response.text)




if __name__ == "__main__":
    main()













#print(url)
#print(parameters)

#text_file = open("filename.dat", "r")
#lines = text_file.readlines()
#print lines
#print len(lines)
#text_file.close()