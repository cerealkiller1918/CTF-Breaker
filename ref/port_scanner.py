import pyfiglet
import sys
import socket
from datetime import datetime
import requests 
import os 



def main():
	ascii_banner = pyfiglet.figlet_format("Killer - Hacker\n Port Scanner")
	print(ascii_banner)
	
	# Defining a target
	if len(sys.argv) == 2:

		# translate hostname to IPv4
		portscanner(sys.argv[1])
	else:
		print("Invalid amount of Argument")




def dirb(urls,wordlist):
	arr=[]
	url=urls
	try:
		if url[:7] != 'http://':
			url="http://"+url
		r=requests.get(url)
		if r.status_code == 200:
			print('Host is up.')
		else:
			print('Host is down.')
			return
		if os.path.exists(os.getcwd()+wordlist):
			fs=open(os.getcwd()+wordlist,"r")
			for i in fs:
				print(url+"/"+i)
				rq=requests.get(url+"/"+i)
				if rq.status_code == 200:
					print(">OK".rjust(len(url+"/"+i)+5,'-'))
					arr.append(str(url+"/"+i))
				else:
					print(">404".rjust(len(url+"/"+i)+5,'-'))
			fs.close()
			print("output".center(100,'-'))
			l=1
			for i in arr:
				print(l, "> ", i)
				l+=1
		else:
			print(wordlist+" don't exists in the directory.")
	except Exception as e:
		print(e)




def portscanner(ip_address):
	port80 = False
	
	target = socket.gethostbyname(ip_address)

	# Add Banner
	print("-" * 50)
	print("Scanning Target: " + target)
	print("Scanning started at:" + str(datetime.now()))
	print("-" * 50)

	try:
		
		# will scan ports between 1 to 65,535
		for port in range(1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			
			# returns an error indicator
			result = s.connect_ex((target,port))
			if result ==0:
				if port == 80:
					port80 = True
				print("Port {} is open".format(port))
			s.close()

		# if port80 == True:
		# 	print(pyfiglet.figlet_format("Web Serives"))
			
	except KeyboardInterrupt:
			print("\n Exiting Program !!!!")
			sys.exit()
	except socket.gaierror:
			print("\n Hostname Could Not Be Resolved !!!!")
			sys.exit()
	except socket.error:
			print("\ Server not responding !!!!")
			sys.exit()


if __name__ == '__main__':
	main() 