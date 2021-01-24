#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup

def request(url):

    try:
        return requests.get(url)
    except requests.exception.ConnectionError:
        pass



target_url = "http://167.71.54.69/"
response = request(target_url)
print(response.content)