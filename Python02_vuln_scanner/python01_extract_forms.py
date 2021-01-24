#!/usr/bin/env python


#This is a programm to get the URL and print the response of the html code back
import requests
from bs4 import BeautifulSoup

def request(url):

    try:
        return requests.get(url)
    except requests.exception.ConnectionError:
        pass



target_url = "http://167.71.54.69/"
response = request(target_url)
print(response.content)