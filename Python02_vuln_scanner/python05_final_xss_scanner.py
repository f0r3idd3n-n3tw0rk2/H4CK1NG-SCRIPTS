#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup
import urllib.parse
import re


class bcolors:
    CBLUE = '\33[34m'
    CRED = '\33[31m'


def request(url):
    try:
        return requests.get(url)
    except requests.exception.ConnectionError:
        pass


target_url = "http://167.71.54.69/"
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
        if input_type == "text":
            input_value = "<h1>test</h1>"
        # print(input)
            post_data[input_name] = input_value


    for input_type in post_data:
        result = requests.post(post_url, data=post_data)
        result_p_content = print(result.content)
        #print(result_p)



        # write the result.content in a file and save it
        with open("result.txt", "w") as text_file:
            print(result.content, file=text_file)

        # read the file with all the results and check if the webpage is vulnerable
        with open("result.txt", "r") as f:
            for line in f:
                if '<h1>test</h1>' not in line:
                    print(bcolors.CBLUE, "\r\n[+++++]", "Webpage has no XSS Vulnerability", "[+++++]")
                else:
                    print(bcolors.CRED, "\r\n[---------------------------------------------------------------------------]", "\r\n")
                    print(bcolors.CRED, "\r\n[---------------------------]", "\r\n[Form_Field:]", input_type, "\r\n[---------------------------]")
                    print(bcolors.CRED, "\r\n[-----]", "Webpage has an XSS Vulnerability", "[-----]", "\r\n")



