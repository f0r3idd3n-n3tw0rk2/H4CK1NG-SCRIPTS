import pyshark

count = 0

unique_list = []

capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='dns.flags.response == 1')

for packet in capture:
    if packet.ip.src not in unique_list:
        unique_list.append(packet.ip.src)

print(unique_list)