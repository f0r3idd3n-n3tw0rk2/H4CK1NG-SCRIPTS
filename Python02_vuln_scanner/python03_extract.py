#!/usr/bin/env python



import requests
from bs4 import BeautifulSoup

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
    print(action)
    method = form.get("method")
    print(method)

    inputs_list = form.findAll("input")
    for input in inputs_list:
        print(input)