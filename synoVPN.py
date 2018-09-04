#-*-coding:utf8;-*-
	
#this script checks first for network ip address
#it uses nmap to scan for all ip address in the same network
#it randomly selects an ip from the list and uses linux command to change ip
#gets new ip address and compare with old


__author__ = "festus murimi"
__copyright__ = "copyright (c) 2018"

import socket
import nmap 
import os
import time
import random
import sys
import warnings
import banner

#terminal colors

HEADER = '\033[95m' 
OKBLUE = '\033[94m' 
OKGREEN = '\033[92m' 
WARNING = '\033[93m' 
FAIL = '\033[91m' 
ENDC = '\033[0m' 
BOLD = '\033[1m' 
UNDERLINE = '\033[4m'

###checking for root access###
if os.getuid() != 0:
    print("You need root access to run anubis vpn\n Use sudo")
    sys.exit(0)
###checking for current os##
import platform 

current_os.lower() = platform.platform()#change results to lowercase and store current_os
#print (current_os)
if (current_os == 'windows' or current_os == 'mac'):
    print(FAIL+"+------------+-----------------------+")
    print(FAIL+"| script does not support your system|")
    print(FAIL+"+------------+-----------------------+")
    time.sleep(3)
    sys.exit(0)

nm = nmap.portScanner()

#determine the system ip address using socket
hostname = socket.getfqdn()
ip_address = socket.gethostbyname(hostname)

#print (ip_address)

#scanning all ip address in local network

try:
    #nmap -sP ip_address.*(ie) 198.68.12.*
    #os.system("ping -b+ ip_address")
    #all_ip_address = os.sytem(" arp -e")
    host_address = ip_address[:-1].append(-1, '*')
    nm.scan(host="host_address" arguments="-sP")
    for host in nm.all_host() if host != ip_address:
        #print(host)
        #export data to csv
        #edit file by determining delimiter
        #iterate over each row/comlumn
        try:
            new_ip = random.choice(host)
            ipaddress.IPV4Address('new_ip')
        except valueError:
            print("the netmask/ipaddress seems not to be valid for an ip4v address",+new_ip)
            time.sleep(3)
            sys.exit()
            
        #print(new_ip) 
        os.system("ifconfig eth0 +new_ip netmask 255.255.255.0 up")
        os.system("route add default gw +new_ip")#setting new default getway
        #os.system("""echo nameserver 1.1.1.1" > /etc/resolv.conf""")#setting Dns server 1.1.1.1


except:
    warnings.filterwarnings('ignore')#blocks ssl related warning
    print(FAIL+"the script could not change your ip address")
    time.sleep(3)
    sys.exit()
    
#checking again the system ip
new_ip_address = socket.gethostbyname(hostname)
if (ip_address != new_ip_address):
    return banner()
    print(OKGREEN+"+--------------------------+")
    print(OKGREEN+'| new ip'+ new_ip_address '|')
    print(OKGREEN+"+--------------------------+")
    time.sleep(5)
    sys.exit()
else:
    print(FAIL+"your ip has not changed"+new_ip_address, "please run the script again")
    time.sleep(3)
    sys.exit()

