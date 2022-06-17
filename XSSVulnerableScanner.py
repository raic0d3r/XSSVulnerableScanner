import re, requests, os, sys
from time import time as timer	
from multiprocessing.dummy import Pool
from pathlib import Path
from colorama import Fore								
from colorama import Style
####### Colors	 ######	
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
              ;::::;  :;      XSS Scanner
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


def getoption():
    url = input("{}[1]{} ENTER WEBSITE : ".format(fg, fw))
    print("\n{}[+] Vulnerability: XSS{}\n".format(fg, sn))
    print("{}{}Trying to find XSS vulnerabilities...{}\n\n".format(sn, fc, sn))
    os.system("gau "+url+" | gf xss | sed 's/=.*/=/' | sed 's/URL: //' | dalfox pipe -o xss.txt")

def installreq():
    print("\n{}[+] Installing Requirement{}\n".format(fg, sn))
    os.system("sudo su")
    os.system("go install github.com/tomnomnom/gf@latest && go install github.com/lc/gau@latest && go install github.com/hahwul/dalfox/v2@latest")
    os.system("cp ~/go/bin/gau /usr/bin && cp ~/go/bin/gf /usr/bin/ && cp ~/go/bin/dalfox /usr/bin")
    print("\n{}Installed Done{}\n".format(fg, sn))
    os.system("git clone https://github.com/Sherlock297/gf_patterns.git && cd gf_patterns/ && cp *.json ~/.gf")
    getoption()

banners()
path_to_file = '/usr/bin/gau'
path_to_file1 = '/usr/bin/gf'
path_to_file2 = '/usr/bin/dalfox'
path = Path(path_to_file)
path1 = Path(path_to_file1)
path2 = Path(path_to_file2)
if path.is_file() & path1.is_file() & path2.is_file():
    print(f'The file {path_to_file} & {path_to_file1} & {path_to_file2} exists')
    getoption()
else:
    print(f'The file {path_to_file} & {path_to_file1} & {path_to_file2} does not exist')
    installreq()
