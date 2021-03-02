import pyshark

count = 0
request_uri = []

capture = pyshark.FileCapture('data-exfiltration1.pcap', display_filter='http && ip.dst ==  146.64.213.83')

for packet in capture:
    if packet.http.request not in request_uri:
        request_uri.append(packet.http.request)

print(request_uri)




