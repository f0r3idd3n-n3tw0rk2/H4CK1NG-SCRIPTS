#!/usr/bin/env python3

import requests

r = requests.post('$host', data = {'field1':'name'})

payload = {'field1': 'name', 'field2': 'street'}
r = requests.post('$host', params = payload)