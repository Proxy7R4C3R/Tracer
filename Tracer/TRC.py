import socket 
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scaning Target ]' + str(target))
    for port in range (1,200):
        scan_port(converted_ip, port)

def get_banner(s):
    return s.recv(1024)

def check_ip(ip):
    try:

        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ip,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ip, port))
        try:
            banner = get_banner(sock)
            print ('[+] Open Port ' + str(port) +  ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:
        pass

targets = input('[+] Target/s Adress to Scan (Split with ,): ')
if ',' in targets:
    for ip in targets.split(','):
        scan(ip.strip(' '))
else:
    scan(targets)

