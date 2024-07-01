import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

banner = (Fore.RED + """
▪  ·▄▄▄▄      ▄▄▄▄▄          ▄▄▄▄▄      ▄ •▄ ▄▄▄ . ▐ ▄ 
██ ██▪ ██     •██  ▪         •██  ▪     █▌▄▌▪▀▄.▀·•█▌▐█
▐█·▐█· ▐█▌     ▐█.▪ ▄█▀▄      ▐█.▪ ▄█▀▄ ▐▀▀▄·▐▀▀▪▄▐█▐▐▌
▐█▌██. ██      ▐█▌·▐█▌.▐▌     ▐█▌·▐█▌.▐▌▐█.█▌▐█▄▄▌██▐█▌
▀▀▀▀▀▀▀▀•      ▀▀▀  ▀█▄▀▪     ▀▀▀  ▀█▄▀▪·▀  ▀ ▀▀▀ ▀▀ █▪
                                                      by arviis.
""")

print(banner)
userid = input(Fore.WHITE + "\n [ID] Kullanıcı ID'si: \n")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")

print(Fore.WHITE + f'\n [TOKEN] Tokenin İlk 24 Hanesi: \n{Fore.CYAN + encodedStr}')

os.system('pause >nul') 
