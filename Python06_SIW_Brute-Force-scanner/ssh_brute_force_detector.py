#!/usr/bin/python

import sys

# print("[+] First Parameter --> ", sys.argv[0])           # Script name
# print("[+] Second Parameter --> ", sys.argv[1])          # Number of failed logins

failed_logins = int(sys.argv[1])

if failed_logins != 0:
    with open("auth.log", "r") as f:
        log_lines = f.readlines()
        # print(type(content))
        ips_list = []
        for line in log_lines:
            if "pam_unix(sshd:auth): authentication failure;" in line:
                # print(line)
                line = line.strip().split(" ")
                # print(line)
                ips = line[-1].split("=")
                date = line[1] + " " + line[0] + " " + line[2]
                # print(date, " --> ", ips[1])
                ips_list.append(ips[1])
        # print(ips_list)

        ip_count = {}
        for ip in ips_list:
            count = ips_list.count(ip)
            ip_count[ip] = count
        # print(ip_count)

        for ips, counts in ip_count.items():
            if counts >= failed_logins:
                print("The IP", ips, "made", counts, "failed login attempts")

else:
    print("[+] You must enter a number other than zero")