#! /usr/bin/python3 

import socket
from datetime import datetime

def port_scanner(ip_address):
    
    target = socket.gethostbyname(ip_address)

    # Banner
    print("-"*50)
    print("Scanning Target:",target)
    print("Scanning started at:",str(datetime.now()))

