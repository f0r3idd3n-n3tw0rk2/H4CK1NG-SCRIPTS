#!/usr/bin/env python3

import requests
import re
import urllib.parse
from bs4 import BeautifulSoup


class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []

    def extract_links_from(self, url):
        response = requests.get(url)
        #html = response.read(response)
        #html = html.decode('ISO-8859-1')
        #htmltext = response.load().decode('utf-8')
        return re.findall("<title>(.*?)</title>", response.content)


    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urllib.parse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)


    def extract_form(self, url):
        response = self.session.get(url)
        parsed_html = BeautifulSoup(response.content, "html.parser")
        return  parsed_html.findAll("form")

    def submit_form(self, form, value, url):
        action = form.get("action")
        post_url = urllib.parse.urljoin(url, action)
        method = form.get("method")

        inputs_list = form.findAll("input")
        post_data = {}
        for input in inputs_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value
            post_data[input_name] = input_value
        if method == "post":
            return self.session.requests.post(post_url, data=post_data)
        return self.session.get(post_url, params=post_data)