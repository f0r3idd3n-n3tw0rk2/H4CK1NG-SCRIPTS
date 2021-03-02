import pyshark

count = 0
request_uri = []

capture = pyshark.FileCapture('data-exfiltration1.pcap', display_filter='http.request.method == GET && ip.src == 146.64.212.80 && http.request.uri.query.parameter')

for packet in capture:
    if packet.http.request_query_parameter not in request_uri:
        request_uri.append(packet.http.request_query_parameter)

    print(request_uri)





