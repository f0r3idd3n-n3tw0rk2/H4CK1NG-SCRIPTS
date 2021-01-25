#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import sys
import time
import tqdm



class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'

#website = "http://167.71.54.69/"








print(bcolors.CBLUE,"e.g target ->>>> http://target.com/", "or http://IP-ADDRESS/")
website = input("Please Enter Target URL\t:")
print(bcolors.CBLUE,"Default Payload List ->>>> xss_teststrings02.txt")
print(bcolors.CBLUE,"Default Payload ->>>> <h1>XSS-VULNERABLE</h1>")

print("XSS-SCANNER will load the full Aresenal to attack the given Page")
time.sleep(3.5)    # Pause 5.5 seconds

for i in tqdm.tqdm(range(100)):
    time.sleep(0.01)
    # or other long operations















#This is the 1st function for error handling and trying the parameter for the website calling it in the method request
#Checking for type errors in the website url and checking with Timeout if the website is reachable
#Also you can skip the script manual with the escape Character "Control+C"
def request(website):
    url = website
    while True:
        try:
            return requests.get(url, timeout=6.0)

        except requests.ConnectionError as e:
            print(bcolors.CRED,
                  "OOPS!! Connection Error. Make sure you are connected to Internet or check the correct Syntax of IP address. Technical Details given below.\n")
            print(str(e))
            break
        except requests.Timeout as e:
            print(bcolors.CRED, "OOPS!! Timeout Error")
            print(str(e))
            break
        except requests.RequestException as e:
            print(bcolors.CRED, "OOPS!! General Error")
            print(str(e))
            break
        except KeyboardInterrupt:
            print(bcolors.CRED, "Someone closed the program")
            break
        except AttributeError:

            print(bcolors.CRED, "Website is not readable")
            print(bcolors.CRED, "Please type in a correct Website html")
    sys.exit()

#This is the 2nd function which is calling the variable website after error checks
#Then it is using this URL to form the response, analyze it with Beautifulsoup for parsing the content
#put the forms which are found into the forms_list
#Get the action, method and create the input list
#Create the Post Data for the website to use the name, type and value
#If the Value is Text then use the xss test Script String
def target_url(website):
    target_url = website
    response = request(target_url)

    parsed_html = BeautifulSoup(response.content, "html.parser")
    forms_list = parsed_html.findAll("form")

    for form in forms_list:
        action = form.get("action")
        post_url = urllib.parse.urljoin(target_url, action)
        method = form.get("method")
        inputs_list = form.findAll("input")
        post_data = {}

        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")

#If input for the variable is text then put in the value for the xss test script string
            if input_type == "text":
                input_value = "<h1>XSS-VULNERABLE</h1>"
                # print(input)
                # for Post in input_name:
                post_data[input_name] = input_value
            # print(Post)

        for input_type in post_data:
            result = requests.post(post_url, data=post_data)
            # result_p_content = print(result.content)
            # print(result.content)

            # XSS_Test_Script Variable
            xss_test_script = "<h1>XSS-VULNERABLE</h1>"

            # write the result.content in a file and save it
            with open("result.txt", "w") as text_file:
                print(result.content, file=text_file)

            # read the file with all the results and check if the webpage is vulnerable
            with open("result.txt", "r") as f:
                for line in f:
                    # if '<h1>test</h1>' not in line:
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

            print(result.content)
    sys.exit()



#call the function "target_url" and "requests" with the parameter variable website given in the input

target_url(website)
requests(website)




