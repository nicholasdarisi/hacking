from scapy.all import *

ttl = 1
arrived = False
try:
    while not arrived:
        ip = IP(dst='8.8.8.8', ttl=ttl)
        packet = ip / ICMP()
        reply = sr1(packet, timeout=2, verbose=0)
        if reply is None:
            print(f"TTL {ttl}: no reply")
        elif reply.haslayer(ICMP):
            reply.show()
            if reply[ICMP].type == 0:
                arrived = True
            elif reply[ICMP].type == 11:
                print(f"TTL {ttl}: router intermedio")
        


        ttl += 1
except KeyboardInterrupt:
    print("Interrotto")