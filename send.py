#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv) < 2:
        print 'pass 2 arguments: <IPv4 destination>'
        exit(1)

    addr_str = sys.argv[1]
    addr = socket.gethostbyname(addr_str)
    iface = get_if()

    switch = addr_str.split('.')
    host = int(switch[-1])
    switch = int(switch[-2])
    data = 'teste'

    print "sending on interface %s to %s" % (iface, str(addr))
    pkt =  Ether(src=get_if_hwaddr(iface), dst='00:00:00:00:%02x:%02x' % (switch, host) )
    pkt = pkt /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / data
    pkt.show2()
    print ' '
    print ' '
    print ' -----  PACOTE TESTE ENVIADO  ------ '
    print ' '
    sendp(pkt, iface=iface, verbose=False)


if __name__ == '__main__':
    main()
