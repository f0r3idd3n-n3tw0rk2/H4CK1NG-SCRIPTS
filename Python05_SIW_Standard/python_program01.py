#!/usr/bin/env python3

#1.) Import modules
import sys


#Printing Number of Arguments f.eg. python3 scriptname.py argument1 argument2

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

#Now run above script as follows −
#$ python test.py arg1 arg2 arg3

#This produce following result −
#Number of arguments: 4 arguments.
#Argument List: ['test.py', 'arg1', 'arg2', 'arg3']



#a List
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[0])
#apple
print(len(mylist))

#a dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])


#2.) Define variables
#sys.arv 1 -> python3 "programme-name.py" "sys.arv 1"
#sys.arv 2 -> python3 "programme-name.py" "sys.arv 2 and split by ,"

txt = "welcome to the SIW"
x = txt.split()
print(x)


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




#5.) Define a function with my_function() method
# in the end call the function

def my_function():
  print("Hello from a function")

my_function()


#6.) Define a function and call the attribute
def my_function(variable2):
  print(variable2 + "Hello from a function")

my_function(variable2)


#7.) Passing a list in a function as argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
