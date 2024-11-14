from BotServer.MainServer import MainServer
from cprint import cprint

Bot_Logo = """
███▄▄▄▄      ▄██████▄  ▀█████████▄   ▄██████▄      ███     
███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ▀█████████▄ 
███   ███   ███    █▀    ███    ███ ███    ███    ▀███▀▀██ 
███   ███  ▄███         ▄███▄▄▄██▀  ███    ███     ███   ▀ 
███   ███ ▀▀███ ████▄  ▀▀███▀▀▀██▄  ███    ███     ███     
███   ███   ███    ███   ███    ██▄ ███    ███     ███     
███   ███   ███    ███   ███    ███ ███    ███     ███     
 ▀█   █▀    ████████▀  ▄█████████▀   ▀██████▀     ▄████▀   
     Version: V2.1
     Author:                                          

"""

if __name__ == '__main__':
    cprint.info(Bot_Logo.strip())
    Ms = MainServer()
    Ms.processMsg()
