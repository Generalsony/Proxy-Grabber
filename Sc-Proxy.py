import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import os
import sys
import time
from time import sleep
s='[+]Coded By Scream (General Sony)[+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
    time.sleep(5)
    s='[+]https://www.facebook.com/GeneralSony666[+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)
s='[+]https://www.facebook.com/groups/1886171651498073[+]'
for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    sleep (10. /90)

try:
    url = "https://free-proxy-list.net/"
    req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
    open_url = urllib.request.urlopen(req)
    data = open_url.read()
    soup = BeautifulSoup(data,'html.parser')
    proxy_file = open("Output.txt","w+")
    proxy_data = soup.find_all('tr')
    Pr_list = []
    for i in proxy_data:
        Pr = "http://{0}:{1}".format(BeautifulSoup(str(list(i)[0]),'html.parser').text,BeautifulSoup(str(list(i)[1]),'html.parser').text)
        Pr_list.append(Pr)
    Pr_list.remove(Pr_list[0])
    Pr_list.remove(Pr_list[-1])
    for p in Pr_list:
        proxy_file.write("{0}\n".format(p))
    proxy_file.close()
    print("[+]\033[5;49mProxy \033[5;49mSaved \033[5;49mSuccessfully[+]".format(len(Pr_list)))
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)
