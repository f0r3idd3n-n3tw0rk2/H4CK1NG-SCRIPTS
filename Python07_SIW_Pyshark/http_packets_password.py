import pyshark

count = 0

capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='http contains password')

for packet in capture:
    count = count + 1

print(count)