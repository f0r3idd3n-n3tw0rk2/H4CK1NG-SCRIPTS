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


    vuln_list = form.findAll(result.content)
    if vuln_list == "b'<table>\n<tr><td>first</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>last</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>email</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>street</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>street2</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>city</td><td><h1>test</h1></td></tr><tr><td>region</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>postal</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr><tr><td>location</td><td>&lt;h1&gt;test&lt;/h1&gt;</td></tr></table>\n'":
        print("[-]", "Webpage is vulnerable")
    else:
        print("[+]", "Webpage has no XSS Vulnerability")
