# To work you need to install the libraries below
# The function Crowling allow https://example.com input only
import socket
import whois
import requests
import re
import threading
import tkinter as tk


def interface():
    print('Hello and Welcome to スカウトくん(SUKAUTO-KUN)')
    print('Please chose your favourite Interface:\n')
    print('1) Command Line      2) Graphical User Interface      3)Exit\n')
    chose= int(input())
    if chose == 1:
        return main()
    elif chose == 2:
        return gui()
    elif chose == 3:
        exit()
    else :
        print('Please enter values​ 1 or 2 only\n')
        return interface()


def gui():
    gui= tk.Tk()
    gui.geometry('600x600')
    gui.title('スカウトくん(SUKAUTO-KUN).py')
    gui.resizable(True,True)
    gui.configure(background='black')

    result_text = tk.Text(gui, height=20, width=65)
    result_text.pack(pady=10)

    text=tk.Entry()
    text.pack()

    def find_ip(): # this function find an ip from te domain
      hostname= text.get()
      ip=socket.gethostbyname(hostname)
      result_text.delete(1.0, tk.END)
      result_text.insert(tk.END, f"The IP is: {ip}\n")



    def find_whois_info():# This function send a whois request and print the results
      whoi= text.get()
      output=whois.whois(whoi)
      result_text.delete(1.0, tk.END)
      result_text.insert(tk.END, f"{output}")


    def find_url_from_IP():# This function find the domain from an IP
      ip=text.get()
      hostname=socket.gethostbyaddr(ip)
      output='This is the IP: {}\nand this is the hostname: {}'.format(ip,hostname)
      result_text.delete(1.0, tk.END)
      result_text.insert(tk.END, f"{output}")


    def print_urls():#this one print all the urls inside the html page that you given
     inp = text.get()
     html= requests.get(inp)
     urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', html.text)
     result_text.delete(1.0, tk.END)
     result_text.insert(tk.END, f"{urls}")


    def scan():#This one run a simple port scan on a chosen IP adress and print also the banner on the open ports
     ip= text.get()

     def portscan(port): 
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.settimeout(1)
       try: 
           s.connect((ip,port))
           try:
               services= s.recv(1024).decode()
               result_text.insert(tk.END, f"Port {port} is open [+] running service {services}")
           except:
               result_text.insert(tk.END, f"Port {port} is open [+]")  
       except:
           pass
     
     result_text.delete(1.0, tk.END)  
     for port in range (0,65535):
         thread = threading.Thread(target=portscan, args=[port])
         thread.start()
  

    button= tk.Button(text='Find IP', command=find_ip) #this is the button for the function find ip
    button.pack()

    button_ip=tk.Button(text='Find report Whois', command= find_whois_info ) # this is the buttor of the whois function
    button_ip.pack()

    button_find=tk.Button(text='Find url from IP', command= find_url_from_IP ) # this is the button for the function url from ip
    button_find.pack()

    button= tk.Button(text='Crowler', command=print_urls) #this is the button for the crowling function
    button.pack()

    button= tk.Button(text='Portscan', command=scan) #this is the button for the portscan function
    button.pack()


    gui.mainloop()



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

def print_urls():#this one Crowl a web page
  html = requests.get(input('Insert url:\n')).text
  urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', html)
  print('')
  print(urls)
  print('')
  return main()

def scan():#This one run a simple port scan on a chosen IP adress and print also the banner on the open ports
  ip= input('insert ip:\n')
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

print(interface())
