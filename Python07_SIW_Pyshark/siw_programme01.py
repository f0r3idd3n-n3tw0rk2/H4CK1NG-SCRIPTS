import pyshark

count = 0
request_uri = []

capture = pyshark.FileCapture('data-exfiltration1.pcap', display_filter='http.request.method == GET && ip.src == 146.64.212.80 && http.request.uri.query.parameter')

for packet in capture:
    if packet.ip._all_fields.values not in request_uri:
        request_uri.append(packet.ip._all_fields.values)

    print(request_uri)




