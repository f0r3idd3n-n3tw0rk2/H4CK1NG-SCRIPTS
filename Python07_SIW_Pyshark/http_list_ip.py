import pyshark

count = 0

url_list = []

capture = pyshark.FileCapture('HTTP_traffic.pcap',
                              display_filter='ip.src==192.168.252.128 && http && http.request.method=="GET"')

for packet in capture:
    host_name = packet.http.host
    host_name = ".".join(host_name.split('.')[-2:])
    if host_name not in url_list:
        url_list.append(host_name)

print(url_list)