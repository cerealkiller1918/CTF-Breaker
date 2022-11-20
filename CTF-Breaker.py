#!/usr/bin/env python3

import sys
from socket import *
from datetime import datetime
import requests
import io 
import os 
from http.server import *
import time
from socketserver import *
import base64 

def port_scanner(ip_address): 
    target = gethostbyname(ip_address)
    start_time = datetime.now()
    # Banner
    print("-"*50)
    print("Scanning Target:",target)
    print("Scanning started at:",str(start_time))
    print("-"*50)
    try:
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

        nmap(ports,target)
        
        ended_time = datetime.now()
        # Ending Banner
        print("-"*50)
        print("Scanned Target:",target)
        print("Scanning end at:",str(ended_time))
        print("The Scan took", str(ended_time-start_time),"to run")
        print("-"*50)


    except KeyboardInterrupt:
        print("\n Exiting Program !!!!!\n")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except socket.error:
        print("\n Server not responding !!!!")
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

def dirb(urls):
    arr=[]
    url=urls
    wordlist = os.getcwd() + "/directory-list-lowercase-2.3-medium.txt"
    sublist = ["",".txt",".php",".html"]
    try:
        if url[:7] != 'http://':
            url="http://"+url
        r=requests.get(url)
        if r.status_code == 200:
            print('Host is up.')
        else:
            print('Host is down.')
            return
        if os.path.exists(wordlist):
           with open(wordlist, "r") as wlist:
                for i in wlist:
                    for sub in sublist:
                        print(url+"/"+i+sub)
                        rq=requests.get(url+"/"+i+sub)
                        if rq.status_code == 200:
                            print(">OK".rjust(len(url+"/"+i+sub)+5,'-'))
                            arr.append(str(url+"/"+i+sub))
                        else:
                            print(">404".rjust(len(url+"/"+i+sub)+5,'-'))
                    
                print("output".center(100,'-'))
                l=1
                for i in arr:
                    print(l, "> ", i)
                    l+=1
        else:
            print(wordlist+" don't exists in the directory.")
    except Exception as e:
        print(e)

def webHosting(port):
    # TODO tring to rethink about how I am doing this
#    http.server(port)
    print("Working on it")
    print(os.environ.get('DESKTOP_SESSION'))
#    os.system(("python -m http.server " + port))
    
#    Handler = SimpleHTTPRequestHandler
#    http = TCPServer(("",int(port)),Handler)
#    print("serving at port",port)
#    http.serve_forever()

def decodeBase64(code):
    decode = base64.b64decode(code)
    print(decode)

def printTitle():
    print("""

 ██████╗████████╗███████╗    ██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║        ██║   █████╗█████╗██████╔╝██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝
██║        ██║   ██╔══╝╚════╝██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗   ██║   ██║         ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═╝         ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                     

    """)

def main_menu():
    while True:
        print("""
 1: Port Scanner    
 2: Web Hosting
 3: Dirbuster
 exit: Exit
 """)
        pick = input("> ")
        choices(pick)

def choices(pick):
    match pick:
        case "1":
            port_scanner(input("Enter IP Address: "))
        case "2":
            webHosting(input("Enter a port:"))
        case "3":
            url = input("Enter the url:")
            dirb(url)
        case "exit":
            print("Good Bye.")
            time.sleep(2)
            os.system("clear")
            exit()
        case _:
            print("Not a choice. ") 

def main():

    printTitle()
    main_menu()

if __name__ == '__main__':
    main()
