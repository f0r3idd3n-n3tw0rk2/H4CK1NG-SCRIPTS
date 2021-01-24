#!/usr/bin/env python3



import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

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
        #print(input)
        post_data[input_name] = input_value
        #print(input_value)
    result = requests.post(post_url, data=post_data)
    result_p = print(result.content)
    #print(result_p)


    #write the result.content in a file and save it
    with open("result.txt", "w") as text_file:
        print(result.content, file=text_file)


#read the file with all the results and check if the webpage is vulnerable



       # if
       # print("[-]", "Webpage is vulnerable")
       # else:
       # print("[+]", "Webpage has no XSS Vulnerability")


