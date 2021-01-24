#!/usr/bin/env python


#This is a programm to get the URL and print the response of the html code back
#Then calling Beautifulsoup and giving it the response content for parsing

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
print(forms_list)