#!/usr/bin/env python

import requests
import re
import urlparse
from BeautifulSoup import BeautifulSoup


class Scanner:
    def __init__(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

#Test Method "test_xss_in_form" in Function to use and test accessible abilities in forms and url in page
#Submit Test Script to the Form, Result is stored in the response
    def test_xss_in_form(self):
        xss_test_script = "<script>alert('Test')</script>"
        response = self.submit_form(form, xss_test_script, url)
        if xss_test_script in response.content:
            return True