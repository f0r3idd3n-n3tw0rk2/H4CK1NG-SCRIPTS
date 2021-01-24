#!/usr/bin/env python



import requests
from bs4 import BeautifulSoup
import urlparse

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
    post_url = urlparse.urljoin(target_url, action)

    print(post_url)
    method = form.get("method")
    print(method)

    inputs_list = form.findAll("input")
    for input in inputs_list:
        input_name = input.get("name")
        print(input_name)