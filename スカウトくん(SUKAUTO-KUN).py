# To work you need to install the libraries below
import socket
import whois
import requests
import re
import threading

def find_ip():# This function find the IP from the domain ex: google.com
    url=input('Insert web site:\n')
    ip=socket.gethostbyname(url)
    print('')
    print('The IP is:',ip)
    print('')
    return main()

def find_whois_info():# This function send a whois request and print the results
    ip=input('Insert IP:\n')
    url=whois.whois(ip)
    print('')
    print(url)
    print('')
    return main()

def find_url_from_IP():# This function find the domain from an IP
    ip=input('Insert here your IP:\n')
    hostname= socket.gethostbyaddr(ip)
    print('')
    print ('This is the IP: {}\nand this is the hostname: {}'.format(ip,hostname))
    print ('')
    return main()

def print_urls():#this one print all the urls inside the html page that you given
  html = requests.get(input('inserisci url:\n')).text
  urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', html)
  print('')
  print(urls)
  print('')
  return main()

def scan():#This one run a simple port scan on a chosen IP adress and print also the banner on the open ports
  ip= input('Insert here the target:\n')
  def portscan(port): 
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     s.settimeout(1)
     try: 
         s.connect((ip,port))
         try:
              services= s.recv(1024).decode()
              print(f"Port {port} is open [+] running service {services}")
         except:
              print(f"Port {port} is open [+]")
     except:
         pass
  for port in range (0,65535):
      thread = threading.Thread(target=portscan, args=[port])
      thread.start()
  return main()    


def main():# This is the main function and it's scope has manage the other ones. It's allow you to call the others in orted to chose the function you need.
    print('Welcome chose your action:')
    print('1) Find IP from url\n2) Find whois info\n3) Find url from IP\n4) Find urls\n5) Port Scan\n6) Exit')
    chose = int(input())
    print('')
    if chose == 1:
        print(find_ip())
    elif chose == 2:
        print(find_whois_info())  
    elif chose == 3:
        print (find_url_from_IP())
    elif chose == 4:
        print(print_urls())
    elif chose == 5:
        print(scan())    
    elif chose == 6:   
        exit()

print(main())
