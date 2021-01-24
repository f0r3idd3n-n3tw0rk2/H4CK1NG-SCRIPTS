#!/usr/bin/env python3



import requests
from bs4 import BeautifulSoup
import urllib.parse

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
    for input in inputs_list:
        input_name = input.get("name")
        input_type = input.get("type")
        print(input_type)