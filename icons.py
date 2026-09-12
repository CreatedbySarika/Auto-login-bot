from colorama import Fore, Back, Style
import time

def intro():
    print(Fore.RED+'''
=================================================================
 _      ____   _____ _____ _   _             ____   ____ _______
| |    / __ \ / ____|_   _| \ | |           |  _ \ / __ \__   __|
| |   | |  | | |  __  | | |  \| |   _____   | |_) | |  | | | |
| |   | |  | | | |_ | | | | . ` |  |_____|  |  _ <| |  | | | |
| |___| |__| | |__| |_| |_| |\  |           | |_) | |__| | | |
|______\____/ \_____|_____|_| \_|           |____/ \____/  |_|

=================================================================
'''+Fore.BLACK)

def thinking(num):
    x=num
    while x != 0:
        print(Fore.MAGENTA+"==",end=" ")
        time.sleep(0.2)
        x = x-1
    print(">"+Fore.BLACK)
    time.sleep(0.3)
    #print("Done !")

thinking(3)

def star():
    print(Fore.YELLOW+
        '''
        
    ____/\___
    \        /
    /__    __\
        \/

    '''+Fore.BLACK
         )



    