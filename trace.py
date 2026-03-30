from scapy.all import *

target = "8.8.8.8"
ttl = 1

packet = IP(dst=target, ttl=ttl) / ICMP()

print("=== PACKET SENT ===")
packet.show()

reply = sr1(packet, timeout=3, verbose=0)

print("\n=== RAW REPLY OBJECT ===")
print(reply)

if reply is None:
    print(f"\nTTL {ttl}: no reply")
else:
    print("\n=== REPLY SUMMARY ===")
    print(reply.summary())

    print("\n=== FULL REPLY ===")
    reply.show()

    if reply.haslayer(ICMP):
        print("\n=== ICMP INFO ===")
        print("ICMP type:", reply[ICMP].type)
        print("ICMP code:", reply[ICMP].code)

        if reply[ICMP].type == 11:
            print("Result: Time Exceeded -> intermediate router")
        elif reply[ICMP].type == 0:
            print("Result: Echo Reply -> destination reached")
        else:
            print("Result: other ICMP response")
    else:
        print("Reply received, but no ICMP layer found")
