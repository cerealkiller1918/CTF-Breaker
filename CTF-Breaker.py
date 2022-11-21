#!/usr/bin/env python3
import binascii
import sys
from socket import *
from datetime import datetime
import requests
import os
from base64 import *


def port_scanner(ip_address):
    target = gethostbyname(ip_address)
    start_time = datetime.now()
    # Banner
    print("-" * 50)
    print("Scanning Target:", target)
    print("Scanning started at:", str(start_time))
    print("-" * 50)
    try:
        ports = []
        # Scans for open ports
        for port in range(1, 65535):
            s = socket(AF_INET, SOCK_STREAM)
            setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print("Port", port, "is open")
                ports.append(port)
            s.close()

        nmap(ports, target)

        ended_time = datetime.now()
        # Ending Banner
        print("-" * 50)
        print("Scanned Target:", target)
        print("Scanning end at:", str(ended_time))
        print("The Scan took", str(ended_time - start_time), "to run")
        print("-" * 50)


    except KeyboardInterrupt:
        print("\n Exiting Program !!!!!\n")
        sys.exit()
    except gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
    except error:
        print("\n Server not responding !!!!")
        sys.exit()


def nmap(ports, target):
    print("Nmap scan")
    scanPorts = ""
    count = 1
    for port in ports:
        if count < len(ports):
            count += 1
            scanPorts += (str(port) + ",")
        else:
            scanPorts += (str(port))
    # print(scanPorts)
    os.system(f"nmap -p {scanPorts} -sC -sV  {target} -oN nmap-scan")


def dirb(urls):
    arr = []
    url = urls
    wordlist = f"{os.getcwd()} /directory-list-lowercase-2.3-medium.txt"
    sublist = ["", ".txt", ".php", ".html"]
    try:
        if url[:7] != 'http://':
            url = f"http://{url}"
        r = requests.get(url)
        if r.status_code == 200:
            print('Host is up.')
        else:
            print('Host is down.')
            return
        if os.path.exists(wordlist):
            with open(wordlist, "r") as wlist:
                for i in wlist:
                    for sub in sublist:
                        print(url + "/" + i + sub)
                        rq = requests.get(url + "/" + i + sub)
                        if rq.status_code == 200:
                            print(">OK".rjust(len(url + "/" + i + sub) + 5, '-'))
                            arr.append(str(url + "/" + i + sub))
                        else:
                            print(">404".rjust(len(url + "/" + i + sub) + 5, '-'))

                print("output".center(100, '-'))
                num = 1
                for i in arr:
                    print(num, "> ", i)
                    num += 1
        else:
            print(f"{wordlist} don't exists in the directory.")
    except Exception as e:
        print(e)


def webHosting(port):
    # TODO trying to rethink about how I am doing this
    #    http.server(port)
    print("Working on it")
    print(os.environ.get('DESKTOP_SESSION'))


#    os.system(("python -m http.server " + port))

#    Handler = SimpleHTTPRequestHandler
#    http = TCPServer(("",int(port)),Handler)
#    print("serving at port",port)
#    http.serve_forever()

def printOutputBytes(message: bytes):
    print(f"Output: {message.decode('utf-8')}")


def decodeBase64(code):
    try:
        decoded = b64decode(code)
        printOutputBytes(decoded)
    except UnicodeDecodeError:
        print("Not Base64.")
        return
    except binascii.Error:
        print("Not Base64.")
        return


def encodeBase64(encodeMessage):
    try:
        printOutputBytes(b64encode(encodeMessage))
    except:
        print("Not Base64.")
        return


def decodeBase16(code):
    try:
        printOutputBytes(b16decode(code))
    except:
        print("Not Base16.")
        return


def encodeBase16(encodeMessage):
    try:
        printOutputBytes(b16encode(encodeMessage))
    except:
        print("Not Base16.")
        return


def decodeBase32(code):
    try:
        printOutputBytes(b16encode(code))
    except:
        print("Not Base32.")
        return


def encodeBase32(EncodeMessage):
    try:
        printOutputBytes(b32encode(EncodeMessage))
    except:
        print("Not Base32.")
        return


def autoDecode(encodeMessage):
    try:
        printOutputBytes(b64decode(encodeMessage))
        print("Base64")
    except:
        try:
            printOutputBytes(b32decode(encodeMessage))
            print("Base32")
        except:
            try:
                printOutputBytes(b16decode(encodeMessage))
                print("Base16")
            except:
                print("Not able to decode")


def printTitle():
    print("""

 ██████╗████████╗███████╗    ██████╗ ██████╗ ███████╗ █████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║        ██║   █████╗█████╗██████╔╝██████╔╝█████╗  ███████║█████╔╝ █████╗  ██████╔╝
██║        ██║   ██╔══╝╚════╝██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗   ██║   ██║         ██████╔╝██║  ██║███████╗██║  ██║██║  ██╗███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═╝         ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                     

    """)


# TODO add a menu for encode and decode

def encodeMenu():
    while True:
        print("""
1: Base64
2: Base32
3: Base16
back: Back
exit: Exit
        """)

        match input(">"):
            case "1":
                encodeBase64(input("Enter to encode Base64: "))
            case "2":
                encodeBase32(input("Enter to encode Base32: "))
            case "3":
                encodeBase16(input("Enter to encode Base16: "))
            case "back":
                main_menu()
                break
            case "exit":
                exit()
                break
            case _:
                print("Not a choice.")


def decodeMenu():
    while True:
        print("""
1: Base64
2: Base32
3: Base16
back: back
exit: exit
        """)
        match input(">"):
            case "1":
                decodeBase64(input("Enter Base64: "))
            case "2":
                decodeBase32("Enter Base32: ")
            case "3":
                decodeBase16(input("Enter Base16: "))
            case "back":
                main_menu()
                break
            case "exit":
                exit()
                break
            case _:
                print("Not a choice.")


def main_menu():
    while True:
        print("""
 1: Port Scanner    
 2: Web Hosting
 3: Dir buster
 4: Decoding
 5: Encoding
 6: Auto Decode
 exit: Exit
 """)
        match input(">"):
            case "1":
                port_scanner(input("Enter IP Address: "))
            case "2":
                webHosting(input("Enter a port:"))
            case "3":
                url = input("Enter the url:")
                dirb(url)
            case "4":
                decodeMenu()
                break
            case "5":
                encodeMenu()
                break
            case "6":
                autoDecode(input("Enter to decode: "))
            case "exit":
                exit()
            case _:
                print("Not a choice. ")


def main():
    printTitle()
    main_menu()


if __name__ == '__main__':
    main()
