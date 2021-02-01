#!/usr/bin/env python3

#1.) Import modules
import sys



#2.) Define variables
#sys.arv 1 -> python3 "programme-name.py" "sys.arv 1"
#sys.arv 2 -> python3 "programme-name.py" "sys.arv 2 and split by ,"

variable1 = sys.argv[1]
variable2 = sys.argv[2].split(",")

#3.) Loading a File and first function

def method01(filename):
    print("[+] Loading the filename")
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


#4.) Main function
#for loop to fill a dictionary

def main():
    print("[+] Starting the Program")

    for string_var in string_variab:
        #create an empty dictionary
        payload = {}
        #for loop to fill the dictionary with entries
        for parameter in variable2:
            payload[parameter] = string_var




    if __name__ == '__main__':
     main()


