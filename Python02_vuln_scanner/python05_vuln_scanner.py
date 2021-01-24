#!/usr/bin/env python3

import python06_scanner


target_url = "http://167.71.54.69/"
vuln_scanner = python06_scanner.Scanner(target_url)
vuln_scanner.crawl(target_url)