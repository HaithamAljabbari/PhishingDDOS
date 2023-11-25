from scapy.all import *

# Number of packets to send
num_packets = 5

# List to store received packets
received_packets = []

# Loop to send different types of packets
while True:

        # Send ICMP Echo Request
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
    response = sr1(packet, timeout=2)  # Wait 2 seconds for a response

    # Store the received packet in the list
    if response:
        received_packets.append(response)

# Display the received packets
for pkt in received_packets:
    pkt.show()
