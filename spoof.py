from scapy.all import *
IFACE = "br-5de3b839fd4f"  # set here the interface of docker
SPOOFED_IP = "10.9.0.5"
VERBOSE=0

def traceroute(ip=SPOOFED_IP):
    TTL = 1
    print(f"Traceroute to {ip}...")
    while(TTL<255):
        response = sr1(IP(dst=ip, ttl=TTL)/ICMP(), iface=IFACE, verbose=VERBOSE)
        if response[0].src != ip:
            print(f"\t{TTL} ({response[0].src})")
            TTL += 1
        else:
            print(f"\t{TTL} ({response[0].src})")
            print("Done!")
            return 
    print("Error")

if __name__ == "__main__":
traceroute("8.8.8.8")
