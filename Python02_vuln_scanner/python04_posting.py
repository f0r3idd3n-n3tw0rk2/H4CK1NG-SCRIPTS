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
        post_data[input_name] = input_value
    result = requests.post(post_url, data=post_data)
    print(result.content)


#write the result.content in a file and save it
    with open("result.txt", "w") as text_file:
        #print(result.content, file=text_file)

#read the file with all the results and check if the webpage is vulnerable

        mylines = []  # Declare an empty list
        with open('result.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
            for line in myfile:  # For each line of text,
                mylines.append(line)  # add that line to the list.
            for element in mylines:  # For each element in the list,
                print(element)  # print it.
                if element == (print(mylines[0].find("first"))):
                    print("[-]", "Webpage is vulnerable")
                else:
                    print("[+]", "Webpage has no XSS Vulnerability")


