#!/usr/bin/env python3

#import bibliothek
import sys


#print(sys.argv)



text_file = open("filename.dat", "r")
lines = text_file.readlines()
print (lines)
print (len(lines))
text_file.close()



url = sys.argv[1]
parameters = sys.argv[2].split(",")

print(url)
print(parameters)


def main():
    print("|+] Starting Scanner")


if __name__ == "__main__":
    main()
