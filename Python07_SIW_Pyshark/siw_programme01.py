import pyshark

count = 0
ip_list = []

capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='http && ip.dst ==  146.64.213.83')

for packet in capture:
    if packet.ip.dst not in ip_list:
        ip_list.append(packet.ip.dst)

print(ip_list)




