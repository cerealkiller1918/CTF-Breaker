#! /usr/bin/python3 

import sys
from socket import *
from datetime import datetime
import requests
import io 
import os 

def port_scanner(ip_address): 
    target = gethostbyname(ip_address)
    start_time = datetime.now()
    # Banner
    print("-"*50)
    print("Scanning Target:",target)
    print("Scanning started at:",str(start_time))
    print("-"*50)

    try:
        # TODO Make a list to pass to Nmap 
        ports = []
        # Scans for open ports
        for port in range(1,65535):
            s = socket(AF_INET,SOCK_STREAM)
            setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            if result == 0:
                print("Port",port,"is open")
                ports.append(port)
            s.close()

        ended_time = datetime.now()
        # Ending Banner
        print("-"*50)
        print("Scanned Target:",target)
        print("Scanning end at:",str(ended_time))
        print("The Scan took", str(ended_time-start_time),"to run")
        print("-"*50)

        nmap(ports,target)

    except KeyboardInterrupt:
        print("\n Exiting Program !!!!!\n")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\ Server not responding !!!!")
        sys.exit()

def nmap(ports,target):
    print("Nmap scan")
    scanPorts =""
    count = 1
    for port in ports:
        if count < len(ports):
            count += 1 
            scanPorts += (str(port)+",")
        else:
            scanPorts += (str(port))
    #print(scanPorts)
    
    os.system(("nmap -p "+ scanPorts +" -sC -sV "+ target +" -oN nmap-scan"))

