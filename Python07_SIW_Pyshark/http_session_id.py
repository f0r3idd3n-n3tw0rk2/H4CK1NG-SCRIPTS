import pyshark

count = 0

capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='ip contains amazon.in && ip.src==192.168.252.128')

for packet in capture:
    print(packet.http.cookie)
    break