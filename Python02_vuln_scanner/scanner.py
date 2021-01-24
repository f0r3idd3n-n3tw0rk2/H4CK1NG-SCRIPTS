#!/usr/bin/env python3

import requests
import re
import urllib.parse


class Scanner:
    def __init__(self, url):
        self.target_url = url
        self.target_links = []

    def extract_links_from(self, url):
        response = requests.get(url)
        #html = response.read(response)
        #html = html.decode('ISO-8859-1')
        return re.findall("<title>(.*?)</title>", response.content)


    def crawl(self, url):
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urllib.parse.urljoin(url, link)

            if "#" in link:
                link = link.split("#")[0]

            if self.target_url in link and link not in self.target_links:
                self.target_links.append(link)
                print(link)
                self.crawl(link)