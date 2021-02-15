import pyshark

count = 0
ip_list = []

capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='http.request.method==GET && http.host=="www.nytimes.com"')

for packet in capture:
    if packet.ip.dst not in ip_list:
        ip_list.append(packet.ip.dst)

print(ip_list)