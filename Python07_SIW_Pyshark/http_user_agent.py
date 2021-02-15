import pyshark

count = 0

capture = pyshark.FileCapture('HTTP_traffic.pcap', display_filter='ip.src==192.168.252.128 && http')

for packet in capture:
    print(packet.http.user_agent)
    break