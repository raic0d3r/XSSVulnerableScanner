import re, requests, os, sys
import html, urllib.request, urllib.error
from time import time as timer  
from multiprocessing.dummy import Pool
from pathlib import Path
from colorama import Fore                               
from colorama import Style
#from web import web
####### Colors   ###### 
fr  =   Fore.RED                                            
fc  =   Fore.CYAN                                           
fw  =   Fore.WHITE                                          
fg  =   Fore.GREEN                                          
sd  =   Style.DIM                                           
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT
                                        
#######################

def banners():
    try:
        os.mkdir('logs')
    except:
        pass
        
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;   XSS Scanner
             ;:::::'   :;     By RaiC0d3r
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

        \n""".format(fg, fr, fg, sn)
        
    print(banner)


Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    
def getoption():
    print("{}[1]{} Single Site".format(fg, fw))
    print("{}[2]{} Multiple Site".format(fg, fw))
    choiceoption=input('Put Number => ')
    if choiceoption=='1':
        url = input("\n\033[92m[!]\033[91m ENTER WEBSITE : ")
        start = timer()
        singlescan(url)
        print('Finished in : ' + str(timer() - start) + ' seconds')
        print("\n")
        if os.stat("logs/xss_paramaters").st_size == 0:
            print("\n")
        else:
            print("{}[1]{} Advanced Scan".format(fg, fw))
            print("{}[2]{} No Thanks".format(fg, fw))
            choiceoptions=input('Put Number => ')
            if choiceoptions=='1':
                print("{}{}Checking if the entry points are vulnerable...{}\n\n" .format(sn, fc, sn))
                os.system("gau "+url+" | gf xss | sed 's/=.*/=/' | sed 's/URL: //' | dalfox pipe -o xss.txt")
            elif choiceoptions=='2':
                exit()

    elif choiceoption=='2':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(multiplescan, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')

def singlescan(url):
    print("\n{}[+] Vulnerability: XSS{}\n".format(fg, sn))
    print("{}{}Finding XSS entry points in the domain...{}\n\n".format(sn, fc, sn))
    os.system("sudo gau "+url+"| gf xss | tee logs/xss_paramaters")
    print("\n")
    if os.stat("logs/xss_paramaters").st_size == 0:
        print("{}{}[😞]Not Found XSS entry points in the domain...{}\n\n" .format(sn, fc, sn))
    else:
        print("{}{}[😍]Checking if the entry points are vulnerable...{}\n\n" .format(sn, fc, sn))
        try:
            with open("logs/xss_paramaters", 'r') as f:
                domain = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(scanner, domain)

def multiplescan(url):
    print("\n{}[+] Vulnerability: XSS{}\n".format(fg, sn))
    print("{}{}Finding XSS entry points in the domain...{}\n\n".format(sn, fc, sn))
    os.system("sudo gau "+url+"| gf xss | tee logs/xss_paramaters")
    print("\n")
    if os.stat("logs/xss_paramaters").st_size == 0:
        print("{}{}[😞]Not Found XSS entry points in the domain...{}\n\n" .format(sn, fc, sn))
    else:
        print("{}{}[😍]Checking if the entry points are vulnerable...{}\n\n" .format(sn, fc, sn))
        try:
            with open("logs/xss_paramaters", 'r') as f:
                domain = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(scanner, domain)

def scanner(domain):
    try:
        payloads = open("Payloads.txt", 'r').read().splitlines()
        for payload in payloads:
            website = domain + payload
            source = urllib.request.urlopen(website).read()
            mystr = source.decode("utf8")
            if payload in mystr:
                print("\n{}[✓] Vulnerable =>{}{}\n".format(fg, website, sn))
                open('XSSVulnerable.txt', 'a').write(website+'\n')

    except urllib.error.URLError:
        pass

    except urllib.error.HTTPError:
        pass        

    except KeyboardInterrupt:
        raise KeyboardInterrupt

    except:
        pass

def installreq():
    print("\n{}[+] Installing Requirement{}\n".format(fg, sn))
    os.system("sudo su")
    os.system("go install github.com/tomnomnom/gf@latest && go install github.com/lc/gau@latest")
    os.system("cp ~/go/bin/gau /usr/bin && cp ~/go/bin/gf /usr/bin/")
    print("\n{}Installed Done{}\n".format(fg, sn))
    os.system("git clone https://github.com/Sherlock297/gf_patterns.git && cd gf_patterns/ && cp *.json ~/.gf")
    getoption()

banners()
path_to_file = '/usr/bin/gau'
path_to_file1 = '/usr/bin/gf'
path = Path(path_to_file)
path1 = Path(path_to_file1)

if path.is_file() & path1.is_file():
    #print(f'The file {path_to_file} & {path_to_file1} exists')
    getoption()
else:
    print(f'The file {path_to_file} & {path_to_file1} does not exist')
    installreq()
