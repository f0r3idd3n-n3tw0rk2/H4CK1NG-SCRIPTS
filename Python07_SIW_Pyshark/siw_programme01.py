import pyshark

count = 0
request_uri = []

capture = pyshark.FileCapture('data-exfiltration1.pcap', display_filter='http && ip.dst ==  146.64.213.83')

for packet in capture:
    if http.request.full_uri not in request_uri:
        request_uri.append(http.request.full_uri)

print(request_uri)




